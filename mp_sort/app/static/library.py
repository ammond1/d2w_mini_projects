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
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def sortnumber1():
	number_string = document.getElementById("generate").innerHTML

	#creates list of integers from string, removing the ',' and '.'
	array = [int(num) for num in number_string.split(',')]

	#calls bubble sort function
	sort_it(array)

	# '''	This function is used in Exercise 1.
	# 	The function is called when the sort button is clicked.

	# 	You need to do the following:
	# 	- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
	# 	- create a list of integers from the string of numbers
	# 	- call your sort function, either bubble sort or insertion sort
	# 	- create a string of the sorted numbers and store it in array_str
	# '''
	pass
	#creates string of sorted number
	array_str = string_it(array)
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return
	
	array = []
	string_holder = ''
	
	for i in range(len(value)):
		if value[i] == ',':
			array.append(int(string_holder))
			string_holder = ''
		else:
			string_holder = string_holder + value[i]
		
	if string_holder:
		array.append(int(string_holder))
	sort_it(array)
	array_str = string_it(array)

	document.getElementById("sorted").innerHTML = array_str

def sort_it(array):
	switch = True
	n = len(array)
	while switch == True:
		switch = False
		new_n = 0
		for i in range(0,n-2):
			inner_first = array[i]
			inner_second = array[i+1]
			if inner_first > inner_second:
				array[i] , array[i+1] = array[i+1] , array[i]
				switch = True
				new_n = i+1
	n = new_n
	return array

def string_it(array):
	array_str = ''
	
	for i in range(len(array)):
		if i == len(array)-1:
			end = '.'
		else:
			end = ', '
		array_str = array_str + str(array[i]) + end
	return array_str