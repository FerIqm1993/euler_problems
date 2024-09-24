'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum  of these multiples  is 23.
Find the sum  of all the multiples of 3 or 5 below 1000.
'''
# Set the limit of the calculation
limit = 1000
sum_numbers = 0  # Set a variable to store the sum of the multiples

for number in range(1, limit):
    if (number % 3 == 0) or (number % 5 == 0):
        sum_numbers += number  # Add the number to the sum if it is a multiple of 3 or 5

# Displaying the result of the sum
print(f'The sum of all the multiples of 3 or 5 below {limit} is: {sum_numbers}')

