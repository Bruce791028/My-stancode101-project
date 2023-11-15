"""
File: coin_flip_runs.py
Name: Bruce Cheng
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Make the coin flip game, flipping util appearing two times continuous flip and print it
	"""
	print("Let's flip the coin! ")
	runs = int(input('Number of runs: '))
	roll1 = r.randrange(1, 3)
	# random flip with number 1 and 2, representing H and T.
	string = str(roll1)
	run = 0
	is_in_the_row = False
	# switch to identify the consecutive flip as one time continuous happen.
	while True:
		roll2 = r.randrange(1, 3)
		string += str(roll2)
		if roll2 == roll1:
			if not is_in_the_row:
				run += 1
				is_in_the_row = True
		else:
			is_in_the_row = False
		roll1 = roll2
		if run == runs:
			break
	show = ''
	for i in range(len(string)):
		if string[i] == str(1):
			show += 'H'
		else:
			show += 'T'
	print(show)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
