#!/bin/python3

from lib.IsInt import IsInt

def CheckArgument(Arguments,Word ,Line):
	if Arguments == 0:
		print(f"Argument not expected on line {Line}: {Word}")
		quit()
	return Arguments - 1

def FunctionChecker(Called, Defined):
	for D in Defined:
		HasWord = False
		for C in Called:
			if D[0][:-1] == C[0]:
				HasWord = True
				continue
		if HasWord == False:
			print(f"Label \"{D[0][:-1]}\" was defined on line {D[1]} but was never called")
		LineList = []
		for i in Defined:
			if D[0] == i[0]:
				LineList.append(str(i[1]))
		if len(LineList) != 1:
			Lines = ", ".join(LineList)
			print(f"Label \"{D[0]}\" was defined on lines: {Lines}")
			quit()
	for C in Called:
		HasWord = False
		for D in Defined:
			if C[0] == D[0][:-1]:
				HasWord = True
				continue
			if HasWord == False:
				print(f"Label \"{C[0]}\" was called on line {C[1]} but was never defined")
				quit()

def CheckInput(Input, Instructions, Registers):
	CalledFunctions = []
	DefinedFunctions = []
	UnknownWords = []
	Arguments = 0
	for LineCounter, Line in enumerate(Input):
		#Arguments = 0
		JumpInstruction = False
		# if Arguments != 0:
		# 	print(f"missing argument on line: {LineCounter+1}")
		# 	quit()
		for Word in Line:
			if Word[0] == "$" and IsInt(Word[1:]) != "NaN":
				Arguments = CheckArgument(Arguments, Word, LineCounter+1)
			else:
				if Word[1:] in Registers[0]:
					Arguments = CheckArgument(Arguments, Word, LineCounter+1)
				else:
					if type(IsInt(Word)) == type(int()):
						Arguments = CheckArgument(Arguments, Word, LineCounter+1)
					else:
						if Word[0] == "#":
							break
						else:
							if Word[-1] == ":":
								DefinedFunctions.append([Word, LineCounter+1])
							else:
								IsInstruction = False
								if Arguments != 0:
									if JumpInstruction == True:
										Arguments = CheckArgument(Arguments, Word, LineCounter + 1)
										CalledFunctions.append([Word, LineCounter+1])
										JumpInstruction = False
									else:
										print(f"Unexpected operation \"{Word}\" on line: {LineCounter+1}")
										quit()
								for Instruction in Instructions:
									if Word == Instruction[0]:
										IsInstruction = True
										Arguments = Instruction[2]
										if Instruction[3] == "jump":
											JumpInstruction = True
										break
								if IsInstruction == False:
									UnknownWords.append([Word, LineCounter])
	for i in UnknownWords:
		FoundWord = False
		for CFunction in CalledFunctions:
			if i[0] in CFunction:
				FoundWord = True
		for DFunction in DefinedFunctions:
			if i[0] in DFunction:
				FoundWord = True
		if FoundWord == False:
			print(f"Unknown word: {i[0]} on line: {i[1]}")
			quit()
	FunctionChecker(CalledFunctions, DefinedFunctions)