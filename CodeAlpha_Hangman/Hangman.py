import random

# Predefined word list
words = ["python", "apple", "table", "chair", "phone"]

# Choose random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_guesses:
    display_word = ""

    # Show guessed letters and blanks
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    # Check win condition
    if "_" not in display_word:
        print(" You won! The word was:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in word:
        print(" Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", max_guesses - wrong_guesses)

# Lose condition
if wrong_guesses == max_guesses:
    print("\n You lost! The word was:", word)
