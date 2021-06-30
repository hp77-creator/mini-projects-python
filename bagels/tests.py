from src.helpers import getClues
import unittest

class Tests(unittest.TestCase):

	def test_getClues_when_both_equal(self):
		"""
		Testing getClues function
		"""
		guess = '210'
		secretNum = '210'
		self.assertEqual(getClues(guess, secretNum), 'You got it!')

	def test_getClues_for_fermi(self):
		"""
		Testing if the clue given out is correct or not
		i.e when two digits match then clue should be 'Fermi Fermi'
		"""
		guess = '123'
		secretNum = '120'
		self.assertEqual(getClues(guess, secretNum), 'Fermi Fermi')
	
	def test_getClues_for_pico(self):
		"""
		Testing if the clue given out is correct or not
		i.e when digits match but they are not in the right place then clue should be 'Pico'
		"""
		guess = '321'
		secretNum = '213'
		self.assertEqual(getClues(guess, secretNum), 'Pico Pico Pico')

	def test_getClues_for_fermi_pico(self):
		"""
		Testing when one digit is at right place while other is not then the clue
		given should be 'Fermi Pico'
		"""
		guess = '678'
		secretNum = '687'
		self.assertEqual(getClues(guess, secretNum), 'Fermi Pico Pico')

		


if __name__=='__main__':
	unittest.main()