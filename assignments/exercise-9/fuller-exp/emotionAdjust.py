import os
import random
import socket
from psychopy import visual
from psychopy import core,event
from useful_functions import *
import generateTrials


expName = "emotion_adjust"
while True:
	runTimeVarOrder = ['subjCode','seed','gender','stimGender','expInitials']
	runTimeVars = getRunTimeVars({'subjCode':'emotions_101', 'gender':['Choose', 'm','f'], 'stimGender':['Choose', 'm','f', 'b'], 'seed':10, 'expInitials':''},runTimeVarOrder,expName)
	if 'Choose' in runTimeVars.values():
		popupError('Need to choose a value from a dropdown box')
	else:
		outputFile = openOutputFile('data/'+runTimeVars['subjCode'],expName)
		if outputFile:
			break

runTimeVars['room'] = socket.gethostname().upper()
generateTrials.generateTrials(runTimeVars,runTimeVarOrder)

win = visual.Window([800,600],color="gray", allowGUI=False, units='pix')
#win = visual.Window([1920,1080], color="gray", allowGUI=False, monitor='testingRoom',units='pix',winType='pyglet')

generateTrials.generateTrials(runTimeVars,runTimeVarOrder)
showText(win,textToShow="Loading pictures...",color="black",waitForKey=False)
pics = loadFiles('stimuli','jpg','image',win)
(header,trialListMatrix) = importTrialsWithHeader('trials/trialList_'+runTimeVars["subjCode"]+'.csv',separator=",")


emotionMorphText="Adjust emotion by moving the mouse wheel up or down until you find the point at which one emotion transitions to another emotion. When you are satisfied, click the left mouse button to go on to the next picture. This part will take about 2 minutes."
genderMorphText="Adjust gender by moving the mouse wheel up or down until you find the point at which male transitions to female (or female to male). When you are satisfied, click the left mouse button to go on to the next picture. This part will take about 2 minutes."
thanks = "Thank you. This part of the experiment is now complete."

fix = visual.TextStim(win,text='+',height=23,color="black")
delta = 1
maxStimNum=120
myMouse = event.Mouse(win=win)

expTimer = core.Clock()

def runTrial(curTrial):

		if curTrial['direction']=='left':
			stimNum='1'.zfill(3)
		else:
			stimNum=str(maxStimNum)
		win.flip()
		core.wait(1.0)
		win.flip()
		respTimer = core.Clock()
		numWheelTurnsUp=0
		numWheelTurnsDown=0
		
		while True:
			wheelRel = myMouse.getWheelRel()[1]
			if wheelRel<0.0:
				numWheelTurnsDown+=1
				if int(stimNum)>1:
					stimNum = str(int(stimNum)-delta).zfill(3) 
			elif wheelRel>0.0:
				numWheelTurnsUp+=1
				if int(stimNum)<maxStimNum:
					stimNum = str(int(stimNum)+delta).zfill(3) 
			elif myMouse.getPressed()[0]==1:
				rt = respTimer.getTime()
				if rt>.8 and (numWheelTurnsUp>0 or numWheelTurnsDown>0):
					break
			pics[curTrial['filename']]['stim'].draw()
			win.flip()

		fieldVars=[]
		for curField in fieldNames:
			fieldVars.append(curTrial[curField])
		curLine = createResp(optionList,subjVariables,fieldVars,
		a_expTimer = expTimer.getTime(),
		b_upClicks = numWheelTurnsUp,
		c_downClicks = numWheelTurnsDown,
		d_rt = rt*1000,
		e_resp = int(stimNum))
		writeToFile(outputFile,curLine)

		#write data to output file
		curTrial['header']=header
		responses=[curTrial[_] for _ in curTrial['header']]
		#write dep variables
		responses.extend(
			(expName,
			expTimer.getTime(),
			trialIndex,
			numWheelTurnsUp,
			numWheelTurnsDown,
			rt*1000,
			int(stimNum)))
		writeToFile(self.experiment.outputFile,responses,writeNewLine=True)


for trialnum,curTrial in enumerate(trialListMatrix):
	runTrial(trialNum,curTrial)
header.extend(['expName', 'expTimer', 'trialIndex', 'onsetDelay', 'responseKey', 'responseCode', 'isRight', 'RT'])
printHeader(header,headerFile="header.csv", separator=",")
showText(win,thanks,color="black",mouse=myMouse)
