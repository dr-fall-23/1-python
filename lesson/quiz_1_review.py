from typing import Dict, List

# ********
# QUIZ 1 STUDY GUIDE
# Remember: any time we ask you to write a function,
# we expect a purpose statement and at least two tests!
# ********

# Misc. concepts to know:
# Difference between strings, tuples, dictionaries, and lists
#

# PROBLEM 1
# Write the data type or data structure of each variable below
# a
temp = 24.5
# b
honors = False
# c
student_1 = {"name": "George", "homeroom": 103}
# d
message = "I love computer science!"
# e
days = ["Monday", "Tuesday", "Wednesday"]
# f
pointer = -2


# PROBLEM 2
# What is wrong with the following code? (Python will throw an error here!)
def foo(message: str) -> str:
    return message.append(" --from Luke")


# PROBLEM 3
# Write a function that takes in a dictionary representing cities and their populations (in millions),
# and returns the total number of people who live in either New York, Los Angeles, or Chicago
city_pops_1 = {"Los Angeles": 3.8, "New York": 8.3,
               "Chicago": 2.3, "San Francisco": 0.8, "Boston": 0.6}


def get_pop(cities: Dict) -> float:
    pass    # Erase this line and write your code here!


# PROBLEM 4
# What will the following boolean expressions (predicates) output?
# a
(True and False)
# b
(True or True or True or False)
# c
(not (3 > 0))
# d
(not (2 + 2 == 5) or (False and False))
# e
("a" in ["a", "b", "c"] or (True != False))


# PROBLEM 6
my_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
# What will the following lines of code output?
# a
# my_list[3]
# b
# my_list[-2]
# c
# len(my_list)
# d
# my_list[len(my_list)]
# e
# my_list[:]
# f
# my_list[1:]
# g
# my_list[1:6:2]
# h
# my_list[2::2]
# i
# my_list[4:1:-1]
# j
# my_list[::-1]


# PROBLEM
# Consider the following list below:
student_list_1 = [{"name": "Luke", "homeroom": 102, "final_grades": ("A-", "C", "B-")}, {"name": "George", "homeroom": 103, "final_grades": ("B", "A", "A-")},
                  {"name": "Raj", "homeroom": 103, "final_grades": ("A", "A", "B+")}]
# a) What's the length of this list?
# b) What type of data (string, integer, etc) is student_list_1[2] ?
# c) What type of data (string, integer, etc) is student_list_1[-1]["final_grades"] ?
print(student_list_1[-1]["final_grades"])
# d) How can I access Raj's homeroom?
# e) How can I access Raj's grades?
# f) How can I access Luke's third grade?


# PROBLEM 5
# Write a function that checks if the given string has any vowels in it
# Hint: you'll need a loop!
def any_vowels(a_string: str) -> bool:
    pass    # Erase me and write your code here!


# PROBLEM 7
TAX_RATE = 0.0625
# You've been shopping online, and have a list of items in your cart. The website you're using
# tells you the price of all your items combined, but you know that Massachusetts has a sales tax of 6.25%,
# meaning each item will cost 6.25% more at checkout.
# Using the TAX_RATE variable we gave you, write a function that gets the true cost of your shopping cart


def get_cost_with_tax(items: List[float]) -> float:
    pass    # Erase me and write your code here!


# PROBLEM 8
# Write a function similar to your answer for problem 7, but instead of using the variable TAX_RATE,
# it takes in an argument representing the tax rate (meaning it will work even if the sales tax is not 6.25%)

# Erase me and write your code here!


# PROBLEM 9
# Given an integer n, return a list of every number from 1 to n, but:
#   If the number is divisible by 3, add "Fizz" to the list instead
#   If the number is divisible by 5, add "Buzz" to the list instead
#   If the number is divisible by both 3 and 5, add "FizzBuzz" to the list instead
# Hint: Every item in the list should be a string. How do we change data types in Python (change from int to str)?
def fizz_buzz(n: int) -> List[str]:
    pass    # Erase me and write your code here!
