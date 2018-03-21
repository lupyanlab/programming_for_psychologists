
import os


inFiles = [
'7-44_upright',
'7-44_inverted',
'ypcf_upright',
'ypcf_inverted',
'pipes_upright',
'pipes_inverted',
'gabors_upright',
'gabors_inverted',
]

inFiles = [
'11-11_upright',
'11-11_inverted',
'||-||_upright',
'||-||_inverted',
]



angles = range(1,17,1)
directions = {'right':'l','left':'r'}

for curInFile in inFiles:
	for curAngle in angles:
		for curDirection,directionSwitch in directions.items():
			outFile = curInFile.replace('_0','')+'_'+str(curAngle) + '_'+curDirection
			os.system('../skew -d b2'+directionSwitch +' -a '+str(curAngle)+' -b white ' + curInFile+'.png'+' '+outFile+'.png')


#
os.system('mogrify -shave 57x40 *_left*png')
os.system('mogrify -shave 57x40 *_right*png')
#os.system('mogrify -trim *png')



