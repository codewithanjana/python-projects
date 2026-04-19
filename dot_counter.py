text = input("Enter a sentence: ")

count = 0
for char in text:
    if char == '.':
        count += 1

print("Number of dots:", count)
