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


        print(self.word_guessed)

    def check_guess(self, guess):
        guess = guess.lower()
        correct = False
        while not correct:
            if guess in self.word:
                print("Good guess! " + guess + " is in the word.")
                correct = True
                for i in range(len(self.word)):
                    if guess == self.word[i]:
                        self.word_guessed[i] = str(guess)
                print(self.word_guessed)


            else:
                print("Sorry, " + guess + "is not in the word.")
                self.num_lives -= 1
                print("You have " + str(self.num_lives) + " left")
            self.list_of_guesses.append(guess)

    def ask_for_input(self):
        valid = False
        guess = input("Guess a letter. ")

        while not valid:
            if len(guess) == 1:
                if guess.isalpha():
                    print("Good guess")
                    valid = True
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

        self.check_guess(guess)



h = Hangman(["asjs", "sdfhsdvuads"])
h.check_guess("a")