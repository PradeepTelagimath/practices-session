sentence = input()
position = int(input())

# Remove leading and trailing spaces
sentence = sentence.strip()

# Convert to lowercase
sentence = sentence.lower()

# Replace punctuation marks with spaces
sentence = sentence.replace(",", " ")
sentence = sentence.replace(".", " ")
sentence = sentence.replace("!", " ")
sentence = sentence.replace("?", " ")
sentence = sentence.replace(";", " ")
sentence = sentence.replace(":", " ")

# Split the sentence into words
words = sentence.split()

# Join words using exactly one space
cleaned_sentence = " ".join(words)

# Count the words
word_count = len(words)

# Extract first, last and selected words
first_word = words[0]
last_word = words[-1]
selected_word = words[position - 1]

# Extract first three and last three characters
first_word_prefix = first_word[:3]
last_word_suffix = last_word[-3:]

# Display the complete analysis
print("Cleaned Sentence:", cleaned_sentence)
print("Word Count:", word_count)
print("First Word:", first_word)
print("Last Word:", last_word)
print("Selected Word:", selected_word)
print("First Word Prefix:", first_word_prefix)
print("Last Word Suffix:", last_word_suffix)