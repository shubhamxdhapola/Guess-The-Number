import random

#defining function
def Number_Guessing_Game():

    print("\n\n-------------WELCOME TO THE NUMBER GUESSING GAME-------------\n")
    print("How to play? : \n-The system will generate a random number between the range you specified. You will have to guess that number!\n")
   
    startingRange = int(input(">> Enter starting range : "))
    enidingRange = int(input(">> Enter ending range : "))

    randomNumber = random.randint(startingRange,enidingRange)
    
    attempts = 10
    countAttempts = 1
    
    
    print(f"\n>> Guess the number between {startingRange} to {enidingRange} (You have only 10 attempts)\n")
    
    
    while attempts > 0:
    
        print("_________________________________________________")
         
        userInput = int(input("\n>> Guess the number : "))
        
        if userInput == randomNumber: 
            print(">> Congrats! You guessed the correct number\n")
            break
    
        elif userInput > randomNumber:
            print(">> oops! You guessed the greater number")
            attempts = attempts - 1
            if(attempts==0):
                continue
            print("_________________________________________________\n")
            print(">> Only",attempts,"attempts left")
            countAttempts +=1
    
        else:
            print(">> oops! You guessed the smaller number")
            attempts = attempts - 1
            if(attempts==0):
                continue
            print("_________________________________________________\n")
            print(">> Only",attempts,"attempts left")
            countAttempts +=1
    
    if attempts == 0:
        
        print("_________________________________________________\n")
        print(">> Game Over!!(You are out of attempts)")
        print(">> Correct number was :",randomNumber,"\n")
        print("---------------------Game End---------------------\n")
    
    
    else:
    
        print("_________________________________________________\n")
        print(">> You guessed the correct number",countAttempts,"Attempts")    
        print(">> Score : ",(attempts),"/10",sep="")
        print(">> Accuracy : ",(attempts),"0%\n",sep="")
        print("---------------------Game End---------------------\n")

    playAgain = (input("\nDo you want to play again? Y/N: "))

    if(playAgain == 'Y' or playAgain == 'y'):
        Number_Guessing_Game()
    
    else:
        print("_________________________________________________\n")
        print("Exiting the game...........!!")
        print("_________________________________________________\n")

Number_Guessing_Game()