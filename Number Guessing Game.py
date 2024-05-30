import random

def number_guessing_game():

    secret_number = random.randint(1, 50)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess it?")
    
    attempts = 0
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        
        if guess.lower() == 'q':
            print(f"The secret number was {secret_number}. Better luck next time!")
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
