# Step 1: Define Overall Rules of the Wordle Game
# The game selects a secret word at random from a provided dictionary file ('wordle.txt')
# The selected word will always be five letters long
# The player has six attempts to guess the correct word

# The game flow is as follows:
# 1. Load the list of possible words from 'wordle.txt'
# 2. Randomly select one word from the list as the secret word
# 3. Prompt the player to enter a guess
#     - The guess must be exactly five letters long
#     - The guess must be a valid word from the list
# 4. If the guess is invalid (not in the list or not five letters), prompt again without penalty
# 5. Compare the guess to the secret word and give feedback for each letter
#     - If a letter is correct and in the correct position, indicate with a green background
#     - If a letter is correct but in the wrong position, indicate with a yellow background
#     - If a letter is incorrect, indicate with a grey background
# 6. If the guess is correct, display a winning message
# 7. If the guess is incorrect, display the number of attempts remaining and prompt for another guess
# 8. If the player runs out of attempts, display a losing message along with the secret word

