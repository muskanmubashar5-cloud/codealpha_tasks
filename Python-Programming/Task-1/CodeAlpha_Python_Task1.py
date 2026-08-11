import random
print("Welcome to Hangman!")
words = ["python", "computer", "program", "keyboard", "internet"]
word = random.choice(words)  #Player chooses a random word
display = ["_"] * len(word)
incorrect_guesses = 0
while incorrect_guesses < 6:
    print("Word:", " ".join(display)) 

    guess = input("Guess a letter: ").lower()

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

    print("Incorrect guesses:", incorrect_guesses) 

    if "_" not in display: 
        print("Congratulations! You guessed the word!")
        break

if incorrect_guesses == 6:
    print("Game over!")
    print("The word was:", word)