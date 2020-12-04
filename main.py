n=18
guess=5
while(guess!=0):
    user = int(input("Ener the number "))
    if user>12 and user<19:
        print("you are too close increase your number")
        print(guess-1)
    elif user>19 and user<22:
        print("you are too close decrease your number")
        print(guess-1)    
    elif user>=22:
        print("your number is too big chose smaller number")
        print(guess-1)
    elif user<=12:
        print("your number is too small chose larger number")
        print(guess-1)
    if guess == 1:
        print("game over")
    guess -=1

