#!/bin/python3

def IsInt(Num):
	try:
		int(Num)
	except Exception:
		if len(Num) > 2:
			if Num[:2] == "0x":
				try:
					int(Num, 16)
				except Exception:
					return False
			if Num[:2] == "0b":
				try:
					int(Num, 2)
				except Exception:
					return False
		return False
	return True