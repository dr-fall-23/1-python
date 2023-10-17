# Challenge Problem
from typing import List
# We can represent the state of a tic-tac-toe game as a 
# 3x3 grid stored as a list of 3 lists in python.
# Each element in this grid can either be "X", "O" or " "

# For example, here is an empty tic-tac-toe game:
BLANK = [[" ", " ", " "],\
         [" ", " ", " "],\
         [" ", " ", " "]]

# Here is a tic-tac-toe game with a few turns played:
PROGRESS = [["X", " ", "O"],\
            [" ", "X", " "],\
            [" ", " ", "O"]]

# Here is a completed tic-tac-toe game where "O" wins:
O_WIN = [["X", " ", "O"],\
         [" ", "X", "O"],\
         [" ", "X", "O"]]

# Here is a completed tic-tac-toe game where "X" wins:
X_WIN = [["X", " ", "O"],\
         [" ", "X", "O"],\
         [" ", " ", "X"]]

# Write the function "ttt_winner" which takes in a 3x3 array
# representing the tic-tac-toe game state.
# if there state has no winner, return "No Winner"
# if O has won the game, return "O"
# if X has won the game, return "X"

# For example...
# ttt_winner(BLANK) -> "No Winner"
# ttt_winner(PROGRESS) -> "No Winner"
# ttt_winner(O_WIN) -> "O"
# ttt_winner(X_WIN) -> "X"

# Returns the winner of a tic-tac-toe game state
def ttt_winner(board : List[List[str]]) -> str:
    # Write your code here!
