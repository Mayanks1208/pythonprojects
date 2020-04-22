import random

number =random.randint(1, 25)
chances = 0

print("Guess a number (between 1 and 25):")

while chances<5:
    guess=int(input("Enter your Guess : "))

    if guess == number:
        print("Congratulations You WON!")
        exit()

    elif guess<number:
        print("Your guess was to far")
    
    else:
        print("Your guess was too high")
    
    chances+=1
    print("Chances LEft : ",5-chances)

print("you Lose!! The Number is :", number)