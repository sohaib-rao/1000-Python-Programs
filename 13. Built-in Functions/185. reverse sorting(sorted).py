students = [
    {"name": "Ali", "score": 75},
    {"name": "Sara", "score": 92},
    {"name": "Zain", "score": 88}
]
# Sorting based on score in descending order
top_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("Top Students:", top_students)