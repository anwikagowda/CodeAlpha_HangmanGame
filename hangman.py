import random

words = ["apple", "tiger", "house", "drone", "robot"]

word = random.choice(words)

display = []

for letter in word:
    display.append("_")

wrong_guesses = 0

while wrong_guesses < 6 and "_" in display:

    print("\nWord:", " ".join(display))

    guess = input("Enter a letter: ").lower()

    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:

        wrong_guesses += 1

        print("Wrong Guess!")
        print("Remaining Chances:", 6 - wrong_guesses)

if "_" not in display:
    print("\nCongratulations! You Won!")
else:
    print("\nGame Over!")
    print("The word was:", word)