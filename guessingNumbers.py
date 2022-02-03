import random
print("Number guessing game!")
#randint function to generate random numbers between 1 to 9
number = random.randint(1,9)
#NUMBER OF CHANCES TO BE GIVEN TO USER TO GUESS THE NUMBER 
chances = 0 
print("Guess a number (between 1 and 9):")
#WHILE LOOP TO COUNT THE NO. OF CHANCES 
while chances < 5:
    guess = int(input("Enter your guess:- "))
#compare the  number to be guessed
    if guess == number:
        # user entery= generated number
        print("Congrats! You Won!")
        break
    #user entry > generated no
    elif guess<number:
        print("Your guess was too low: Guess a number higher than", guess)
    #user entry< no
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    #chances + 1
    chances += 1
#check wether the user 
if not chances < 5: 
    print("You lose, the number is: " , number)