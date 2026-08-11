number = int(input())
sum_of_digit = 0

#Exact and add each digit using a while loop
while number > 0:
    digit = number % 10
    sum_of_digit += digit
    number = number // 10

print(f"Sum of Digits: {sum_of_digit}") 