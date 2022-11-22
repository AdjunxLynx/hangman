import random

word_list = ["banana", "apple", "strawberry", "pineapple", "plum"]

word = random.choice(word_list)
print(word)
print(word_list)
guess = input("Guess a letter")
print(guess)

if len(guess) == 1:
    if guess.isalpha():
        print("Good guess")

else:
    print("Oops! That is not a valid input.")

for i in range(100):
    print(i)