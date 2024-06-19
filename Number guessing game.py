import random

def get_random_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 50)
    elif level == 3:
        return random.randint(1, 100)

def get_max_attempts(level):
    if level == 1:
        return 5
    elif level == 2:
        return 7
    elif level == 3:
        return 10

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        try:
            level = int(input("Enter the level (1, 2, or 3): "))
            if level not in [1, 2, 3]:
                print("Please enter a valid level (1, 2, or 3).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

    random_number = get_random_number(level)
    max_attempts = get_max_attempts(level)
    attempts = 0

    print(f"Guess the number between 1 and {get_random_number(level)}.")
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
            if guess < 1 or guess > get_random_number(level):
                print(f"Please guess a number within the range 1 to {get_random_number(level)}.")
                continue
            attempts += 1
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts and guess != random_number:
        print(f"Sorry, you've used all your attempts. The number was {random_number}.")

if __name__ == "__main__":
    play_game()
