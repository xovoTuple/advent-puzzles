#!/usr/bin/python3
inputs = []
s = 0
with open('input.txt', 'r') as f:
    for i in f:
        inputs.append(i)
		
inputs = list(map(int,inputs))

for x in inputs:
	s = s + x
print(s)
	
