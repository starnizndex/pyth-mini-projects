
total   = float(input("Enter total: "))
marks  = float(input("Enter marks : "))
#percentage
percentage =(marks  / total marks) * 100

# Determine grade and comment
if percentage >= 90:
    grade = "A"
    comment = "Excellent"
elif percentage >= 80:
    grade = "B"
    comment = "Very Good"
elif percentage >= 70:
    grade = "C"
    comment = "Good"
elif percentage >= 60:
    grade = "D"
    comment = "Satisfactory"
elif percentage >= 50:
    grade = "E"
    comment = "Pass"
elif percentage >= 0:
    grade = "F"
    comment = "Fail"
else:
    grade = "Invalid"
    comment = "Invalid input"

# Display results
print(f"\nPercentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Comment: {comment}")