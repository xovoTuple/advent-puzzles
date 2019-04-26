def get_input():
	inputs = []
	inputs_test = [1, -2, 3, 1, 1, -2, 3, 1]
	with open('input.txt', 'r') as f: #read input text file
		for i in f:
			inputs.append(i) #create list of input frequencies. str at this point!
		
		inputs = list(map(int,inputs)) #map str to int
		return inputs, inputs_test

def get_output(inputs, inputs_test):
	outputs = []
	outputs_test = [0]
	s = 0
	s_test = 0
	for x in inputs:
		s = s + x
		outputs.append(s)
	length = len(outputs)
	if length != len(inputs) : print("input and output lists are unequal length") #make sure input and output lists have same number of elements
	for x in inputs_test:
		s_test = s_test + x
		outputs_test.append(s_test)
	length = len(outputs)
	length_test = len(outputs_test)
	return outputs, outputs_test, length, length_test

def comparator(outputs, outputs_test, length, length_test):
	matched_frequencies = []
	matched_frequencies_test = [0]
	print("length of outputs list is: {}".format(length_test))
	#outputs = outputs[0]
	print("outputs list is {}".format(outputs_test))
	for x in outputs_test:
		for y in range(x + 1, length_test - 1):
			print("outputs_test[x] is {}, outputs_test[y] is {}".format(outputs_test[x], outputs_test[y]))
			if outputs_test[x] == outputs_test[y]:
				print("match found at index x =", x)
				print("match value ", matched_frequencies_test.append(outputs_test[x]))
	#print(len(matched_frequencies))

inputs, inputs_test	= get_input()
outputs, outputs_test, length, length_test  = get_output(inputs, inputs_test)
comparator(outputs, outputs_test, length, length_test)
