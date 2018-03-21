import os
import glob
import math
import pickle
from psychopy import core, visual, prefs, event, gui,misc
from psychopy import sound


try:
	import pygame
except ImportError:
	print "no pygame installed. no worries..."
 


def importTrialsWithHeader(trialsFilename, colNames=None, separator=',', header=True):
	try:
		trialsFile = open(trialsFilename, 'rb')
	except IOError:
		print trialsFilename, 'is not a valid file'
	
	if colNames is None: # Assume the first row contains the column names
		colNames = trialsFile.next().rstrip().split(separator)
	trialsList = []
	for trialStr in trialsFile:
		trialList = trialStr.rstrip().split(separator)
		print len(trialList), len(colNames), colNames
		assert len(trialList) == len(colNames)
		trialDict = dict(zip(colNames, trialList))
		trialsList.append(trialDict)
	if header:
		return (colNames, trialsList)
	else:
		return trialsList

def printHeader(header,headerFile='header.txt',separator="\t", overwrite=False):
	if overwrite or (not overwrite and not os.path.isfile(headerFile)):
		headerFile = open('header.txt','w')
		writeToFile(headerFile,header,writeNewLine=True)
		return True
	else:
		return False		

def evaluateLists(trialList):
	assert isinstance(trialList,list)
	for curTrial in trialList:
		assert isinstance(curTrial,dict)
		for key,value in curTrial.items():
			try:
				if isinstance(eval(curTrial[key]),list) or isinstance(eval(curTrial[key]),dict) or isinstance(eval(curTrial[key]),tuple):
					curTrial[key]=eval(value)
			except:
				pass
	return trialList

def popupError(text):
	errorDlg = gui.Dlg(title="Error", pos=(400,400))
	errorDlg.addText('Error: '+text, color='Red')
	errorDlg.show()
	
def getSubjCode(preFilledInText=''):
	 userVar = {'subjCode':preFilledInText}
	 dlg = gui.DlgFromDict(userVar)
	 return userVar['subjCode']

def getRunTimeVars(varsToGet,order,expName):
	"""Get run time variables, see http://www.psychopy.org/api/gui.html for explanation"""
	order.append('expName')
	varsToGet['expName']= expName
	try:
		previousRunTime = pickle.load( open( expName+'_lastParams.pickle', "rb" ) )
		for curVar in previousRunTime.keys():
			if isinstance(varsToGet[curVar],list):
				pass #don't load in list choices
			else:
				varsToGet[curVar] = previousRunTime[curVar]
	except:
		print "No previous runtime variables to load."
	infoDlg = gui.DlgFromDict(dictionary=varsToGet, title=expName, fixed=[expName],order=order)	
	pickle.dump(varsToGet,open(expName+'_lastParams.pickle','w'))
	if infoDlg.OK:
		return varsToGet
	else: print 'User Cancelled'

def openOutputFile(subjCode,suffix):
	if  os.path.isfile(subjCode+'_'+suffix):
		popupError('Error: That subject code already exists')
		return False
	else:
		try:
			outputFile = open(subjCode+'_'+suffix,'w')
		except:
			print 'could not open file for writing'
		return outputFile


def getKeyboardResponse(validResponses,duration=0):
	event.clearEvents()
	responded = False
	done = False
	rt = '*'
	responseTimer = core.Clock()
	while True: 
		if not responded:
			responded = event.getKeys(keyList=validResponses, timeStamped=responseTimer) 
		if duration>0:
			if responseTimer.getTime() > duration:
				break
		else: #end on response
			if responded:
				break
	if not responded:
		return ['*','*']
	else:
		return responded[0] #only get the first resp



def getMouseResponse(mouse,duration=0):
	event.clearEvents()
	responseTimer = core.Clock()
	numButtons=len(event.mouseButtons)
	response = [0]*numButtons
	timeElapsed = False
	mouse.clickReset()
	responseTimer.reset()
	rt = '*'
	while not any(response) and not timeElapsed:
		(response,rt) = mouse.getPressed(getTime=True)
		if duration>0 and responseTimer.getTime() > duration:
			timeElapsed=True
	
	if not any(response): #if there was no response (would only happen if duration is set)
		return ('*','*')
	else:
		nonZeroResponses = filter(lambda x: x>0,rt)
		firstResponseButtonIndex = rt.index(min(nonZeroResponses)) #only care about the first (earliest) click
		return (firstResponseButtonIndex,rt[firstResponseButtonIndex])


def writeToFile(fileHandle,trial,separator=',', sync=True,writeNewLine=True):
	"""Writes a trial (array of lists) to a previously opened file"""
	line = separator.join([str(i) for i in trial]) #TABify
	if writeNewLine:
		line += '\n' #add a newline
	try:
		fileHandle.write(line)
	except:
		print 'file is not open for writing'
	if sync:
			fileHandle.flush()
			os.fsync(fileHandle)
			
def polarToRect(angleList,radius):
	"""Accepts a list of angles and a radius.  Outputs the x,y positions for the angles"""
	coords=[]
	for curAngle in angleList:
		radAngle = (float(curAngle)*2.0*math.pi)/360.0
		xCoord = round(float(radius)*math.cos(radAngle),0)
		yCoord = round(float(radius)*math.sin(radAngle),0)
		coords.append([xCoord,yCoord])
	return coords

					

def loadFiles(directory,extension,fileType,win='',whichFiles='*',stimList=[]):
	""" Load all the pics and sounds. Uses pyo or pygame for the sound library (see prefs.general['audioLib'])"""
	path = os.getcwd() #set path to current directory
	if isinstance(extension,list):
		fileList = []
		for curExtension in extension:
			fileList.extend(glob.glob(os.path.join(path,directory,whichFiles+curExtension)))
	else:
		fileList = glob.glob(os.path.join(path,directory,whichFiles+extension))
	fileMatrix = {} #initialize fileMatrix  as a dict because it'll be accessed by file names (picture names, sound names)
	for num,curFile in enumerate(fileList):
		fullPath = curFile
		fullFileName = os.path.basename(fullPath)
		stimFile = os.path.splitext(fullFileName)[0]
		if fileType=="image":
			try:
				stim = visual.ImageStim(win, image=fullPath,mask=None,interpolate=True)
				(width,height) = (stim.size[0],stim.size[1])
				fileMatrix[stimFile] = {'stim':stim,'fullPath':fullPath,'filename':stimFile,'num':num,'width':width, 'height':height}
			except:
				print "Need to define window before loading stimuli"
		elif fileType=="sound":
			fileMatrix[stimFile] = {'stim':sound.Sound(fullPath), 'duration':sound.Sound(fullPath).getDuration()}

	#optionally check a list of desired stimuli against those that've been loaded
	if stimList and set(fileMatrix.keys()).intersection(stimList) != set(stimList):
		popupError(str(set(stimList).difference(fileMatrix.keys())) + " does not exist in " + path+'\\'+directory) 
	return fileMatrix

	
def	calculateRectangularCoordinates(distanceX, distanceY, numCols, numRows,yOffset=0,xOffset=0):
	coords = [[0,0]]*numCols*numRows
	curObj=0
	for curCol in range(0,numCols): #x-coord
		for curRow in range(0,numRows): #y-coord
			coords[curObj]= (curCol*distanceX, curRow*distanceY)
			curObj=curObj+1
	xCorrected = max([coord[0] for coord in coords])/2 -xOffset
	yCorrected = max([coord[1] for coord in coords])/2 -yOffset

	return [(coord[0]-xCorrected, coord[1]-yCorrected) for coord in coords]
	
	
def setAndPresentStimulus(win,stimuli,duration=0):
	"""Stimuli can be a list or a single draw-able stimulus"""
	if isinstance(stimuli,list):
		for curStim in stimuli:
			curStim.draw()
	else:
		stimuli.draw()
	if duration==0: #single frame
		win.flip()
	else: 
		win.flip()
		core.wait(duration)
	return





			
			
			