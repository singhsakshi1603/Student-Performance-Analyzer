def generate_report(students):
    print("\nClass Performance Report")
    if not students:
        print("Add at least one student first.")
        return
    averages=[
        student["average"]
        for student in students
    ]
    class_average=sum(averages)/len(averages)
    top_student=max(
        students,
        key=lambda student:student["average"]
    )
    passed=sum(
        1
        for student in students
        if student["average"]>=50
    )
    failed=len(students) - passed
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_average:.2f}")
    print(
        f"Highest Performer:"
        f"{top_student['name']}"
        f"({top_student['average']:.2f})"
    )
    print(f"Passed: {passed}")
    print(f"Needs Improvement: {failed}")
    print("\nRanking")
    ranking=sorted(
        students,
        key=lambda student: student["average"],
        reverse=True
    )
    for position, student in enumerate(ranking, start=1):
        print(
            f"{position}. "
            f"{student['name']} - "
            f"{student['average']:.2f} "
            f"({student['grade']})"
        )