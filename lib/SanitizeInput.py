#!/bin/python3

from lib.IsInt import IsInt

def Sanitizer(Input, Instructions, Registers):
	Output = []
	LineList = []
	for LineCount, Line in enumerate(Input):
		OutputLine = []
		for Word in Line:
			if Word[0] == "#":
				break
			if Word[0] == "$":
				if IsInt(Word[1:]) == "NaN":
					for i, Register in enumerate(Registers[0]):
						if Word[1:] == Register:
							OutputLine.append(f"${Registers[1][i]}")
				else:
					OutputLine.append(f"${IsInt(Word[1:])}")
				continue
			if IsInt(Word) != "NaN":
				OutputLine.append(IsInt(Word))
				continue
			OutputLine.append(Word)
		if OutputLine == []:
			continue
		LineList.append(LineCount+1)
		Output.append(OutputLine)
		print(OutputLine)
	print(LineList)
	return Output, LineList