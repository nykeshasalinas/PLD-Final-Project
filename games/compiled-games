def guessTheNumber():
    import random

    print("\nWelcome to the Random Number Guessing Game!")

    print("\nChoose Mode")
    print("1. Easy (5 attempts)")
    print("2. Difficult (7 attempts)")
    print("3. Impossible (10 attempts)\n")

    # Get mode
    while True:
        try:
            mode = int(input("Enter the mode number (1, 2, or 3):"))
            if mode in [1, 2, 3]:
                break
            else:
                print("\nInvalid mode. Please enter 1, 2, or 3.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    # Generate number and attempts
    if mode == 1:
        secret_number = random.randint(1, 100)
        attempts_left = 5
        print("You selected Easy mode. Guess a number between 1 and 100.\n")
    elif mode == 2:
        secret_number = random.randint(1, 1000)
        attempts_left = 7
        print("You selected Difficult mode. Guess a number between 1 and 1000.\n")
    else:
        secret_number = random.randint(1, 10000)
        attempts_left = 10
        print("You selected Impossible mode. Guess a number between 1 and 10000.\n")

    # Guessing loop
    while attempts_left > 0:
        try:
            print(f"Attempts left: {attempts_left}")
            guess = int(input("Enter your guess: "))
            attempts_left -= 1
            if guess < secret_number:
                print("\nToo low! Try again.")
            elif guess > secret_number:
                print("\nToo high! Try again.")
            else:
                print(f"\nCongratulations! You've guessed the number {secret_number}!")
                break
        except ValueError:
            print("\nPlease enter a valid number.\n")

    # Pag talo
    if attempts_left == 0:
        print("\nGame Over! You've run out of attempts.")
        print(f"The secret number was {secret_number}.")


def hangman():
    print("Hinahanap pa si porman, bukas ka nalang bumalik")

def aboutTheDevs():
    print(" Dito yung information, sa susunod ko na gawin hahahaha. fuck.")
