from functools import reduce


school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}


teachers = [subject['teacher'] for subject in school.values()]
print(teachers)

print("-"*20)

list_of_numbers = [subject['students'] for subject in school.values()]
actual_list_of_number = [arr for arr in list_of_numbers for arr in arr]
scores = [score for (_,score) in actual_list_of_number]
print(scores)

print("-"*20)


total = reduce(lambda acc,x:acc+x,scores)
average = total/len(scores)
print("average",average)
