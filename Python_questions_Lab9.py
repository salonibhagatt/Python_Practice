# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2
result = div(10, 5)
print("The result of division is:", result)

# Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(number):
    return number * number
result = square(3)
print("The square of 3 is:", result)

# Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
maximum_number = max(random_numbers)
minimum_number = min(random_numbers)
print("Random Numbers:", random_numbers)
print("Maximum Number:", maximum_number)
print("Minimum Number:", minimum_number)

# Accept a name from the user and display that in lower case using lower() function
user_name = input("Please enter your name: ")
lower_case_name = user_name.lower()
print("Your name in lower case is:", lower_case_name)
