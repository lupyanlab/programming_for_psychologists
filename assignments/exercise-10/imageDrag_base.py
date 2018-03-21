mport random
from psychopy import visual, core, event
from useful_functions import loadFiles, calculateRectangularCoordinates

win = visual.Window([900, 850], color="white", allowGUI=False, units='pix')
pics = loadFiles('stimuli', 'png', 'image', win)
numPics = len(pics.keys())
positions = calculateRectangularCoordinates(150, 150, numPics / 4, numPics / 5)
random.shuffle(positions)
mouse = event.Mouse(win=win)

done = visual.Circle(win,lineColor="orange",fillColor="orange",size=100,autoDraw=True)
doneText = visual.TextStim(win,text="Done",color="black",height=25)
doneText.setAutoDraw(True)
done.setPos((0,-320))
doneText.setPos((0,-320))


#keep going

#draw all the stims in their initial positions

#now allow user to move the stimuli and end by clicking on the orange button
