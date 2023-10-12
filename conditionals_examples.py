# Function that determines if the given age is old enough
# to vote
def old_enough_to_vote(age: int) -> bool:
    return age >= 18


# print(old_enough_to_vote(2))
# print(old_enough_to_vote(18))
# print(old_enough_to_vote(20))

# Based on your age, determine whether you can a) vote
# b) drink alcohol c) both d) neither
def old_enough(age: int) -> str:
    if age >= 18 and age >= 21:
        return "Both"
    if age < 18 and age <= 21:
        return "Neither"
    if age >= 18 and age < 21:
        return "Yes vote, no drink"


# print(old_enough(2))
# print(old_enough(18))
# print(old_enough(19))
# print(old_enough(21))


# Given your age and your country,
# output whether you can:
# a) vote b) drink c) both d) neither
# Drinking age in US: 21
# Drinking age in Canada: 19
# Drinking age in Mexico: 18
# Voting age in all countries: 18
def old_enough_2(age: int, country: str) -> str:
    if country == "US":
        return old_enough(age)
    if country == "Mexico":
        if age >= 18:
            return "Both"
        if age <= 18:
            return "Neither"
    if country == "Canada":
        if age >= 18 and age >= 19:
            return "Both"
        if age < 18 and age <= 19:
            return "Neither"
        if age >= 18 and age < 19:
            return "Yes vote, no drink"


print(old_enough_2(3, "US"))
print(old_enough_2(18, "US"))
print(old_enough_2(25, "US"))
print(old_enough_2(3, "Canada"))
print(old_enough_2(18, "Canada"))
print(old_enough_2(19, "Canada"))
print(old_enough_2(1, "Mexico"))
print(old_enough_2(18, "Mexico"))
print(old_enough_2(1000000, "Mexico"))


# Game of life rules:
# For empty cells: stay empty unless it has exactly 3 neighbors
# For filled cells: stays filled if it has 2 or 3 neighbors
#   becomes empty if it has 0, 1, 4, 5, 6, 7, or 8 neighbors

# Takes in a cell's state (empty/filled) and how many neighbors,
# outputs whether or not the cell should become empty or filled
# state is False for empty, True for filled
# num_of_neighbors means how many filled squares and next to this square
# outputs True if this cell will become filled
# outputs False if this cell will become empty
def one_tick(state: bool, num_of_neighbors: int) -> bool:
    if state == False:      # case for empty cells
        if num_of_neighbors == 3:
            return True
        else:
            return False
    else:                   # case for filled cells
        if num_of_neighbors == 2 or num_of_neighbors == 3:
            return True
        else:
            return False


print(one_tick(False, 3))   # True
print(one_tick(False, 2))   # False
print(one_tick(False, 6))   # False
print(one_tick(True, 2))   # True
print(one_tick(True, 3))   # True
print(one_tick(True, 0))   # False
print(one_tick(True, 1))   # False
print(one_tick(True, 5))   # False
