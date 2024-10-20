#!/bin/python3

from lib.IsInt import IsInt

def CheckInput(Input, Instructions):
	LineCounter = 0
	CalledFunctions = []
	DefinedFunctions = []
	for Line in Input:
		for Word in Line:
			IsInstruction = False
			for Instruction in Instructions:
				if Word == Instruction[0]:
					IsInstruction = True
					break
			if IsInstruction == False:
				if IsInt(Word) == False:
					print(Word)
		LineCounter += 1