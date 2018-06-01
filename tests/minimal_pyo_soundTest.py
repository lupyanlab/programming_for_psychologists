from psychopy import core, visual, prefs, event
import pyo
prefs.general['audioLib'] = ['pyo']
from psychopy import sound
sound.init(48000,buffer=128)
win = visual.Window([300,200],color="black", units='pix')

tick = sound.Sound(800,secs=0.01)
tock = sound.Sound(600,secs=0.01)
white_circle = visual.Circle(win,size=50,fillColor="white",lineColor="black")
green_circle = visual.Circle(win,size=50,fillColor="green",lineColor="black")
prompt = visual.TextStim(win,text="Press 't' for a 800 hz sound\n 'o' for a 600 hz sound\n and 'q' to quit.",color="white",pos=(0,50))
prompt.autoDraw=True

win.flip()
while True:
	if event.getKeys(keyList=['t']):
		white_circle.draw()
		tick.play()
		win.flip()
		win.flip()
	if event.getKeys(keyList=['o']):
		green_circle.draw()
		tock.play()
		win.flip()
		win.flip()
	if event.getKeys(keyList=['q']):
		break
win.close()
core.quit()
