# Read the number of values
value_count = int(input())

original_list = []

# Read and store all values using append()
for _ in range(value_count):
    original_list.append(int(input()))

# Create an alias using simple assignment
alias_list = original_list

# Create an independent shallow copy using copy()
copied_list = original_list.copy()

# Read position and value for alias modification
alias_position = int(input())
alias_value = int(input())

# Read position and value for copied list modification
copy_position = int(input())
copy_value = int(input())

# Update the alias list (convert 1-based index to 0-based index)
alias_list[alias_position - 1] = alias_value

# Update the copied list (convert 1-based index to 0-based index)
copied_list[copy_position - 1] = copy_value

# Display the required output lists
print("Original List:", original_list)
print("Alias List:", alias_list)
print("Copied List:", copied_list)

# Check identity using 'is' keyword
if alias_list is original_list:
    print("Alias Shares Original: Yes")
else:
    print("Alias Shares Original: No")

# Count how many positions contain different values
different_positions = 0
for i in range(value_count):
    if original_list[i] != copied_list[i]:
        different_positions += 1

print("Different Positions:", different_positions)