import random
import itertools
import random
import sys
from psychopy import visual, core, event



categories = {'Happy'='F', 'Angry'='W', 'Sad'='T'}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
responseMapping = {'up':1,'down':0}
numTrials = 40


def randomButNot(l,toExclude):
	chosen = random.choice(l)
	while toExclude in chosen:
		chosen = random.choice(l)
	return chosen

def generateTrials(numTrials):
	trials=[]
	propMatch  = .6
	for i in range(numTrials):
		emotionPrompt = random.choice(categories.keys())
		shownActor = random.choice(actors)
		isMatch = int(random.random()<propMatch)

		if isMatch:
			shownCategory = emotionPrompt
			targetFaceImage = shownActor+categories[emotionPrompt]+suffix
		else:
			shownCategory = randomButNot(categories.keys(), emotionPrompt)
			targetFaceImage = shownActor+categories[shownCategory]+suffix

		trials.append({	'isMatch':isMatch,
						'emotionPrompt':emotionPrompt,
						'shownActor':shownActor,
						'shownCategory':shownCategory,
						'targetFaceImage':targetFaceImage
						})

		return trials

trials = generateTrials(numTrials)

win = visual.Window([800,600],color="black", units='pix')
prompt = visual.TextStim(win=win,text='',color="white",height=60)
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)
pic = visual.ImageStim(win=win, mask=None,interpolate=True)

for curTrial in trials:
	win.flip()
	core.wait(25)
	prompt.setText(curTrial['emotionPrompt']+'?')
	prompt.draw()
	win.flip()
	core.wait(.5)

	win.flip()
	core.wait(.1)
	pic.setImage('faces/'+curTrial['targetFaceImage'])
	pic.draw()
	win.flip()
	response = event.waitKeys(keyList=responseMapping.values())[0]
	if response==responseMapping[curTrial['isMatch']]:
		correctFeedback.draw()
	else:
		correctFeedback.draw()
	win.flip()
	core.wait(.5)