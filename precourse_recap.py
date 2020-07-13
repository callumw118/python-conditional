solved = False

while solved == False:
    guess = input("Guess the number between 0-10: ")

    if int(guess) == 4:
        print("You have guessed the correct number")
        solved = True
    elif int(guess) == 3 or int(guess) == 5:
        print("So close, you were one number off")

    else:
        print("Sorry wrong number")