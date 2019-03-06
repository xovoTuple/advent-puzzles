def get_input():
	inputs = []
	with open('input.txt', 'r') as f:
		for i in f:
			inputs.append(i) #create list of input frequencies. str at this point!
		
		inputs = list(map(int,inputs)) #map str to int
		return inputs		

def get_output(inputs):
	outputs = []
	s = 0
	for x in inputs:
		s = s + x
		outputs.append(s)
	length = len(outputs)
	if length != len(inputs) : print("input and output lists are unequal length") #make sure input and output lists have same number of elements
	return outputs, length

def comparator(outputs, length):
	matched_frequencies = []
	print(length)
	outputs = outputs[0]
	#for i in length:
	#	for j in range(i + 1, length):
	#		if outputs[i] == outputs[j]:
	#			matched_frequencies.append()
	#			return matched_frequencies

	#no_of_matches = len(matched_frequencies)
	#print('found {} output values'.format(length))

inputs = get_input()
outputs, length  = get_output(inputs)
comparator(outputs, length)
