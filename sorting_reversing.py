employees = [
    ("Aliceya", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Caroliyaaaa", 55000, "Engineering"),
    ("Davidkabachaaaaaaa", 45000, "Sales")
]

accending_sort = sorted(employees, key=lambda x: x[1], reverse=False)
print(accending_sort)
print("-" * 20)

decending_sort = sorted(employees, key=lambda x: x[1], reverse=True)
print(decending_sort)
print("-" * 20)

department_salary_sort = sorted(employees, key=lambda x: (x[2], x[1]))
print(department_salary_sort)
print("-" * 20)

reverse_list = list(reversed(employees))
print(reverse_list)
print("-" * 20)

sort_by_name_length = sorted(employees, key=lambda x: len(x[0]))
print(sort_by_name_length)
print("-" * 20)






