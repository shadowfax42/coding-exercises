"""
Project: Hangman game
Author: Siham Elmali
Date: December 2020

"""
import random


def load_words(file):
	"""
	:param file: input file with bunch of words
	:return: return a list of words
	"""
	with open(file, "r") as f:
		print("Loading word list from file...")
		words_list = f.read().split()
		print(f"There are {len(words_list)} words in the file")
		return words_list


def choose_word(words_list):
	"""
	:param words_list: a list of words
	:return: a random word from the list
	"""
	chosen_word = random.choice(words_list)
	return chosen_word


if __name__ == '__main__':
	# input file with words to use
	file_name = "words.txt"
	words = load_words(file_name)
	print(choose_word(words))
