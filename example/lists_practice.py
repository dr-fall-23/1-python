from typing import Dict

# A school stores data about its students in Python dictionaries.
# A Student is a dict of the form {"name": str, "homeroom": int, "gpa": float}.
student_a = {"name": "Abigail", "homeroom": 101, "gpa": 2.8}
student_b = {"name": "Bob", "homeroom": 102, "gpa": 3.8}
student_c = {"name": "Cade", "homeroom": 102, "gpa": 2.5}
student_d = {"name": "Dalia", "homeroom": 101, "gpa": 3.5}


# The school is launching a peer mentorship program,
# and wants to check if two students are compatible peers
# Two students are compatible peers if...
# - they are in the same homeroom
# - one student is honors (GPA at least 3.0), and the other is not

# Write the function peer_match which takes in two
# dictionaries representing students, and returns
# if they are a valid peer mentor pair.

# Returns if two students form a valid peer mentorship
def peer_match(student_1: Dict, student_2: Dict) -> bool:

    # are student_1 and student_2 in the same homeroom?
    same_homeroom = (student_1["homeroom"] == student_2["homeroom"])

    # will be True if one student gpa >= 3.0 and other student gpa < 3.0
    honors_and_not = (honors(student_1) and not honors(student_2)) or \
                     (honors(student_2) and not honors(student_1))

    return same_homeroom and honors_and_not

# Test your code here!

# Is a student honors?


def honors(student: Dict) -> bool:
    return student["gpa"] >= 3.0


print(range(3))
print(range(0, 3, 1))


my_dict = {"San Francisco": 0.81, "Boston": 0.68,
           "New York": 8.8, "Los Angeles": 3.9}
print(my_dict)
print(my_dict["San Francisco"])
print(my_dict["New York"])
print(my_dict.keys())

my_list = ["a", "b", "c", "d", "e"]
print(my_list[0:1])
print(my_list[0:4])
print(my_list[1:3])
print(my_list[5])
print(my_list[4:1:-1])
print(my_list[0:4:2])
print(my_list[:])
print(my_list[::-1])

# We didn't get to these in class, but the basic idea is that tuples work the same as lists, you just can't append or remove from them
my_tuple = ("alpha", "beta", "gamma", "delta")
print(my_tuple[0:1])
print(my_tuple[1:2])
print(my_tuple[1:])
print(my_tuple[:0:-2])
