'''
Elizabeth Meredith
IS 303 - A03

Grade Report
This program collects student names and scores and produces a grade summary.

Inputs:
- Number of students (int)
- For each student: name (string), score (int)

Processes:
- Collect student data into a list of dictionaries
- Accumulator: calculate total score and average
- Min/Max: find the highest and lowest score
- Filter: build a list of students who scored 70 or above (passing)

Outputs:
- Print each student name and score
- Print class average, highest score, lowest score, and list of passing students
'''

num_students = int(input("How many students? "))
students = []

for i in range(num_students):
    name = input(f"Student {i + 1} name: ")
    score = int(input(f"Student {i + 1} score: "))
    students.append({"name": name, "score": score})

# Accumulator: total score for average
total_score = 0
for student in students:
    total_score = total_score + student["score"]
average_score = total_score / len(students)

# Min/Max: find highest and lowest score
highest = students[0]
lowest = students[0]
for student in students:
    if student["score"] > highest["score"]:
        highest = student
    if student["score"] < lowest["score"]:
        lowest = student

# Filter: students who are passing (70 or above)
passing = []
for student in students:
    if student["score"] >= 70:
        passing.append(student["name"])

# Output
print("---")
print("Grade Report")
print("---")
for student in students:
    print(f"{student['name']}: {student['score']}")

print("---")
print(f"Class average: {average_score:.1f}")
print(f"Highest score: {highest['name']} ({highest['score']})")
print(f"Lowest score: {lowest['name']} ({lowest['score']})")

if len(passing) > 0:
    print(f"Passing students (70+): {', '.join(passing)}")
else:
    print("Passing students (70+): none")