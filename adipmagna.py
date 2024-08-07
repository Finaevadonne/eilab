import random

def generate_logarithmic_string():
    length = int(10 ** random.uniform(0, 3))  # Generate a random length based on a logarithmic distribution
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))

# Generate 1000 strings and count the frequency of each length
length_counts = {}
for _ in range(1000):
    s = generate_logarithmic_string()
    length_counts[len(s)] = length_counts.get(len(s), 0) + 1

# Print the frequency of each length
for length, count in length_counts.items():
    print(f"Length {length}: {count} occurrences")
