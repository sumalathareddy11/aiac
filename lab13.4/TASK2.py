words = ["AI", "helps", "in", "refactoring", "code"]

# Inefficient approach using += (avoid this)
sentence = ""
for word in words:
    sentence += word + " "
print(sentence.strip())

# Efficient approach using join() function
sentence = " ".join(words)
print(sentence)
