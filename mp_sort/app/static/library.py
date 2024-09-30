from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	array = list(range(number))
	return array

def generate():
	number = 10
	seed = 200
	array = gen_random_int(number, seed)
	random.shuffle(array)
	array_str = string_it(array)

	# This line is to place the string into the HTML
	document.getElementById("generate").innerHTML = array_str

def sortnumber1():
	number_string = document.getElementById("generate").innerHTML

	#creates list of integers from string, removing the ',' and '.'
	array = [int(num.replace(' ','')) for num in number_string.split(',')]

	#calls bubble sort function
	sort_it(array)

	#calls string_it function to convert list into string
	array_str = string_it(array)
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return
	
	array = []
	string_holder = ''
	
	#alternate way to remove ',' from string and turn it into a list, using the ',' as a signal to append previous digits
	for i in range(len(value)):
		if value[i] == ',':
			array.append(int(string_holder))
			string_holder = ''
		else:
			string_holder = string_holder + value[i]
	#appends the last value into the list 
	if string_holder:
		array.append(int(string_holder))
	sort_it(array)
	array_str = string_it(array)

	document.getElementById("sorted").innerHTML = array_str

#bubble sort v4 function
def sort_it(array):
	switch = True
	n = len(array)
	while switch == True:
		switch = False
		new_n = 0
		for i in range(0,n):
			inner_first = array[i]
			inner_second = array[i+1]
			if inner_first > inner_second:
				array[i] , array[i+1] = array[i+1] , array[i]
				switch = True
				new_n = i
		n = new_n
	return array

#turns input array into a string with appropriate seperations and formatting 
def string_it(array):
	array_str = ''
	
	for i in range(len(array)):
		if i == len(array)-1:
			end = '.'
		else:
			end = ', '
		array_str = array_str + str(array[i]) + end
	return array_str