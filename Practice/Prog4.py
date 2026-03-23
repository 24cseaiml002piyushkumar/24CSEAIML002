l = []
n = int(input("Enter the number of terms to be entered:"))
for i in range(n):
    l.append(int(input(f"Enter {(i+1)}th terms:")))
res = sorted(list(set(l)))
print("After removing:",res)