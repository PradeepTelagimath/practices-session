student_count = int(input())
marks = []

#Read and store all marks using append()
for i in range(0,student_count):
    score = int(input())
    marks.append(score)

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

#Update the mark at the entered student position
marks[position-1]=corrected_mark 

#calculate the total, average, highest and lowest marks
total_marks = sum(marks)
average_marks = total_marks / student_count
highest_mark = max(marks)
lowest_mark = min(marks)

passed_students = 0

for mark in marks:
    if mark >= passing_mark:
        passed_students += 1

print(f"Updated Marks: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Passed Students: {passed_students}")