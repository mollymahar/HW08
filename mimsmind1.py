#!/usr/bin/env python
"""This is the bulls and crows version. It defaults to 3 digits."""

# import
import random
import sys

# body
def comp_guess(dig):
	"""This function takes an integer input and returns a random integer with that 
	number of displayed digits, broken into a list of single integer digits."""
	# convert number of digits to a proper range, then find a random number within that.
	# e.g. 2 digits is 00 - 99, or 0 to (10^2)-1
	# e.g. 3 digits is 000 - 999, or 0 to (10^3)-1
	# so the pattern is: 0 to (10^digits)-1
	# this formats the random number so that it has leading zeroes if necessary:
	comp_answer = "{0:0>{width}}".format(random.randint(0,(10**dig)-1), width = dig)
	# return as a list for easier comparison
	comp_answer_list = [int(i) for i in str(comp_answer)]
	return comp_answer_list

def set_max_rounds(dig):
	# ex: if digits is 3, max rounds is 11
	return (2**dig) + dig

def set_digits():
	"""I take an input (or not) and return an integer."""
	try:
		digs = int(sys.argv[1]) 		# make sure sys.argv is valid integer
	except:
		digs = 3 						# if not (or nothing entered), set to 3
	return digs

def find_bulls(dig, guess, answer):
	"""I take three arguments and return an integer."""
	bulls = 0
	for x in range(0, dig):
		if guess[x] == answer[x]:
			bulls += 1
	return bulls

def find_cows(dig, guess, answer):
	"""I take three arguments and return an integer."""
	cows = 0
	for x in range(0, dig):
		if guess[x] in answer and guess[x] != answer[x]:
			cows += 1
	return cows
	# this doesn't solve case of when guess has multiple instances of a single number that is in answer


def play_game():
	digits = set_digits()
	answer = comp_guess(digits) 	# set the correct/computer answer, as list
	maxrounds = set_max_rounds(digits)
	print "\nLet's play the mimsmind1 game. You have %d guesses." % maxrounds
	print "computer's answer =", answer
	guess = raw_input("Guess a %r-digit number: " % digits)
	count = 0
	
	while count < maxrounds:
		# format guess as a list for easy comparison with the computer's number
		try:
			guess_list = [int(i) for i in guess]
		except:
			guess = raw_input("\nInvalid input. Try again: ")
			continue
		count += 1
		
		if guess_list == answer:
			print "\nCongratulations! You guessed the correct number in %d round(s)." % count,
			break
		elif count == maxrounds:
			print "Sorry. You did not guess the number in %d rounds. The correct number was %s." % (count, ''.join(str(x) for x in answer))
		else:
			# look for bulls
			print "\n", find_bulls(digits, guess_list, answer), " bull(s)," , 
			# look for cows
			print find_cows(digits, guess_list, answer), "cow(s).",
			# take another guess
			guess = raw_input("Try again: ")
	


# call main()
def main():
	play_game()

if __name__ == '__main__':
		main()
