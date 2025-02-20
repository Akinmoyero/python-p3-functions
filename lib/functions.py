def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, (int, float)):  # Ensure input is a number
        return number / 2
    return None  # Handle cases where input is not a number
