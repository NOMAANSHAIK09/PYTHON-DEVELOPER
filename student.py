x = int(input("Enter the grade: "))

if x > 96:
    print("The grade is S+")
elif x > 81 and x <= 90:
    print("The grade is A")
elif x > 71 and x <= 80:
    print("The grade is B")
elif x > 61 and x <= 70:
    print("The grade is C")
elif x > 51 and x <= 60:
    print("The grade is D")
else:
    print("The student has failed")
