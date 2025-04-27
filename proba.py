import random

# Generate 7 random numbers between 1 and 35
random_numbers = [random.randint(1, 35) for i in range(7)]

random_numbers.sort()
print(random_numbers)