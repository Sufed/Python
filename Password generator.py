import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    char_sets = []
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    all_chars = ''.join(char_sets)
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    print("Password Generator")
    length = get_int_input("Enter password length: ")
    while True:
        use_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
        use_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
        use_digits = get_yes_no_input("Include digits? (y/n): ")
        use_symbols = get_yes_no_input("Include symbols? (y/n): ")

        try:
            pwd = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
            print("Generated password:", pwd)
            break
        except ValueError as e:
            print(e)
            print("Please select at least one character type.")