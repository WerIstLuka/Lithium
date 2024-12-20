#!/bin/python

#developed at https://github.com/WerIstLuka/Lithium

from lib.ReadFile import ReadFile
from lib.CheckInput import CheckInput
from lib.SanitizeInput import Sanitizer
from lib.ByteCounter import ByteCounter
# cpu arch
# name, num, arguments, info
Instructions = [
	["mov", 1, 2, "none"],
	["add", 2, 2, "none"],
	["sub", 3, 2, "none"],
	["inc", 4, 1, "none"],
	["dec", 5, 1, "none"],
	["jmp", 6, 1, "jump"],
	["jov", 7, 1, "jump"],
	["jnz", 8, 1, "jump"],
	["jiz", 9, 1, "jump"],
	["ld", 10, 2, "none"],
	["st", 11, 2, "back"],
	["and", 12, 2, "none"],
	["xor", 13, 2, "none"],
	["not", 14, 1, "none"],
	["or", 15, 2, "none"],
	["shl", 16, 1, "none"],
	["shr", 17, 1, "none"],
	["slp", 18, 1, "none"]]

# [0] special registers, [1] addresses for special registers
# [1] general purpose registers
Registers = [
	["out", "pc", "NULL"],
	[255, 254, 0],
	[1, 15]]

CPU = {
	"Bits": 64,
	"Bytes": 8,
	"RegAddrSizeBit": 8,
	"RegAddrSizeByte": 1
}

File = ReadFile("Source.li")
print(File)
CheckInput(File, Instructions, Registers)
SanitizedFile, LineList = Sanitizer(File, Instructions, Registers)
ByteCounter(SanitizedFile, Instructions, CPU)