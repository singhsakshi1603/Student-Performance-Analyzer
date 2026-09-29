from student_module import (
    add_student,
    view_students,
    search_student
)
from report_module import generate_report
from algorithm_module import algorithm_menu
def menu():
    print("\n" + "=" * 52)
    print("       STUDENT PERFORMANCE ANALYZER")
    print("="* 52)
    print("1.Add student record")
    print("2.View all student records")
    print("3.Generate class performance report")
    print("4.Search for a student")
    print("5.Open algorithm toolkit")
    print("0.Exit")
def main():
    students = []
    while True:
        menu()
        choice=input("Choose an option: ").strip()
        if choice=="1":
            add_student(students)
        elif choice=="2":
            view_students(students)
        elif choice=="3":
            generate_report(students)
        elif choice=="4":
            search_student(students)
        elif choice=="5":
            algorithm_menu()
        elif choice=="0":
            print(
                "\nThank you for using "
                "Student Performance Analyzer."
            )
            break
        else:
            print("Invalid choice. Select an option from 0 to 5.")
if __name__ == "__main__":
    main()