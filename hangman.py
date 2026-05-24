import random

# List of predefined words
words = ["python", "apple", "tiger", "house", "music"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display hidden word
display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct guess!")

        # Reveal the guessed letter in the word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Final result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)