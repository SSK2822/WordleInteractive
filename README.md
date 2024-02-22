# WordleInteractive

# Wordle Game Instructions

## Define Overall Rules of the Wordle Game

- The game selects a secret word at random from a provided dictionary file (`wordle.txt`).
- The selected word will always be five letters long.
- The player has six attempts to guess the correct word.

## Game Flow

1. **Load the Dictionary:**

   - Load the list of possible words from `wordle.txt`.

2. **Choose Secret Word:**

   - Randomly select one word from the list as the secret word.

3. **User Guess:**

   - Prompt the player to enter a guess.
   - The guess must be exactly five letters long.
   - The guess must be a valid word from the list.

4. **Validate Guess:**

   - If the guess is invalid (not in the list or not five letters), prompt again without penalty.

5. **Feedback:**

   - Compare the guess to the secret word and give feedback for each letter.
   - Indicate with a green background if a letter is correct and in the correct position.
   - Indicate with a yellow background if a letter is correct but in the wrong position.
   - Indicate with a grey background if a letter is incorrect.

6. **Winning Condition:**

   - If the guess is correct, display a winning message.

7. **Continuing the Game:**

   - If the guess is incorrect, display the number of attempts remaining and prompt for another guess.

8. **Losing Condition:**
   - If the player runs out of attempts, display a losing message along with the secret word.
