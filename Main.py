#!/bin/python

#developed at https://github.com/WerIstLuka/Lithium

from lib.ReadFile import ReadFile
from lib.CheckInput import CheckInput

#cpu arch
#name, num, arguments, info
Instructions = [
	["mov", 1, 2, "none"],
	["add", 2, 2, "none"],
	["sub", 3, 2, "none"],
	["inc", 4, 1, "none"],
	["dec", 5, 1, "none"],
	["jmp", 6, 2, "jump"],
	["jov", 7, 2, "jump"],
	["jnz", 8, 2, "jump"],
	["jiz", 9, 2, "jump"],
	["ld", 10, 2, "none"],
	["st", 11, 2, "back"],
	["and", 12, 2, "none"],
	["xor", 13, 2, "none"],
	["not", 14, 1, "none"],
	["or", 15, 2, "none"],
	["shl", 16, 1, "none"],
	["shr", 17, 1, "none"],
	["slp", 18, 1, "none"]]

Registers = [
	["out", "pc"],
	[255, 254]
]

File = ReadFile("Source.li")
print(File)
CheckInput(File, Instructions, Registers)