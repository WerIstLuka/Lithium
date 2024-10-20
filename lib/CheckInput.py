#!/bin/python3

def CheckInput(Input, Instructions):
	LineCounter = 0
	CalledFunctions = []
	DefinedFunctions = []
	for Line in Input:
		for Word in Line:
			IsInstruction = False
			for Instruction in Instructions:
				if Word == Instruction[0]:
					IsInstruction =  True
					break
			if IsInstruction == False:
				print(Word)
			#word is not an instruction
		LineCounter += 1