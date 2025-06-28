# gpa_calculator.py
def grade_to_point(grade):
    grade = grade.upper()
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    elif grade == 'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    else:
        return None

def main():
    print("GPA Calculator (4.0 scale)")
    num_courses = int(input("Enter number of courses: "))

    total_units = 0
    total_points = 0

    for i in range(num_courses):
        print(f"\nCourse {i + 1}")
        unit = int(input("Enter course unit: "))
        grade = input("Enter grade (A-F): ")
        point = grade_to_point(grade)

        if point is None:
            print("Invalid grade. Try again.")
            return

        total_units += unit
        total_points += unit * point

    if total_units == 0:
        print("No courses entered.")
    else:
        gpa = total_points / total_units
        print(f"\nYour GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()
