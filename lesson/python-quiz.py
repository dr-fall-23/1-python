from typing import List, Dict

"""
Digital Ready Fall 2023 Computer Science Python Quiz

This exam is OPEN RESOURCE.

You may consult your notes, course materials, and the internet.

You may not communicate with anyone else (digitally or verbally): other classmates, chatGPT.

If you have any questions, please ask your lab leader.

Please write your name below and turn into your personal GitHub when finished.
"""

##################
# YOUR NAME:
##################

# Section 1: Short Answers***
# Write your answer as a single line (#) commment below each question prompt.

""" PROBLEM 1
What is the difference between a "float" and an "int"?
"""

""" PROBLEM 2
A piece of "boolean" data can hold two possible values: ___ and ___.
"""

""" PROBLEM 3
The MLB is keeping a new database of players, and are keeping track
of player data. For each of the following pieces of data,
state which *TYPE* of data (int, float, boolean or str)
would be most appropriate to store it:

a) The player's name

b) The player's jersey number

c) Whether or not the player is the captain of their team

d) The player's home run average (total home runs divided by games played)
"""

# Section 2: Writing Functions
# For each of the following questions, implement the desired function.
# Function headers have been provided.

""" PROBLEM 4
Write the function "format_name".
Given a first name and last name,
return the formatted name "Last, First"
For example, format_name("John", "Doe") -> "Doe, John"

For full credit, write 2 tests.
"""
# Returns a formatted name


def format_name(first: str, last: str) -> str:
    # Erase "pass" and write your code here!
    pass


""" PROBLEM 5
Two players are playing rock, paper, scissors!
Create the function "rps" which takes in 2 player's moves
and returns the winning move, or "draw"

For example,
rps("rock", "paper") -> "paper"
rps("scissors", "paper") -> "scissors"
rps("rock", "scissors") -> "rock"
rps("rock", "rock") -> "draw"

For full credit, write 4 tests that return unique results.
"""

# Returns the winning moves of a rock, paper, scissors game or "draw"


def rps(player_1: str, player_2: str) -> str:
    # Erase "pass" and write your code here!
    pass


""" PROBLEM 6
Four CS50 classes at Harvard just took their first exams! Here are the results.
Each int represents a student's grade on the exam.
In order to easily organize all of these results,
the computer science have composed them into a dictionary,
where for each dictionary entry the _key_ is the professor of that class,
and the _value_ is the list of grades for that classroom.
"""
grades1 = [90, 95, 88, 70, 78, 90, 88, 90, 90, 99,
           88, 90, 90, 99, 70, 78, 90, 80, 100, 70, 60, 80]
grades2 = [100, 95, 90, 79, 88, 89, 78, 90, 66, 90, 99]
grades3 = [90, 95, 88, 70, 78, 90, 80, 80, 80, 85, 85, 90, 90, 90, 95, 95]
grades4 = [90, 95, 88, 60, 78, 90, 100, 100, 99, 78, 78, 90]
cs50_grades = {"Mrs. Adams": grades1,
               "Mr. Bernoulli": grades2,
               "Mrs. Carlsson": grades3,
               "Mr. Danish": grades4}

"""
The computer science department wishes to quickly analyze this data
to see which professor's class is performing the best.

Write the function "best_class" which takes in a dictionary of professors and grades,
and returns the name of the professor whose class had the highest exam average.

For full credit, write one test. (hint: Mr. Bernouilli's class performed best!)

The helper function "average" has been provided.
"""

# Given a list of numbers, return their average
# NOTE: Do not edit this function!!!


def average(li: List[int]) -> float:
    return sum(li) / len(li)

# Returns the room number with the best exam average


def best_class(grades: Dict[int, List[int]]) -> int:
    # Erase "pass" and write your code here!
    pass

# BONUS: Which classroom had the best average, AND what was their score?
# Calculate answers to both questions and print them.
