import random
from colorama import Fore, Back, Style

# Define the GamePlay Class
class GamePlay:
    def loadDictionary(self, file_path):
        # Implementation of loading the dictionary from a file

    def checkGuess(self, guess, secret_word):
        # Implementation of checking the guess

    def chooseWord(self, words_list):
        # Implementation of choosing a secret word

    def getInput(self):
        # Implementation of getting user input

    def printErrorMessage(self):
        # Implementation of printing an error message

    def printResult(self, result):
        # Implementation of printing the guess result

    def printWinMessage(self):
        # Implementation of printing the winning message

    def printLostMessage(self, secret_word):
        # Implementation of printing the losing message
    
    def validGuess(self, guess, words_list):
        # Implementation of validating the guess

# Function to run the game
def main():
    game = GamePlay()
    words_list = game.loadDictionary("wordle.txt")
    secret_word = game.chooseWord(words_list)
    attempts = 6
    
    while attempts > 0:
        guess = game.getInput()
        if not game.validGuess(guess, words_list):
            game.printErrorMessage()
            continue
        
        if guess == secret_word:
            game.printWinMessage()
            break
        
        result = game.checkGuess(guess, secret_word)
        game.printResult(result)
        attempts -= 1
    
    if attempts == 0:
        game.printLostMessage(secret_word)

# Run the game
if __name__ == "__main__":
    main()
