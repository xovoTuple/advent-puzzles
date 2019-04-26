frequency = 0
inputs = []
with open('input.txt', 'r') as f:
	for i in f:
		inputs.append(i) 
	inputs = list(map(int,inputs))
	for x in inputs:
		frequency += x
	print(frequency)
	print(len(inputs))
	
