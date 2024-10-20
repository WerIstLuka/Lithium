#!/bin/pthon3

def ReadFile(FileName):
	with open(FileName, "r") as File:
		FileContent = File.read().splitlines()
	Output = []
	for LineCounter in FileContent:
		Output += [LineCounter.split()]
	return Output