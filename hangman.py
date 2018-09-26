
import replit
import sys
import random
correctGuesses = []
incorrectGuesses = []
fullBody = 8

def play():
	correctWord = False
	playType = raw_input('One or two players? ')
	if playType == 'One' or playType == 'one' or playType == '1':
		secretWord = random.choice(dictionary)
	else:
		secretWord = raw_input('Enter a word to guess: ').lower()
	if secretWord.isalpha():
		clear()
		initialGuessDisplay(secretWord)
		while len(incorrectGuesses) < fullBody and correctWord != True:
			printBoard(incorrectGuesses)
			displayLetters()
			guessLetter(secretWord)
			correctWord = winChecker()
			clear()
		if len(incorrectGuesses) >= fullBody:
			printBoard(incorrectGuesses)
			print 'Good try! The word was', secretWord
		else:
			print 'Congratulations, you won! The word was', secretWord
	else:
		print 'This is not an acceptable word'
		wrongInput()

def printBoard(wrongList):
	if len(wrongList) == 0:
		print '+======+ \n|      |\n       |\n       |\n       |\n       |\n ======='
	if len(wrongList) == 1:
		print '+======+ \n|      |\nO      |\n       |\n       |\n       |\n ======='
	if len(wrongList) == 2:
		print '+======+ \n|      |\nO      |\n|      |\n       |\n       |\n ======='
	if len(wrongList) == 3:
		print ' +======+ \n |      |\n O      |\n/|      |\n        |\n        |\n  ======='
	if len(wrongList) == 4:
		print ' +======+ \n |      |\n O      |\n/|\     |\n        |\n        |\n  ======='
	if len(wrongList) == 5:
		print ' +======+ \n |      |\n O      |\n/|\     |\n  \     |\n        |\n  ======='
	if len(wrongList) == 6:
		print ' +======+ \n |      |\n O      |\n/|\     |\n/ \     |\n        |\n  ======='
	if len(wrongList) == 7:
		print '  +======+ \n  |      |\n  O      |\n /|\     |\n./ \     |\n         |\n   =======' 
	if len(wrongList) == 8:
		print '  +======+ \n  |      |\n  O      |\n /|\     |\n./ \.    |\n         |\n   ======='
	#In order to give the user more guesses, I added little "feet" to increase the body parts drawn
	
def displayLetters():
	for j in correctGuesses:
		print j,
	print '\n'
	print 'Wrong letters guessed: '
	for k in incorrectGuesses:
		print k,
	print '\n'

def guessLetter(word):
	letter = raw_input('Guess a letter: ').lower()
	if letter.isalpha() and len(letter) == 1 and letter not in correctGuesses:
		for l in range(0,len(word)):
			if word[l] == letter:
				correctGuesses[l] = letter
			elif letter not in word and letter not in incorrectGuesses:
				incorrectGuesses.append(letter)
	elif letter not in correctGuesses:
		print 'Invalid guess'
	else:
		print 'Letter already guessed'

			

def initialGuessDisplay(word):
	for i in range(0, len(word)):
		correctGuesses.append('_')
		
def winChecker():
	if '_' not in correctGuesses:
		return True


def clear():
	#use in not file mode
	replit.clear() #This is the Replit IDE function used to clear the terminal
	#print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
	#use this "clear" when using a different python compiler

def wrongInput():
	choice = raw_input('Play again? ')
	if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'Y':
		correctGuesses = []
		incorrectGuesses = []
		play();
	else:
		sys.exit()

#This dictionary is from the text file at http://www.instructables.com/id/Python-and-Word-Lists/. Since it is over 113000 words long, only a very small portion of the dictionary is shown
#To make the game better, all words 3 letters or less have been removed.
dictionary = ['aahed',
'aahing',
'aahs',
'aalii',
'aaliis',
'aals',
'aardvark',
'aardvarks',
'aardwolf',
'aardwolves',
'aasvogel',
'aasvogels',
'abaca',
'abacas',
'abaci',
'aback',
'abacus',
'abacuses',
'abaft',
'abaka',
'abakas',
'abalone',
'abalones',
'abamp',
'abampere',
'abamperes',
...]



