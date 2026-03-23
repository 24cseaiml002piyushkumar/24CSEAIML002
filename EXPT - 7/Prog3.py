paragraph = input("Enter a paragraph:")
words = paragraph.split()
word_count = len(words)
print(f"Number of words: {word_count}")
palindrome_count = 0
for word in words:
    if word.lower() == word.lower()[::-1]:
        palindrome_count += 1
print(f"Number of palindrome words: {palindrome_count}")
print("Each word in reverse order:")
for word in words:
    print(word[::-1])