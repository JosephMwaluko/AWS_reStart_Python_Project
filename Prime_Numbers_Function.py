# Python script to display and store prime numbers between 1 and 250.
# I started by defining a function to check if a number is prime.

def primeNumbersCheck(num):

  # Generally, a number is prime if it is greater than 1 and has no other factors except 1 and itself.
  # The following if-else statement nested with a for loop was used to define the prime numbers characteristics and factors. 
  if num > 1:
    # Check for factors from 2 up to the square root of the number.
    for i in range(2, int(num**0.5) + 1):
      # If the number is divisible by any factor, it is not prime.
      if num % i == 0:
        return False
    # If no factor is found, the number is prime.
    return True
  # If the number is 1 or less, it is not prime.
  else:
    return False

# Create an empty list to store the prime numbers. The empty list will be a place holder.
# A placeholder is a symbol or a string that represents a value that is not known yet or that can vary depending on the context.
primes = []

# Loop through the numbers from 1 to 250.
# We are looping to 251 in the beacket so that 250 is part of the for loop executed by the code.
for num in range(1, 251):
  # If the number is prime, add it to the list.
  if primeNumbersCheck(num):
    primes.append(num)

# Display the prime numbers.
print("The Prime Numbers Between 1-250 are:\n")
print(*primes, sep=", ")

# After displaying the prime numbers for verification, they have to be store the results in a results.txt file.
# Open a file named results.txt in write mode.
primesList = open("results.txt", "w")

# Write the prime numbers to the file, separated by commas.
primesList.write(", ".join(map(str, primes)))

# Close the file.
primesList.close()

# Test the script and verify the results; Open the file named results.txt in read mode.
primesList = open("results.txt", "r")

# Read the contents of the file.
contents = primesList.read()

# Split the contents by commas and convert to integers.
numbers = list(map(int, contents.split(", ")))

# Check if the numbers are the same as the primes list.
if numbers == primes:
  print("Successful Script Execution: Results in the 'results.txt' file are as expected.")
else:
  print("Unsuccessful Script Execution: Results in the 'results.txt' file are not as expected.")

# Close the file
primesList.close()

