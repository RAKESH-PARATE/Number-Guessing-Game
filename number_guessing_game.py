import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.\n")

    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Guess out of range! Please guess between 1 and 100.")
            continue

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number {secret_number} in {attempt} attempt(s).")
            break
        elif guess < secret_number:
            print("🔼 Too low! Try a higher number.")
        else:
            print("🔽 Too high! Try a lower number.")

    else:
        print(f"\n❌ Sorry, you've used all {max_attempts} attempts.")
        print(f"The correct number was: {secret_number}")

number_guessing_game()
