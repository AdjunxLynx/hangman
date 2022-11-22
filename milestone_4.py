import random
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        for i in range(len(self.word)):
            self.word_guessed.append("_")
        self.num_letters = 0
        self.num_lives = num_lives
        self.word_list = word_list

        self.list_of_guesses = []


        print(self.word_guessed)
h = Hangman(["asjs", "sdfhsdvuads"])