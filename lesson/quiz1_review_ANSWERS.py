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
# a)
temp = 24.5
# ANSWER: FLOAT

# b)
honors = False
# ANSWER: BOOLEAN

# c)
student_1 = {"name": "George", "homeroom": 103}
# ANSWER: DICTIONARY

# d)
message = "I love computer science!"
# ANSWER: STRING

# e)
days = ["Monday", "Tuesday", "Wednesday"]
# ANSWER: LIST

# f)
pointer = -2
# ANSWER: INTEGER


# PROBLEM 2
# What is wrong with the following code? (Python will throw an error here!)
def foo(message: str) -> str:
    return message.append(" --from Luke")
# ANSWER: CAN'T MUTATE (APPEND/REMOVE) STRINGS


# PROBLEM 3
# Write a function that takes in a dictionary representing cities and their populations (in millions),
# and returns the total number of people who live in either New York, Los Angeles, or Chicago
city_pops_1 = {"Los Angeles": 3.8, "New York": 8.3,
               "Chicago": 2.3, "San Francisco": 0.8, "Boston": 0.6}

# Gets the total population of LA, NYC, and Chicago


def get_pop(cities: Dict) -> float:
    return cities["Los Angeles"] + cities["New York"] + cities["Chicago"]


print(get_pop(city_pops_1))     # 14.4


# PROBLEM 4
# What will the following boolean expressions (predicates) output?
# a)
(True and False)
# ANSWER: FALSE

# b)
(True or True or True or False)
# ANSWER: TRUE

# c)
(not (3 > 0))
# ANSWER: FALSE

# d)
(not (2 + 2 == 5) or (False and False))
# ANSWER: TRUE

# e)
("a" in ["a", "b", "c"] or (True != False))
# ANSWER: TRUE


# PROBLEM 5
my_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
# What will the following lines of code output?
# a) my_list[3]
# ANSWER: "d"

# b) my_list[-2]
# ANSWER: "g"

# c) len(my_list)
# ANSWER: 8

# d) my_list[len(my_list)]
# ANSWER: ERROR

# e) my_list[:]
# ANSWER: ["a", "b", "c", "d", "e", "f", "g", "h"]

# f) my_list[1:]
# ANSWER: ["b", "c", "d", "e", "f", "g", "h"]

# g) my_list[1:6:2]
# ANSWER: ["c", "e", "g"]

# h) my_list[2::2]
# ANSWER: ["d", "f", "h"]

# i) print(my_list[4:1:-1])
# ANSWER: ["e", "d", "c"]

# j) print(my_list[::-1])
# ANSWER: ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


# PROBLEM 6
# Consider the following list below:
student_list_1 = [{"name": "Luke", "homeroom": 102, "final_grades": ("A-", "C", "B-")}, {"name": "George", "homeroom": 103, "final_grades": ("B", "A", "A-")},
                  {"name": "Raj", "homeroom": 103, "final_grades": ("A", "A", "B+")}]
# a) What's the length of this list?
# ANSWER: 3

# b) What type of data (string, integer, etc) is student_list_1[2] ?
# ANSWER: DICTIONARY

# c) What type of data (string, integer, etc) is student_list_1[-1]["final_grades"] ?
# ANSWER: TUPLE

# d) How can I access Raj's homeroom?
# ANSWER: student_list[2]["homeroom"]

# e) How can I access Raj's grades?
# ANSWER: student_list[2]["final_grades"]

# f) How can I access Luke's third grade?
# ANSWER: student_list[0]["final_grades"][2]

# g) You see a for loop as shown below. What data type is "item?"
for item in student_list_1:
    pass    # (pass is a placeholder, like None)
# ANSWER: DICTIONARY


# PROBLEM 7
# Write a function that checks if the given string has any vowels in it
# Hint: you'll need a loop!
def any_vowels(a_string: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    for char in a_string:
        if char in vowels:
            return True
    return False


print(any_vowels("hello"))      # True
print(any_vowels("cmbnsklg"))   # False


# PROBLEM 8
TAX_RATE = 0.0625
# You've been shopping online, and have a list of items in your cart. The website you're using
# tells you the price of all your items combined, but you know that Massachusetts has a sales tax of 6.25%,
# meaning each item will cost 6.25% more at checkout.
# Using the TAX_RATE variable we gave you, write a function that gets the true cost of your shopping cart


def get_cost_with_tax(items: List[float]) -> float:
    total_cost = 0
    for item in items:
        total_cost += (item * (1 + TAX_RATE))
    return total_cost


print(get_cost_with_tax([10]))    # 10.625
print(get_cost_with_tax([10, 100]))    # 116.875


# PROBLEM 9
# Write a function similar to your answer for problem 7, but instead of using the variable TAX_RATE,
# it takes in an argument representing the tax rate (meaning it will work even if the sales tax is not 6.25%)

def get_cost_with_tax_2(items: List[float], tax_rate: float) -> float:
    total_cost = 0
    for item in items:
        total_cost += (item * (1 + tax_rate))
    return total_cost


print(get_cost_with_tax_2([10], 1.0))   # 20
print(get_cost_with_tax_2([20, 10], 0.5))   # 35


# PROBLEM 10
# Given an integer n, return a list of every number from 1 to n, but:
#   If the number is divisible by 3, add "Fizz" to the list instead
#   If the number is divisible by 5, add "Buzz" to the list instead
#   If the number is divisible by both 3 and 5, add "FizzBuzz" to the list instead
# Hint: Every item in the list should be a string. How do we change data types in Python (change from int to str)?
def fizz_buzz(n: int) -> List[str]:
    answer = []
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            answer.append("FizzBuzz")
        elif (i % 3 == 0):
            answer.append("Fizz")
        elif (i % 5 == 0):
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer


print(fizz_buzz(3))     # ["1", "2", "Fizz"]
print(fizz_buzz(5))     # ["1", "2", "Fizz", "4", "Buzz"]
print(fizz_buzz(15))     # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
