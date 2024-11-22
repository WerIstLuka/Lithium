#!/bin/python3

def IsInt(Num):
	try:
		int(Num)
		return int(Num)
	except ValueError:
		pass
	if Num[:2] == "0b":
		try:
			int(Num, 2)
			return int(Num, 2)
		except ValueError:
			pass
	if Num[:2] == "0x":
		try:
			int(Num, 16)
			return int(Num, 16)
		except ValueError:
			pass
	return "NaN"
