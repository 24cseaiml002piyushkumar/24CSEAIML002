sentence = input("Enter a sentence: ")
LIST1 = sentence.split()
print("Elements of LIST1 with indices:")
for index, word in enumerate(LIST1):
    print(f"{index}: {word}")
LIST2 = list(range(1, len(LIST1) + 1))
LIST3 = list(zip(LIST1, LIST2))
print("LIST3 (zipped LIST1 and LIST2):")
print(LIST3)