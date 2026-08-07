# variables
name = "Swati"
years_of_experience = 10
career_goal = "Senior AI Software Engineer"

# list
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)


numbers.append(12)
print(numbers)

# dictionary
profile = {
    "name": "Swati",
    "experience": 10,
    "goal": "AI Engineer"
}
print(profile)

for key, value in profile.items():
    print(key, ":",value)

# functions

# calculate average of a list of numbers
def calculate_average(numbers):
    return sum(numbers)/len(numbers)

print("Average of numbers:", calculate_average(numbers))

# find even numbers in a list
def find_even_numbers(numbers):
    print("Finding even numbers in the list...")
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

print("Even numbers:", find_even_numbers(numbers))

# find odd numbers in a list
def find_odd_number(numbers):
    print("Finding odd numbers in the list:...")
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)

    return odd_numbers

print((find_odd_number(numbers)))

# find maximum number in a list
def find_maximum(numbers):
    print("Finding maximum number in the list:...")
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print("Maximum number:", find_maximum(numbers))


