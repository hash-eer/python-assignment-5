# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...

# Write a python code to read the file and store the words in the list
# Write a function to guess a word randomly from the list.
# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter.
# Display letters in the clue word that were guessed correctly.
# Let say word is EVAPORATE
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.

# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.


import random

startgame=100
while startgame!=1:
    my_file = open("file1.txt", "r")
    

    data = my_file.read()
    

    list = data.split("\n")
    print(list)
    my_file.close()

    word=random.choice(list)
    print(word)
    tries=6
    display='_'*len(word)

    game_over = False

    while not game_over:
        print("you have"+str(tries)+"tries remaining")
        print(display)
        guess=input("enter the guess letter:")
        
        i=0
        if guess in word:
            while word.find(guess,i)!= -1: # this is will serach the letter after i if it reaches end it will return -1
                i=word.find(guess,i)
                display=display[:i]+guess+display[i+1:]
                i+=1
            print("correct superb Guess you are a genious!:")
        else:
            print("sorry wrong guesss try again")
            tries-=1 #decrementing the tries if false
        if word == display: # checking the word is equal to display
            print("Horray1 you have won the game , the word was"+word)
            startgame=int(input("enter 1 to stop the game and 5 to start the game once again:"))
            game_over=True
                
        if tries==0:
            print("sorry you are out of your tries")
            startgame=int(input("enter 1 to stop the game and 5 to start the game once again:"))
            game_over=True
        
        
    

        
        
        
    





