import random
import string
import time



def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


# Example usage: Generate a random string of length 16
random_string = generate_random_string(10)
start_time = time.time()
num_tries = 0

while time.time() - start_time < 1:
    random_string1 = generate_random_string(10)
    num_tries += 1
    print(f"Code: {random_string1} and try {num_tries}")
    if random_string == random_string1:
        print(f"Match found after {num_tries} tries")
        exit()
    