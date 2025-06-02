import random

# ✅ Task 1: Hangman Game

# List of 5 predefined words
word_list = ["apple", "table", "house", "chair", "grape"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Create placeholders for the guessed word
guessed_word = ["_"] * len(chosen_word)

# Set of letters already guessed
guessed_letters = set()

# Max number of incorrect guesses
max_attempts = 6
attempts_left = max_attempts

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Main game loop
while attempts_left > 0 and "_" in guessed_word:
    print("\nWord: " + " ".join(guessed_word))
    print(f"Attempts left: {attempts_left}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game over! The word was:", chosen_word)
