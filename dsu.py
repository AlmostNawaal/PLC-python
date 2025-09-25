words = ["banana", "pie", "Washington", "book"]

# Decorate
decorated = [(len(word), word) for word in words]

# Sort
decorated.sort()

# Undecorate
result = [word for (length, word) in decorated]

print(result)
