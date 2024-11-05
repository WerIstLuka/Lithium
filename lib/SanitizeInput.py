#!/bin/python3

from lib.IsInt import IsInt

def Sanitizer(Input, Instructions, Registers):
	Output = []
	for Line in Input:
		if Line == []:
			continue
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
		Output.append(OutputLine)
		print(OutputLine)
	return Output
# todo
# line count converter from sanitized file to source file
# if line gets removed increment counter
# have a list the length of the amount of lines in sanitized file and for each line have the number of skipped lines