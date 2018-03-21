from psychopy import core, visual, prefs, event
from useful_functions import loadFiles
win = visual.Window([800,600],color="black", units='pix')
myMouse = event.Mouse()
myMouse.setVisible(0)

pics =  loadFiles('stimuli/','.png','image', win=win)
adjustStim = visual.GratingStim(win=win,tex='sin', mask='gauss',interpolate=True, size=[8,96], pos=[0,-150], color="white")


def do_adjustment(pic):
	numWheelTurnsDown=numWheelTurnsUp=0
	responded=False
	while not responded:
		pics[pic]['stim'].draw()
		adjustStim.draw()

		#insert your code here

		if myMouse.getPressed()[0]==1:
			responded=True
			print 'responded'
		win.flip()
	

for i in range(10):
	do_adjustment(random.choice(pics.keys()))


