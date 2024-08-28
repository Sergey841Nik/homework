grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

average_grades = []
for i in grades:
    average_grade = round(sum(i)/len(i), 2)
    average_grades.append(average_grade)

res = dict(zip(students, average_grades))
print(res)

