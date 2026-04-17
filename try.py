student_name = input("Enter name: ")
student_marks  = int(input("enter the marks: "))
attendance_per = float(input("Enter the attandance percentage 1-100: "))


print("Hello ",student_name)
if student_marks>=90:
    grade = "A"
elif student_marks>=75:
    grade = "b"
elif student_marks>=50:
    grade = "C"
else:
    grade = "Fail"
print("Grade: ",grade)

if grade != "Fail":
    if(attendance_per>80):
        eligible = True
    else:
        eligible = False
else:
        eligible = False

print("Scholarship Eligible:",eligible)