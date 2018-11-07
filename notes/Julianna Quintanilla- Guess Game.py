import random
a = (random.randint(0,10))
win = False
loop = 5

while loop > 0 and not win:
    guessed_number = int(input("Guess a number between 0 and 10 "))
    if guessed_number > a:
        print("Guess lower")
        loop -= 1
    elif guessed_number < a:
        print("Guess higher")
        loop -= 1
    elif guessed_number == a:
        print("You win, you guessed correctly.")
        win = True

