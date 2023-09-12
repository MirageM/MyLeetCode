import random

def generate_random_numbers(n):
    # Initialize a list to store the random numbers
    random_numbers = []

    # Generate n random numbers and add them to the list
    for _ in range(n):
        random_numbers.append(random.randint(1, 10))  # Adjust the range as needed

    return random_numbers

# Generate 100 random numbers
random_numbers = generate_random_numbers(100)

# Count how many times the number 5 occurs
count_of_5 = random_numbers.count(5)

print(f"The number 5 occurs {count_of_5} times in the generated random numbers.")