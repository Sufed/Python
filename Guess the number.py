import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("Welcome to Guess the Number! I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.")
    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
if __name__ == "__main__":
    guess_the_number()