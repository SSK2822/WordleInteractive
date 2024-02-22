import random
from colorama import Fore, Back, Style

# Define the GamePlay Class
class GamePlay:
    def loadDictionary(self, file_path):
        # Implementation of loading the dictionary from a file
        with open(file_path, 'r') as file:
            return [word.strip().lower() for word in file.readlines() if len(word.strip()) == 5]

    def checkGuess(self, guess, secret_word):
        # Implementation of checking the guess
        result = ['_'] * 5
        for i, letter in enumerate(guess):
            if letter == secret_word[i]:
                result[i] = Back.GREEN + letter + Back.RESET
            elif letter in secret_word:
                result[i] = Back.YELLOW + letter + Back.RESET
            else:
                result[i] = Back.RED + letter + Back.RESET
        return result

    def chooseWord(self, words_list):
        # Implementation of choosing a secret word
        return random.choice(words_list)

    def getInput(self):
        # Implementation of getting user input
        return input("Enter your guess: ").strip().lower()

    def printErrorMessage(self, guess):
        # Implementation of printing an error message
        if len(guess) != 5:
            print(Fore.RED + "Invalid word! Please enter a 5-letter word." + Fore.RESET)
        else:
            print(Fore.RED + "Invalid word! Please enter a valid word from the dictionary." + Fore.RESET)

    def printWinMessage(self):
        # Implementation of printing the winning message
        print(Fore.GREEN + "Congratulations! You found it!!!" + Fore.RESET)

    def printLostMessage(self, secret_word):
        # Implementation of printing the losing message
        print(Fore.RED + f"Better luck next time! The word was {secret_word}" + Fore.RESET)
    
    def printResult(self, result):
        # Implementation of printing the guess result
        print("".join(result))
    
    def validGuess(self, guess, words_list):
        # Implementation of validating the guess
        return guess in words_list

# Function to run the game
def main():
    game = GamePlay()
    words_list = game.loadDictionary("wordle.txt")
    secret_word = game.chooseWord(words_list)
    attempts = 6
    count = 1
    
    while attempts > 0:
        print(f"Attempt {count}/6")
        count+=1
        guess = game.getInput()
        if not game.validGuess(guess, words_list):
            count-=1
            game.printErrorMessage(guess)
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
