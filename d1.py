# Variables and printing
name = "Emmanuel"
age = 20
print(f"My name is {name} and I am {age} years old")

# Function
def greet(user):
    return f"Welcome, {user}!"
print(greet(name))
print(f"Your age next year will be {age + 1}")

# List and loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for n in numbers:
    print(n * 2)

# Dictionary    
person = {"name": name, "age": age}
for key, value in person.items():
    print(f"{key}: {value}")    