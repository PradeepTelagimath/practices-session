text = input()

vowel_count = 0

# Iteration directly over the string and count the vowels
for ch in text:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        vowel_count += 1

print(f"Vowel Count: {vowel_count}")        


