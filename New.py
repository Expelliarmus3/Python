'''Create a Python program that removes even duplicate positive integer numbers(includes zero) from a list and prints 
the unique numbers in the order they first appeared.
The program should prompt the user to input a list of numbers, then process the list to remove duplicates 
and print the resulting list of unique numbers.
'''
user_input = input()
lst = list(map(int, user_input.split()))

seen = set()
unique_numbers = []

# Process the list to remove duplicates
for num in lst:
    if num not in seen:
        seen.add(num)
        if num % 2 != 0 or num == 0:
            unique_numbers.append(num)

# Print the resulting list of unique numbers
print(unique_numbers)

