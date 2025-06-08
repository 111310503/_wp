def summary(data):
    for student in data:
        total = sum(student['scores'])
        average = total / len(student['scores'])
        print(f"{student['name']} - Total: {total}, Average: {average:.2f}")
students = [
    {'name': 'Alice', 'scores': [85, 90, 88]},
    {'name': 'Bob', 'scores': [70, 75, 80]},
    {'name': 'Charlie', 'scores': [95, 100, 98]
    }
]
summary(stud)
