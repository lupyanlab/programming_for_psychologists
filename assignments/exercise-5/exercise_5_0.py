from psychopy import visual, core, event
import random
 
win = visual.Window([800,600],color="black", units='pix')
 
circle = visual.Circle(win,size = 20)
square = visual.Rect(win,size = 40)
locations = [[-15,0], [15,0]]
colors = ['blue', 'blue']
 
circle.setPos(locations[0])
circle.setFillColor(colors[0])
circle.setLineColor(colors[0])
circle.draw()

square.setPos(locations[1])
square.setFillColor(colors[1])
square.setLineColor(colors[1])
square.draw()

win.flip()

event.waitKeys('q')
win.close()
core.quit()