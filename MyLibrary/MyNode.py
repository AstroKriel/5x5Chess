import chess

## ################################
## NODE STRUCTURE
## ################################
class Node():
  def __init__(self, board: chess.Board, parent):
    self.board    = board
    self.parent   = parent
    self.children = []

def createNode(board: chess.Board, parent=None):
  n = Node(board, parent)
  if parent is not None:
    parent.children.append(n)
  return n

## END OF LIBRARY