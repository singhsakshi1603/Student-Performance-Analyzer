Student Performance Analyzer

##Problem Statement

Managing student academic records manually can be time-consuming and may
lead to errors while calculating averages, grades, and class
performance. The Student Performance Analyzer is a Python-based,
menu-driven application developed to simplify this process.

The system allows users to enter student details such as name, roll
number, number of subjects, and marks. It validates the entered marks,
calculates the average, assigns a grade, stores student records,
searches for students, and generates a class performance report. The
project also includes an algorithm toolkit for demonstrating basic
programming algorithms.

##Scope of the Project

The scope of the project includes:

-Adding and storing student records.
-Accepting marks for multiple subjects.
-Validating marks within the range of 0 to 100.
-Calculating the average marks of each student.
-Assigning grades from A+ to F based on the calculated average.
-Viewing all stored student records.
-Searching for a student using name or roll number.
-Generating class-level performance statistics.
-Finding the highest-performing student.
-Counting students who have passed and those who need improvement.
-Generating a ranking based on student averages
_Providing an algorithm toolkit containing factorial, Fibonacci
sequence, text reversal, decimal-to-binary conversion, and exchange
of two values.
-Providing a simple menu-driven interface for accessing all major
functions.

The project is intended as a basic academic programming application. It
uses in-memory data storage through Python lists and dictionaries and
does not include a permanent database or external authentication system.

##Target Users

The primary target users are:

-Students -- to understand and demonstrate Python programming
concepts through a practical project.

-Faculty members -- to demonstrate or evaluate concepts such as
functions, loops, conditions, lists, dictionaries, searching,
sorting, and input validation.

-Teachers or instructors -- for classroom demonstrations of basic
programming and algorithmic problem solving.

-Small academic groups -- for maintaining simple student
performance records during a programming exercise.

##High-Level Features

1. Student Record Management

The system allows users to add student names, roll numbers, subject
counts, and marks and stores the information in student records.

2. Grade Calculation

The application calculates the average marks and automatically assigns a
grade according to the defined grading conditions:

90 and above → A+

80--89 → A

70--79 → B

60--69 → C

50--59 → D

Below 50 → F

3. Input Validation

The read_number() function checks numerical input and ensures that
values remain within the specified minimum and maximum limits.

4. View Student Records

Users can display all currently stored student records, including marks,
average, and grade.

5. Student Search

Users can search for a student by entering part or all of the student's
name or the exact roll number.

6. Class Performance Report

The report module calculates the class average, identifies the highest
performer, counts passed and failed/needs-improvement students, and
displays student ranking according to average marks.

7. Algorithm Toolkit

The application provides a separate toolkit containing: - Factorial
calculation - Fibonacci sequence generation - Text reversal -
Decimal-to-binary conversion - Exchange of two values

8. Menu-Driven Interface

The main program provides a simple menu through which users can access
student management, reporting, searching, and algorithm functions.

##Technologies and Programming Concepts

Programming Language: Python

Program Structure: Multiple Python modules

Data Structures: Lists, dictionaries, and tuples

Core Concepts: Functions, loops, conditional statements, input
validation

Algorithms: Searching, sorting, factorial, Fibonacci, reversal,
and number conversion