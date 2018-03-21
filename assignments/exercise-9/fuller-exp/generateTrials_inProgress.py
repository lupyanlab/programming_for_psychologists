#!/usr/bin/env python

import random
from itertools import permutations
separator = ","
numIter = 4

stimTypes = list(permutations(['HA-left','HA-right','SA-left','SA-right'],4))
orderForGender = ['right','left']
codes = {'m':'man', 'f':'woman', 'AH':'ang-hap', 'HA':'ang-hap', 'AS':'sad-ang', 'SA':'sad-ang'}

def generateTrials(runTimeVars,runTimeVarsOrder):
	trialsFile = open('trials/trialList_'+runTimeVars['subjCode']+ '.csv','w')
	order = int(order)
	numRepeats = int(numRepeats)
	trialsFile = open('trialList_test_'+subjCode+ '.csv','w')
	writeToFile(trialsFile,curTrial)



	# if curTrial['morphType']=='emotion':
	# 	filename = curTrial['stimGender']+curTrial['continuumCode']+'_'+str(stimNum)
	# else:
	# 	filename = 'malefemalemorph'+'_'+str(stimNum)

	emotionMorphs=[]
	genderMorphs=[]
	numInBlock=0
	for i in range(numRepeats):
		curOrder = i+order
		if curOrder+numRepeats > len(stimTypes):
			curOrder -= len(stimTypes)
		for curContinuum in stimTypes[curOrder]:
			emotionMorphs.append(("emotion", str(numInBlock), codes[stimGender], str(i), codes[curContinuum.split('-')[0]],curContinuum.split('-')[0],curContinuum.split('-')[1]))
			numInBlock+=1
		genderMorphs.append(("gender", str(i), '*', str(i), '*','*',orderForGender[(curOrder+order) % 2]))

	if genderMorph=='n':
		for curTrial in emotionMorphs:
			writeToFile(trialsFile,curTrial)
	elif int(genderMorph)==1:
		for curTrial in genderMorphs:
			writeToFile(trialsFile,curTrial)
		for curTrial in emotionMorphs:
			writeToFile(trialsFile,curTrial)
	elif int(genderMorph)==2:
		for curTrial in emotionMorphs:
			writeToFile(trialsFile,curTrial)
		for curTrial in genderMorphs:
			writeToFile(trialsFile,curTrial)
							
if __name__ == "__main__":
    trialList = main('testTrials-13','m',16,'2',2)
