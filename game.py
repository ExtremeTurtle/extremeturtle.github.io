import random

def display_win_screen():
    print("Congratulations! You guessed the number!")
    print("   __  __          __      __")
    print("  / / / /___  ____/ /___ _/ /_____  _____")
    print(" / / / / __ \/ __  / __ `/ __/ __ \/ ___/")
    print("/ /_/ / /_/ / /_/ / /_/ / /_/ /_/ / /")
    print("\____/ .___/\__,_/\__,_/\__/\____/_/")
    print("    /_/")

def display_lose_screen(secret_number):
    print("Sorry, you've run out of attempts.")
    print("The number I was thinking of was", secret_number)
    print("Better luck next time!")
    print("  ____                            ")
    print(" / ___| ___ _ __   ___  _ __ ___  ")
    print("| |  _ / _ \ '_ \ / _ \| '_ ` _ \ ")
    print("| |_| |  __/ | | | (_) | | | | | |")
    print(" \____|\___|_| |_|\___/|_| |_| |_|")

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = input("Enter your guess (between 1 and 100): ")
        
        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        
        # Check if the guess is within the valid range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            display_win_screen()
            return

    display_lose_screen(secret_number)

if __name__ == "__main__":
    main()