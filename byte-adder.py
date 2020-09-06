# byte_adder.py
# A simple python program which simulates the behaviour of a digital circuit performing integer addition.
# It adds two 8 bit binary numbers using different logical gates.

import sys
import os

#defining input
def Input():
	upper_bit_int = int(input("Enter \'first integer\' from 0 to 255 : ")) # first input from the user
	lower_bit_int= int(input("Enter \'second integer\' from 0 to 255 : ")) # second input from the user
	return(upper_bit_int, lower_bit_int)

# defining and gate
def andGate(bitOne, bitTwo): 
	return bitOne & bitTwo

# defining or gate
def orGate(bitOne, bitTwo):     
	return bitOne | bitTwo

# defining not gate
def compliment(bitValue):
	return ~bitValue

# defining xor gate
def xorGate(bitOne, bitTwo):
	return orGate(andGate(bitOne, compliment(bitTwo)), andGate(compliment(bitOne), bitTwo))

# calculating carry
def calculateCarry(a, b, c, d):
	return orGate(andGate(a,b), andGate(c,d))

# performing bit operation
def bitOperation(upper_bit, lower_bit):
	result = []
	carry = 0
	for index in range(len(upper_bit)):
		after_xor_cal = xorGate(upper_bit[index], lower_bit[index])
		result.append(xorGate(after_xor_cal, carry))
		carry = calculateCarry(upper_bit[index], lower_bit[index], after_xor_cal, carry)
	result.append(carry)
	return list(reversed(result))

# Final processing and printing the sum
def Output():
	upper_bit_int, lower_bit_int = Input()
	if 255>=upper_bit_int>=0 and 255>=lower_bit_int>=0: #checking the input range min=0 and max=255
		print('calculating sum...')
	else :
		print('Error: Input is not in range')
		print('Restarting...')
		print()		
		del upper_bit_int 
		del lower_bit_int 
		Output()

	upper_bit = [int(x) for x in list('{:08b}'.format(upper_bit_int))]
	lower_bit = [int(x) for x in list('{:08b}'.format(lower_bit_int))]

  # output of bit operation
	result = bitOperation(list(reversed(upper_bit)), list(reversed(lower_bit)))
	final_sum_bin = ''.join(str(e) for e in result)
	final_sum_int = int(''.join(str(e) for e in result),2)
	print('Integer sum using bit operation = ', final_sum_int ,' In Binary = ',final_sum_bin)
	print()

  # loop for adding two integers again and again unless user exits
	quit = input("Do you want to add again Y/N : ")
	if quit.lower() == 'n':
		exit()
	elif quit.lower() == 'y':
		print()
		Output()

print('This is a python program which simulates the behaviour of a digital circuit performing integer addition.')
print()
Output()
		

			


