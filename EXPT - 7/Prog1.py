m = int(input("Enter the starting number m: "))
n = int(input("Enter the ending number n: "))
numbers = []
for i in range(m, n + 1):
    numbers.append(i)
if numbers:
    total_sum = 0
    for num in numbers:
        total_sum += num
    average = total_sum / len(numbers)
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
else:
    print("No numbers in the range.")
filtered_list = []
for num in numbers:
    if num % 3 != 0:
        filtered_list.append(num)
print(f"Filtered list (excluding multiples of 3): {filtered_list}")