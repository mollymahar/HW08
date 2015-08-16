#!/usr/bin/env python
"""This program generates a random integer and prompts the user for integer input guesses,
responding with feedback until the user guesses correctly. It also counts the number
of tries the user has made."""


# import
import random
import sys

# body
def comp_guess(dig):
	"""This function takes an integer input and returns a random number with that 
	number of digits."""
	# convert number of digits to a proper range, then find a random number within that.
	# e.g. 2 digits is 10 - 99, or 10^(2-1) to (10^2)-1
	# e.g. 3 digits is 100 - 999, or 10^(3-1) to (10^3)-1
	# so the pattern is: 10^(digits-1) to (10^digits)-1
	return random.randint(10**(dig-1),(10**dig)-1)


def play_game():
	print "\nLet's play the mimsmind0 game."
	# choose the number of digits for the answer
	try:
		digits = int(sys.argv[1]) 		# make sure sys.argv is valid integer
	except:
		digits = 1 						# if not (or nothing entered), set to 1
	answer = comp_guess(digits) 		# set the correct/computer answer

	count = 0
	# print "computer's answer =", answer
	guess = raw_input("\nGuess a %r-digit number: " % digits)
	while True:
		try:
			guess_int = int(guess) 		# turn their entry into an integer
		except:
			guess = raw_input("That is not an integer. Try again: ")
			continue 					# if it's not an int, give them a chance to fix it
		else:
			count += 1 					# count each try that is an integer
			if guess_int == answer:
				if count == 1:
					print "\nCongratulations. You guessed the correct number on your first try!\n\n"
				else:
					print "\nCongratulations. You guessed the correct number in %r tries.\n\n" % count
				break
			if answer > guess_int:
				if len(guess) < digits: 	# make sure they're within lower limit
					print "\nThat guess has less than %r digits." % digits,
				guess = raw_input("\nTry again. Guess a higher number: ")
			elif answer < guess_int:
				if len(guess) > digits: 	# make sure within upper limit
					print "\nThat guess has more than %r digits." % digits,
				guess = raw_input("\nTry again. Guess a lower number: ")
	


# call main()
def main():
	play_game()

if __name__ == '__main__':
		main()
