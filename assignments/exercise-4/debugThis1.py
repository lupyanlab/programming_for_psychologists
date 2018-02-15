import time
import random
from psychopy import visual, core, event,sound
win = visual.Window([800,600],color="blak", units='pix')

rect = visual.Rect(win,fillColor="blue",size=size)
aspect = {'wide':[200,100], 'narrow':[100,200]}
validKeys = {'wide':'w', 'narrow':'n'}

bleep = sound.Sound('sounds/bleep.wav')
buzz = sound.Sound('sounds/buzz.wav')

for curIter in range(20)
	win.flip()
	core.wait(.5)
	curAspect  = random.choice(aspect.values())
	rect.setSize(aspect[curAspect])
	rect.draw()
	win.flip()
	timer = core.Timer()
	resp = event.waitKeys(keyList=validKeys.values())
	if resp==validKeys[aspect]:
		print 1, timer.getTime()
		bleep.play()
	else:
		print 0, timer.getTime()
		buzz.play()