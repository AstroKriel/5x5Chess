#!/usr/bin/env python3

import os, sys, time, chess
from MyLibrary import MyNode, ChessFuncs, DepthFirst, BreadthFirst
os.system("clear") # clear terminal window


## ################################
## CHESS ENGINE
## ################################
class Engine():
  def __init__(self, max_depth=2):
    self.root = MyNode.createNode(chess.Board(
      "8/8/8/rnbqk3/ppppp3/8/PPPPP3/RNBQK3 w - - 0 1"
    ))
    self.max_depth = max_depth
    self.height    = 0
    self.num_nodes = 0
  
  def simulate(self):
    print("Started simulation...")
    time_start = time.time()
    BreadthFirst.simulate(self.root, self.max_depth)
    # DepthFirst.simulate(self.root, self.root, 0, self.max_depth)
    time_elapsed = time.time() - time_start
    print("Finished simulation.")
    print(f"Elapsed time: {time_elapsed:.2f} seconds.")
    ## TODO: calculate tree height
    ## TODO: calculate number of nodes


## ################################
## MAIN PROGRAM
## ################################
def main():
  game = Engine(4)
  game.simulate()


## ################################
## RUN PROGRAM
## ################################
if __name__ == "__main__":
  main()
  sys.exit()


## END OF PROGRAM