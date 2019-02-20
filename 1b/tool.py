#!/usr/bin/python3
inputs = []
s = 0
outputs = []
with open('input.txt', 'r') as f:
    for i in f:
        inputs.append(i)
		
inputs = list(map(int,inputs))

for x in inputs:
	s = s + x
	outputs.append(s)
	for x in outputs:
	   
	
print(outputs)
	
