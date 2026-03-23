l = ["Apple","Banana","Mango"]
print("Fruits displayed from last to first index with their length:")
for i in l[::-1]:
    print(i, "- Length:", len(i))
print("\n List containing reverse of each element:")
rev = []
for fruit in l:
    rev.append(fruit[::-1])
print(rev)