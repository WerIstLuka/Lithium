#!/bin/python3

def IsInt(Num):
	try:
		int(Num)
	except Exception:
		if len(Num) > 2:
			IsBin = False
			IsHex = False
			if Num[:2] == "0x":
				try:
					int(Num, 16)
					IsHex = True
				except Exception:
					return "NaN"
			if Num[:2] == "0b":
				try:
					int(Num, 2)
					IsBin = True
				except Exception:
					return "NaN"
			if IsHex == True:
				return int(Num, 16)
			if IsBin == True:
				return int(Num, 2)
		return "NaN"
	return int(Num)
IsInt("0x1")