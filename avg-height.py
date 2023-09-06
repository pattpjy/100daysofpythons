student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)

average = total_height/num_of_students
print(round(average))
