scores = {"Alice": 85, "Bob": 92, "Charlie": 88}

top_student = max(scores, key=scores.get)  
print(f"Top student is {top_student} with {scores[top_student]} points.")