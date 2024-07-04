import random

# Define a constant line for formatting
LINE = '=' 

# Function to get starting and ending range with error handling
def get_specified_range():
    
     while True:
        
        try:
            # Prompt the user to enter the starting and ending range
            starting_range = int(input("\n>> Enter starting range : "))
            ending_range = int(input(">> Enter ending range : "))
            return starting_range, ending_range
        
        except ValueError:
            # Handle invalid input
            print(">> Invalid input! Please enter a valid number.")
    
    
# Function to get user input with error handling
def get_user_input():
    
    while True:
        
        try:
            # Prompt the user to guess the number
            user_input = int(input("\n>> Guess the number: "))
            return user_input
        
        except ValueError:
            # Handle invalid input
            print(">> Invalid input! Please enter a valid number.")

# Function to play the guessing game
def play_game():
    
    # Generate a random number between user specified range
    starting_range, ending_range = get_specified_range()
    random_number = random.randint(starting_range, ending_range)
    
    # Set the number of attempts
    attempts = 10
    count_attempts = 1

    print(f"\n>> Guess the number between {starting_range} to {ending_range} (You have only 10 attempts)\n")

    while attempts > 0:
        
        print(LINE*48)
        
        # Get the user's guess
        user_input = get_user_input()

        # Check if the guess is correct
        if user_input == random_number:
            print(">> Congrats! You guessed the correct number\n")
            break
        
        # Check if the guess is too high
        elif user_input > random_number:
            print(">> Oops! You guessed a greater number")
        
        # Check if the guess is too low
        else:
            print(">> Oops! You guessed a smaller number")

        # Decrement attempts and increment the attempt count
        attempts -= 1
        count_attempts += 1

        # Print remaining attempts or game over message
        if attempts > 0:
            print(f"{LINE * 48}\n>> Only {attempts} attempts left")
            
        else:
            print(f"{LINE * 48}")
            print("\n>> Game Over!!(You are out of attempts)")
            print(f">> Correct number was : {random_number} \n")
            print(f"{LINE * 19} Game End {LINE * 19} \n")

    # If the user guessed the number within the attempts
    if attempts > 0:
        print(LINE * 48)
        print(f"\n>> You guessed the correct number in {count_attempts} attempts")
        print(f">> Score: {attempts}/10")
        print(f">> Accuracy: {attempts * 10}%\n")
        print(f"{LINE * 19} Game End {LINE * 19} \n")
       
    # If the user ran out of attempts        
    else:
        print(f">> Better luck next time!\n")


# Function to start the number guessing game
def number_guessing_game():
    
    print(f"\n{LINE * 20} WELCOME TO THE NUMBER GUESSING GAME {LINE * 20}")
    print("\nHow to play?\nThe system will generate a random number between the range you specified. You will have to guess that number!")

    while True:
        
        # Play the game
        play_game()
        
        # Ask if the user wants to play again
        play_again = input(">> Do you want to play again? (Y/N): ").strip().capitalize()
        if play_again != 'Y':
            break

    print(f"{LINE * 48}\n>> Exiting the game...\n{LINE * 48}")

# Main function to run the game
if __name__ == "__main__":
    
    number_guessing_game()
