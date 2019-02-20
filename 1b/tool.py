#!/usr/bin/python3
def main():
	run_program()

def run_program():
		get_output(get_input())

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
		outputs.append(s) #create list of output frequencies
	length = len(outputs)
	print('Working with {} output values'.format(length))
	
if __name__ == "__main__": main()