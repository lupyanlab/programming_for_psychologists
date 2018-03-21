#!/usr/bin/env python

import random
from itertools import permutations
separator = ","
numIter = 4

stimTypes = list(permutations(['HA-left','HA-right','SA-left','SA-right'],4))
orderForGender = ['right','left']
codes = {'m':'man', 'f':'woman', 'AH':'ang-hap', 'HA':'ang-hap', 'AS':'sad-ang', 'SA':'sad-ang'}
#random.seed(seed)
#seed = int(seed)	

def	main(subjCode,stimGender,order,genderMorph,numRepeats):
	order = int(order)
	numRepeats = int(numRepeats)
	testFile = open('trialList_test_'+subjCode+ '.csv','w')
	print >>testFile, separator.join(("morphType","numInBlock","stimGender","iteration", "continuum","continuumCode","direction","filename"))
	emotionMorphs=[]
	genderMorphs=[]
	numInBlock=0	
	for i in range(numRepeats):
		filename=''
		curOrder = i+order
		if curOrder+numRepeats > len(stimTypes):
			curOrder -= len(stimTypes)
		for curContinuum in stimTypes[curOrder]:
			filename = codes[stimGender]+curContinuum.split('-')[0]+'_'
			emotionMorphs.append(("emotion", str(numInBlock), codes[stimGender], str(i), codes[curContinuum.split('-')[0]],curContinuum.split('-')[0],curContinuum.split('-')[1], filename))
			numInBlock+=1
		filename = 'malefemalemorph_'
		genderMorphs.append(("gender", str(i), 'NA', str(i), 'NA','NA',orderForGender[(curOrder+order) % 2], filename))

	if genderMorph=='n':
		for curTrial in emotionMorphs:
			print >>testFile, separator.join(curTrial)
	elif int(genderMorph)==1:
		for curTrial in genderMorphs:
			print >>testFile, separator.join(curTrial)		
		for curTrial in emotionMorphs:
			print >>testFile, separator.join(curTrial)
	elif int(genderMorph)==2:
		for curTrial in emotionMorphs:
			print >>testFile, separator.join(curTrial)
		for curTrial in genderMorphs:
			print >>testFile, separator.join(curTrial)		
							
if __name__ == "__main__":
    trialList = main('testTrials-13','m',16,'2',2)
