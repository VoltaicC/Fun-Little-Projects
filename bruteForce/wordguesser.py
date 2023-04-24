import string
import itertools
import time

def guess_string(target_string):
    characters = string.ascii_letters + string.digits + string.punctuation + ' ' # Generate a string containing all possible characters
    max_length = len(target_string) # Set the maximum length of the guessed string to be the same as the target string
    for length in range(1, max_length+1): # Loop through all possible lengths of the guessed string
        for combination in itertools.product(characters, repeat=length): # Generate all possible combinations of characters for the current length
            guess = ''.join(combination) # Convert the combination of characters to a string
            if guess == target_string: # Check if the guess matches the target string
                return guess # Return the guess if it matches the target string

# Get input from user
target_string = input("Enter the target string: ")
start = time.time() # Start the timer

# Call the guess_string function
result = guess_string(target_string)

# Print the result
if result:
    print("String guessed:", result)
else:
    print("No matching string found.")

end = time.time() # Stop the timer
print("Time taken:", end-start, "seconds")
