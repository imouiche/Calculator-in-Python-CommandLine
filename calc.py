#!/usr/bin/env python

"""Simple calculator script in Python
Max depth = 2
@Author Inoussa Mouiche, 10/25/2018, 6pm Waterloo
"""

import sys, re

def validInput(ArgList):
	for arg in ArgList:
		if arg != 'add' and arg !='multiply':
			try:
				int(arg)
			except:
				print (arg + ' is not valid argument')
				sys.exit()

def add(List):
	i, s =0, 0
	#print (List, 'addf')
	while True:
		try:
			s += int(List[i])
			i +=1
		except:
			break
	#print (i, s, Inputs1[i:], List[i:], Inputs1[i], 'par add')
	if len(List[i:])!=0 and List[i]=='multiply':
		i +=1 
		return s+multiply(List[i:])
	elif len(List[i:])!=0 and List[i]=='add':
		i +=1
		return s+add(List[i:])
	
	return s

def multiply(List):
	i, s =0, 1
	while True:
		try:
			s *= int(List[i])

			i +=1
		except:
			#i+=1
			#print (List[i])
			break
	#print (i, s, List[i:], Inputs1[i], List[i], 'multip')
	if len(List[i:])!=0 and List[i]=='add':
		i +=1
		return s*multiply(List[i:])
	elif len(List[i:])!=0 and List[i]=='multiply':
		i +=1
		return s*add(List[i:])
			#break
	
	return s

if __name__ == '__main__':
	argList = sys.argv[1:]         # collect all argument except the funtion itself
	#sys.argv.pop(0)
	if len(argList[0].split())==1:
		print argList[0]

	else:

		Inputs=re.sub('[(){}<>]', '', argList[0]) #Remove unaccessary characters
		i,s = 0, 0
		Inputs1 = Inputs.split()
		validInput(Inputs1)                     # Validate all inputs
		
		if Inputs1[0] =='add': 
			i+=1
			CurrentSum = add(Inputs1[i:])
			print (CurrentSum, 'is the final result')
		if Inputs1[0] =='multiply': 
			i+=1
			CurrentSum = multiply(Inputs1[i:])
			print (CurrentSum, 'is the final result')
			