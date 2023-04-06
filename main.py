from replit import clear
from art import logo
import random

grid = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}


def tictactoe():
  for row in grid:
    print(grid[row])

def replace_number(number):
    if number <= 3:  #1, 2, 3
      grid[1][number - 1] = "X"
    elif number <= 6:  # 4, 5, 6
      new_number = number % 3
      grid[2][new_number - 1] = "X"
    elif number <= 9:  # 7, 8, 9
      new_number = number % 3
      grid[3][new_number - 1] = "X"
    else:
      print("That's not an option.")

def robot():
  for row in grid:
    random.choice(grid[row])
  
game_over = False
while not game_over:

  print(logo)
  tictactoe()
  user_number = int(
    input(
      "Enter a number from 1-9 corresponding to the numbers on the grid: "))
  clear()
  
  replace_number(number=user_number)