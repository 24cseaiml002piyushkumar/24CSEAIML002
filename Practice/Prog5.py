l = ['Apple','Banana','Mango']
print("Fruits displayed:")
for i in l[::-1]:
    print(i, "Length:",len(i))
print("\n List containing reverse:")
rev = []
for fruit in l:
    rev.append(fruit[::-1])
print(rev)