import random
correct = False
word_list = ["banana", "apple", "strawberry", "pineapple", "plum"]

word = random.choice(word_list)
while not correct:
    guess = input("Guess a letter. ")
    if len(guess) == 1:
        if guess.isalpha():
            print("Good guess")
            correct = True
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        
if guess in word:
    print("Good guess! '" + guess + "' is in the word.")
else:
    print("Sorry, " + guess + "is not in the word. Try again.")
    
