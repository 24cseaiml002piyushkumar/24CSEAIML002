d = {}
n = int(input("Enter the number of key-value pairs:"))
for i in range(n):
    k = input(f"Enter key {(i+1)}:")
    v = input(f"Enter value {(i+1)}:")
    d[k] = v
rev = {}
for k, v in d.items():
    rev[v] = k
print("\n Original Dictionary:")
print(d)
print("\n Reversed Dictionary:")
print(rev)