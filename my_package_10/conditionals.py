pass_mark = 40
student_mark = float(input('Enter mark: '))

if student_mark < 0 or student_mark > 100:
    print("Invalid student mark.")

else:
    if student_mark >= pass_mark:
        print("Congratulations You have successfully Passed")

        if 40 <= student_mark <= 59:
            print("Grade : D")
        elif 60 <= student_mark <= 69:
            print("Grade : C")
        elif 70 <= student_mark <= 79:
            print("Grade : B")
        elif 80 <= student_mark <= 89:
            print("Grade : A-")
        elif 90 <= student_mark <= 100:
            print("Grade : A+")

    else:
        print("Sorry, you have failed.")
