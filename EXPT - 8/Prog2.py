def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter the number:"))
result = check(num)
print(f"The number {num} is {result}")