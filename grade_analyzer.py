grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced_grades = grades[2:8]
print("Sliced grades (index 2 to 7):", sliced_grades)

grades_above_85 = [grade for grade in grades if grade > 85]
print("Grades above 85:", grades_above_85)

grades[3] = 95
print("Grades after replacing index 3 with 95:", grades)

grades.append(82)
grades.append(97)
grades.append(88)
print("Grades after appending three new grades:", grades)

sorted_grades = sorted(grades, reverse=True)
top_5_grades = sorted_grades[:5]
print("Top 5 grades (descending order):", top_5_grades)
