import random
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        for i in range(len(self.word)):
            self.word_guessed.append("_")
        temp = set(self.word)
        self.num_letters = len(temp)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = str(guess)
            self.num_letters -= 1
            print("Good guess! " + guess + " is in the word.")
        elif guess not in self.word.lower():
            print("Sorry, " + guess + " is not in the word.")
            self.num_lives -= 1
            print("You have " + str(self.num_lives) + " left")
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter. ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break



h = Hangman(["asjs", "sdfhsdvuads"])
h.check_guess("x")