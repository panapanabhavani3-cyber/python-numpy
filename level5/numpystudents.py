import numpy as np

# Student marks
marks = np.array([
    [85, 90, 80],
    [70, 75, 65],
    [95, 92, 96],
    [60, 55, 58],
    [88, 84, 90]
])

students = ["Bhavani", "Ravi", "Sita", "Kiran", "Anu"]

# Total marks
total = np.sum(marks, axis=1)

# Average marks
average = np.mean(marks, axis=1)

# Highest and lowest scorer
highest = np.argmax(total)
lowest = np.argmin(total)

# Subject-wise average
subject_average = np.mean(marks, axis=0)

# Pass/Fail
pass_students = np.all(marks >= 35, axis=1)

pass_count = np.sum(pass_students)
fail_count = len(students) - pass_count

# Grades
grades = []

for avg in average:
    if avg >= 90:
        grades.append("A+")
    elif avg >= 80:
        grades.append("A")
    elif avg >= 70:
        grades.append("B")
    elif avg >= 60:
        grades.append("C")
    elif avg >= 50:
        grades.append("D")
    else:
        grades.append("F")

# Rank
rank = np.argsort(np.argsort(-total)) + 1

# Class average
class_average = np.mean(average)

above_average = np.array(students)[average > class_average]

# Display results
print("Student Analysis")
print("----------------")

for i in range(len(students)):
    print(
        students[i],
        "Total:", total[i],
        "Average:", round(average[i], 2),
        "Grade:", grades[i],
        "Rank:", rank[i]
    )

print("\nHighest Scorer:", students[highest])
print("Highest Marks:", total[highest])

print("\nLowest Scorer:", students[lowest])
print("Lowest Marks:", total[lowest])

print("\nSubject-wise Average:", subject_average)

print("\nPass Count:", pass_count)
print("Fail Count:", fail_count)

print("\nClass Average:", round(class_average, 2))

print("\nStudents Above Class Average:")
print(above_average)