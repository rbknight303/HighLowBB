"""Ask user to think of a number
between 1 and 100, attempt to guess number,
have user say whether answer is too low,
too high, or correct"""

#explain game to the user
print("Think of a number between 1 and 100 and I will attempt to guess it!")
print("If I guess it in 6 turns, I win. Otherwise, you win!")
print("Tell me if my guess is too low by typing 'l', too high by typing 'h', or correct by typing 'c'!")

#set bounds for game, set initial values of bounds
parameters = (0,100)
bottom, top = parameters

#import random number between 0 and 100 for the first guess
import random
guess = random.randint(0,100)
tries = 0
#initialize correct as False
correct = False

#if correct if False, follow this loop
while not correct and tries < 8:
    #tell user the guess
    print("I am going to guess {}." .format(guess))

    answer = str(input("too (h)igh, too (l)ow, or (c)orrect:"))

    #ask user about guess, create loop if answer is not one of three choices
    inputSuccessful = True
    while inputSuccessful:
        #answer = str(input("too (h)igh, too (l)ow, or (c)orrect:"))
        #if answer is of right type, initialize inputSuccessful as True, ending loop
        if answer.upper() in ["L", "H", "C"]:
            inputSuccessful = False

        #if answer is not of right type, specify what user must type
        else:
            answer = input("Please enter either 'l', 'h', or 'c':")

    #if answer is too low, set bottom bound as previous guess, generate new guess
    if answer == "l":
        bottom = guess
        #add top and bottom bounds and divide by two to get new guess
        guess = int((top + bottom) /2)
        tries += 1

    #if answer is too high, set top as previous guess
    elif answer == "h":
        top = guess
        #add top and bottom bounds and divide by 2
        guess = int((top + bottom) /2)
        tries += 1

    #if answer is correct, greet user
    elif answer == "c":
        print("Yay! I win! You lose!")
        #set correct to True to end the program
        correct = True

if tries >= 8:
    print("Congrats, you won this time.")





