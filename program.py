#!/usr/bin/env python3

import os
os.system("clear") # clear terminal window


## CHESS PIECES
dict_pawn = {
  "name"  : "P",
  "value" : 1.0,
  "count" : 5,
  "move_mask" : [ ],
}

dict_bishop = {
  "name"  : "B",
  "value" : 3.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_knight = {
  "name"  : "N",
  "value" : 3.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_castle = {
  "name"  : "C",
  "value" : 5.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_queen = {
  "name"  : "Q",
  "value" : 9.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_king = {
  "name"  : "K",
  "value" : 100, # lol, for all intents and purposes this is the same as infinity
  "count" : 1,
  "move_mask" : [ ],
}

dict_pieces = {
  1 : dict_pawn,
  2 : dict_bishop,
  3 : dict_knight,
  4 : dict_castle,
  5 : dict_queen,
  6 : dict_king
}


## CHESS BOARD
class ChessBoard():
  def __init__(self):
    self.size  = 5
    self.board = [ [0] * self.size ] * self.size
    ## black pieces
    self.board[-1] = [ -4, -3, -2, -5, -6 ]
    self.board[-2] = [ -1 ] * 5
    ## white pieces
    self.board[1] = [ +1 ] * 5
    self.board[0] = [ +4, +3, +2, +5, +6 ]

  def printBoard(self):
    ## white starts at the bottom and black at the top
    for row in self.board[:: -1]:
      count = 0
      for cell in row:
        ## empty
        if cell == 0:
          str_cell = "~~"
        ## white piece
        elif cell > 0:
          str_cell = "+" + dict_pieces[abs(cell)]["name"]
        ## black piece
        elif cell < 0:
          str_cell = "-" + dict_pieces[abs(cell)]["name"]
        ## formatting
        if count+1 < self.size:
          print(str_cell, end="  ")
        else: print(str_cell, end="\n")
        count += 1


## NODE STRUCTURE
class Node():
  def __init__(self, board, parent_node=None):
    self.board       = board
    self.parent_node = parent_node
    self.child_nodes = []


## COMPUTE ALL POSSIBLE NEXT POSSIBLE GAME STATES
def getNextBoardStates():
  a = 10

def computeChildNodes(root):
  a = 10


## CHESS ENGINE
class Engine():
  def __init__(self, max_depth):
    self.root      = None
    self.max_depth = max_depth
    self.height    = 0
    self.num_nodes = 0
  
  def simulate(self):
    cb = ChessBoard()
    self.root = Node(cb.board)
    self.__simulateBF(self.root)
    # self.height
    # self.num_nodes

  def __simulateBF(self, root: Node):
    ## calculate all possible opening board states
    list_next_boards = getNextBoardStates(
      state = root.board,
      depth = 0
    )
    ## store set of possible moves
    queue = []
    for next_board in list_next_boards:
      queue.append({
        "depth": 1,
        "board": next_board,
        "parent": self.root
      })
    ## simulate game
    while len(queue) > 0:
      state   = queue.pop(0)
      depth  = state["depth"]
      board  = state["board"]
      parent = state["parent"]
      ## trim branches at a particular depth
      if (depth+1) >= self.max_depth: return
      # ## check if the state has occured before
      # if ...: continue
      ## create node
      node = Node(
        parent
      )
      ## check end game requirements
      ## identify all next possible moves


## MAIN PROGRAM
def main():
  game = Engine()
  # game.simulate()


## RUN PROGRAM
if __name__ == "__main__":
  main()


## END OF PROGRAM