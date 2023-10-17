# Exit Ticket
from typing import Dict, List
# A school stores data for their students as dictionaries of the form
# {"name": str, "homeroom": int, "gpa": flat}
# A list of example students are provided below
student_a = {"name": "Abigail", "homeroom": 101, "gpa": 2.8}
student_b = {"name": "Bob", "homeroom": 102, "gpa": 3.8}
student_c = {"name": "Cade", "homeroom": 102, "gpa": 2.5}
student_d = {"name": "Dalia", "homeroom": 101, "gpa": 3.5}
student_e = {"name": "Edward", "homeroom": 103, "gpa": 2.2}
student_f = {"name": "Fatima", "homeroom": 101, "gpa": 3.2}
students_list = [student_a, student_b, student_c, student_d, student_e, student_f]

# The school wishes to quickly determine which students are honors students are which are not.

# 1. Write the function is_honors which takes in a dict representing a student
# and returns if that student is honors (has a GPA > 3.0).
# for example,
# is_honors(student_a) -> False
# is_honors(student_b) -> True
# Include at least 2 tests

# Does a student have a grade greater than 3.0?
def is_honors(student : Dict) -> bool:
    # Write your code here!
    pass

# Test your code here!

# 2. Write a function honors_students which takes a list of students
# and returns a list of all students who are honors.
# for example,
# honors_students(student_list) -> [student_b, student_d, student_f]
# Include at least 1 test

# NOTE: This act of removing elements from a list that don't pass
# a particular test is often called "filtering" a list

# Given a list of students, returns those students
# who are honors
def honors_students(students : List[Dict]) -> List[Dict]:
    # Write your code here!
    pass

# Test your code here!