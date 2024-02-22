# Step 2: Define the GamePlay Class
# Function to load the list of valid words from a file
# It should return a list of words
def loadDictionary(file_path):
    # Open the file at file_path
    # Read all lines in the file
    # Strip whitespace from each word
    # Ensure all words are converted to lowercase (for consistency)
    # Close the file
    # Return the list of words

# Function to choose a secret word at random from the list of valid words
def chooseWord(words_list):
    # Use the random library to select a word at random
    # Return the selected word

# Function to prompt the user to enter a guess
def getInput():
    # Prompt the user for input
    # Return the input

# Function to check if the user's guess is valid
def validGuess(guess, words_list):
    # Check if the guess is in the words_list and is 5 characters long
    # Return True if valid, False otherwise

# Function to print an error message if the guess is invalid
def printErrorMessage():
    # Print an appropriate message to the console

# Function to check the user's guess against the secret word
def checkGuess(guess, secret_word):
    # Create a result list with placeholders for correct letters and positions
    # Check each letter in the guess to see if it matches a letter in the secret word
    # If it matches and is in the correct position, mark it as correct (e.g., with a green background)
    # If it is in the word but in the wrong position, mark it as present (e.g., with a yellow background)
    # If it is not in the word, mark it as absent (e.g., with a gray background)
    # Return the result list

# Function to print the result of the guess
def printResult(result):
    # For each letter in the result, print it with the appropriate color coding
    # Use the colorama library to print letters with colored backgrounds

# Function to print a winning message
def printWinMessage():
    # Print a congratulatory message to the console

# Function to print a losing message with the secret word
def printLostMessage(secret_word):
    # Inform the user that they did not guess the word
    # Reveal the secret word to the user

# Function to run the game
def main():
    # Load the list of valid words from the file
    # Choose a secret word at random
    # Initialize the number of attempts remaining
    # While the player has attempts remaining
        # Prompt the user to enter a guess
        # If the guess is invalid
            # Print an error message
        # If the guess is correct
            # Print a winning message and end the game
        # If the guess is incorrect
            # Print the result of the guess
            # Decrement the number of attempts remaining
    # If the player runs out of attempts
        # Print a losing message with the secret word