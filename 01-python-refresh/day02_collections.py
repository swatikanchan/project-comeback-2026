
# list opertaions
fruits = ["apple", "banana", "orange", "grapes"]
print("Fruits:", fruits)

fruits.append("watermelon")
fruits.append("peach")
fruits.append("lytchee")
print("Fruits after appending:", fruits)

fruits.remove("banana")
print("Fruits after removing banana:", fruits)

fruits.sort()
print("Sorted: ",fruits)

fruits.reverse()
print("Reverse: ", fruits)

print("\n*****************************************************\n")

# ****************************************************
# dictionary operations
student = {
    "name": "Swati",
    "experience": 10,
    "target": "Senior AI Engineer"
}
print("Student:", student)

student["status"] = "preparaing for interview"
print("Student after adding status:", student)  

student["experience"] = 11
print("Student after updating experience:", student)

student.pop("level", "Key not found")
print("Student after removing level:", student)

for key, value in student.items():

    print(key, ":", value)

print("\n*****************************************************\n")

# ****************************************************
# set opreations
frontend = {"React","Angular","Vue", "Python"}
backend = {"Java","Python","Go"}

print("Frontend:", frontend)
print("Backend:", backend)

print("Union:", frontend.union(backend))
print("frontend", frontend)

print("Intersection:", frontend.intersection(backend))
print("frontend", frontend)

print("Difference:", frontend.difference(backend))
print("frontend", frontend)

print("\n*****************************************************\n")

# ****************************************************

# tuples operations
location = ("Bangalore", "Pune", "Chennai", "Hyderabad")
print("Location:", location)

location = location + ("Mumbai",)
print("Location after adding Mumbai:", location)

location = location[:2] + location[3:]
print("Location after removing Chennai:", location)

location = sorted(location)
print("Location after sorting:", location)

location = location[::-1]
print("Location after reversing:", location)

print("\n*****************************************************\n")

# ****************************************************

# list comprehension
numbers = list(range(1,101))

even_numbers = [num for num in numbers if num%2 == 0]
print("Even numbers:", even_numbers)

odd_numbers = [num for num in numbers if num%2 != 0]
print("Odd numbers:", odd_numbers)

squared_numbers = [num*num for num in numbers]
print("Squared numbers:", squared_numbers)

print("\n*****************************************************\n")

# ****************************************************

people = [
    {
        "name":"Alice",
        "age":20
    },
    {
        "name":"Bob",
        "age":35
    },
    {
        "name":"Charlie",
        "age":28
    }
]

for person in people:
    if person["age"] > 25:
        print("Name:", person["name"], ", Age:", person["age"])

[print("Name:", person["name"], ", Age:", person["age"]) for person in people if person["age"] > 25]

print("\n*****************************************************\n")

# ****************************************************

def summarize_numbers(numbers):
    numbers_summary = {}

    numbers_summary["count"] = len(numbers)
    numbers_summary["maximum"] = max(numbers)
    numbers_summary["minimum"] = min(numbers)
    numbers_summary["average"] = sum(numbers) / len(numbers) if numbers else 0
    return numbers_summary

summary = summarize_numbers(numbers)
print("Numbers Summary:", summary)

print("\n*****************************************************\n")

