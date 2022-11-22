
# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


This is a text based Hangman Game built as a project for the AICore course. I have used VScode, python, git, github and terminal. within python, I have used the module random so the word to guess is not always the same, or so that the order of the words is not predictable.

the terminal cmds I have used for this is your basic ``` git add .``` ```git commit -m "" ``` and ```git push ``` so I can have a secure and good version control locally and online.


I have now introduced functions into my code and copied the existing code I had into them. this allows me to keep my variables separate (private) and not accidentally use the incorrect variables later on in my code. automatically calls the functions when the code is run.

I created a class and within that class initialised the variables needed once the class starts up. this means that I can avoid errors like trying to access a variable that doesn't exist yet. I added my previous functions as methods of this class.
I used a few if and ```elifs ``` to detect and make sure my input guess was clean, basically so I knew exactly what type of datatype I was working with.
I also used it to ensure I was enforcing the rules correctly

finally, I have placed all my code into a class and added the final function to control the logic of the game. I also use a few checks, such as if the user has used all guesses, if the user has guessed all letters.
I placed the play_game function outside the class, so it could be imported as a module of a hangman game for others to quickly access
the class also means I can technically have multiple hangmen game instances all at once, which is a good use of multitasking since I don't have to quit the current for a new game

for the logic, I needed to make sure the user hadn't used all of their guesses. I also had to make sure that all the letters hadn't been guessed.
finally, I needed to make sure the user didn't accidentally input the same letter after it was already inputted (even if it was correct) as that would be a waste of a turn
