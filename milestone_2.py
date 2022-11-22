import random
word = random.choice(word_list)
print(word)
word_list = ["banana", "apple", "strawberry", "pineapple", "plum"]
print(word_list)
guess = input("Guess a letter")
print(guess)

if len(guess) == 1:
    if guess.isalpha():
        print("Good guess")

else:
    print("Oops! That is not a valid input.")