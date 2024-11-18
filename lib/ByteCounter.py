#!/bin/python3

from lib.IsInt import IsInt

def ByteCounter(Input, Instructions):
	ByteList = [0]
	for Line in Input:
		IsJump = False
		for Word in Line:
			if IsInt(Word) != "NaN":
				ByteList.append(ByteList[-1] + 8)
				IsJump = False
				continue
			if Word[0] == "$":
				ByteList.append(ByteList[-1] + 1)
				IsJump = False
				continue
			if IsJump == True:
				ByteList.append(ByteList[-1] + 8)
				IsJump = False
				continue
			for Instruction in Instructions:
				if Word == Instruction[0]:
					ByteList.append((ByteList[-1] + 1))
					if Instruction[3] == "jump":
						IsJump = True
	ByteList.pop(0)
	return ByteList