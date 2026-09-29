def calculate_grade(average):
    if average>=90:
        return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"
def read_number(prompt,minimum=None,maximum=None):
    while True:
        try:
            value=int(input(prompt).strip())
            if minimum is not None and value<minimum:
                print(f"Enter a value of at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a value of at most {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input.Please enter a whole number.")
def add_student(students):
    print("\n Add Student")
    name=input("Student Name:").strip().title()
    while not name:
        print("Name cannot be empty.")
        name=input("Student Name:").strip().title()
        roll_number=input("Roll Number:").strip()
        subject_count=read_number(
        "Number of subjects:",
        minimum=1,
        maximum=20
    )
        marks=[]
        for subject_number in range(1, subject_count + 1):
            mark = read_number(
            f"Marks for subject {subject_number} (0-100):",
            minimum=0,
            maximum=100
        )
        marks.append(mark)
    average=sum(marks)/len(marks)
    grade=calculate_grade(average)
    student={
        "name":name,
        "roll_number":roll_number,
        "marks":marks,
        "average":average,
        "grade":grade
    }
    students.append(student)
    print(f"\nRecord saved for {name}. Grade: {grade}")
def display_student(student, position=None):
    if position is not None:
        prefix=f"{position}. "
    else:
        prefix=""
        marks=", ".join(str(mark) for mark in student["marks"])
        print(
        f"{prefix}{student['name']} | "
        f"Roll:{student['roll_number']} | "
        f"Marks:{marks} | "
        f"Average:{student['average']:.2f} | "
        f"Grade:{student['grade']}"
    )
def view_students(students):
    print("\nStudent Records")
    if not students:
        print("No student records available.")
        return
    for position,student in enumerate(students, start=1):
        display_student(student, position)
def search_student(students):
    print("\nSearch Student")
    query = input("Enter name or roll number:").strip().lower()
    matches = [
        student
        for student in students
        if (
            query in student["name"].lower()
            or query==student["roll_number"].lower()
        )
    ]
    if not matches:
        print("No matching student found.")
        return
    for student in matches:
        display_student(student)