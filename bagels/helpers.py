
def getSecretNum(number_of_digits)-> str:
	"""Return a number made up of NUM_DIGITS unique random digits"""
	import random
	numbers = list('0123456789')
	random.shuffle(numbers)

	secretNum = ''
	for i in range(number_of_digits):
		secretNum += numbers[i]
	
	return secretNum



def getClues(guess: str, secretNum: str) -> str:
	"""Returns a number with pico, fermi and bagel for clues for a guess and a secret number"""
	if guess == secretNum:
		return 'You got it!'
	
	clues = []

	for i in range(len(guess)):
		if(guess[i] == secretNum[i]):
			clues.append('Fermi')
		
		elif guess[i] in secretNum:
			clues.append('Pico')
	
	if(len(clues)==0):
		return 'Bagels'
	
	else:
		'''Giving out a sorted information to not give out any information'''

		clues.sort()
		return ' '.join(clues)

	
