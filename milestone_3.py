import random
word_list = ["banana", "apple", "strawberry", "pineapple", "plum"]
word = random.choice(word_list)



def check_guess(guess):
    guess = guess.lower()
    correct = False
    while True:
        if guess in word:
            print("Good guess! '" + guess + "' is in the word.")
            break
        else:
            print("Sorry, " + guess + "is not in the word. Try again.")

def ask_for_input():
    valid = False
    guess = input("Guess a letter. ")

    while True:
        if len(guess) == 1:
            if guess.isalpha():
                print("Good guess")
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)
    
ask_for_input()
