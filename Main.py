#!/bin/python

#developed at https://github.com/WerIstLuka/Lithium

from lib.ReadFile import ReadFile
from lib.CheckInput import CheckInput

#cpu arch
#name, num, arguments, info
Instructions = []
Instructions.append(["mov", 1, 2, "none"])
Instructions.append(["add", 2, 2, "none"])
Instructions.append(["sub", 3, 2, "none"])
Instructions.append(["inc", 4, 1, "none"])
Instructions.append(["dec", 5, 1, "none"])
Instructions.append(["jmp", 6, 1, "jump"])
Instructions.append(["jov", 7, 1, "jump"])
Instructions.append(["jnz", 8, 1, "jump"])
Instructions.append(["jiz", 9, 1, "jump"])
Instructions.append(["ld", 10, 2, "none"])
Instructions.append(["st", 11, 2, "back"])
Instructions.append(["and", 12, 2, "none"])
Instructions.append(["xor", 13, 2, "none"])
Instructions.append(["not", 14, 1, "none"])
Instructions.append(["or", 15, 2, "none"])
Instructions.append(["shl", 16, 1, "none"])
Instructions.append(["shr", 17, 1, "none"])
Instructions.append(["slp", 18, 1, "none"])

File = ReadFile("Source.li")
print(File)
CheckInput(File, Instructions)