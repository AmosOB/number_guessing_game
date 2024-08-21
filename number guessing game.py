import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            # Prompt the user to enter a guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Start the game
number_guessing_game()
