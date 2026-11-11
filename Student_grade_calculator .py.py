name = input("Enter student's name: ")
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3
if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks < 80:
    grade = "A"
elif 60 <= average_marks < 70:
    grade = "B"
elif 50 <= average_marks < 60:
    grade = "C"
else:
    grade = "F"
print(f"Student Name: {name}")
print(f"Total Marks: {total_marks:g}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")