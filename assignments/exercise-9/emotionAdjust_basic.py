import os
import random
from psychopy import visual, core, event
import pandas as pd
from useful_functions import loadFiles


win = visual.Window([800,700],color="gray", allowGUI=False, units='pix')
myMouse = event.Mouse(win=win,visible=False)

#win = visual.Window([1920,1080], color="gray", allowGUI=False, monitor='testingRoom',units='pix',winType='pyglet')
visual.TextStim(win,text="Loading images...", color="black",height=40).draw()
win.flip()


def showText(win,text,color,mouse):
	visual.TextStim(win,text=text,color=color,height=30).draw()
	win.flip()
	if mouse:
		while True:
			while any(mouse.getPressed()):
				if not any(mouse.getPressed()):
					return
	else:
		event.waitKeys()
		return

pics = loadFiles('stimuli','jpg','image',win)
emotionMorphText="Adjust the emotion of the face by moving the mouse wheel up or down until you find the point at which one emotion transitions to another emotion. When you are satisfied, click the left mouse button to go on to the next picture."
genderMorphText="Adjust the gender of the face by moving the mouse wheel up or down until you find the transition from male-to-female or female-to-make. When you are satisfied, click the left mouse button to go on to the next picture."

delta = 1
maxStimNum=120
expTimer = core.Clock()

trials = pd.read_csv('trials/sampleTrials.csv')
trials = trials.to_dict('records')


def runTrial(curTrial):
		if curTrial['direction']=='left':
			stimNum='1'.zfill(3)
		else:
			stimNum=str(maxStimNum)
		win.flip()
		core.wait(1.0)
		win.flip()
		respTimer = core.Clock()
		numWheelTurnsUp = numWheelTurnsDown = 0
		
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
			pics[curTrial['filename']+str(stimNum)]['stim'].draw()
			win.flip()

for curTrial in trials:
	print curTrial['trialIndex'], curTrial['morphType']
	if curTrial['trialIndex']==0 and curTrial['morphType']=="emotion":
		showText(win,emotionMorphText,color="black",mouse=myMouse)
	elif curTrial['trialIndex']==0 and curTrial['morphType']=="gender":
		showText(win,genderMorphText,color="black",mouse=myMouse)

	runTrial(curTrial)
showText(win,thanks,color="black",mouse=myMouse)
