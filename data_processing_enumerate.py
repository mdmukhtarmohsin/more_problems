students = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 95, 78, 92, 88]

print("\n".join(f"{i}: {name}" for i,name in enumerate(students)))
print("-"*20)
print("\n".join(f"{name}: {score}" for name,score in zip(students,scores)))
print("-"*20)
print("\n".join(f"{name}: {score} position {i}" for i,[name,score] in enumerate(zip(students,scores)) if score > 90))
print("-"*20)
print({name:score for name,score in zip(students,scores)})
