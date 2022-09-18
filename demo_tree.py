import os
os.system("clear")

## ################################
## NODE STRUCTURE
## ################################
class Node():
  def __init__(self, data, parent=None):
    self.data     = data
    self.parent   = parent
    self.children = []

def createNode(data, parent=None):
  n = Node(data, parent)
  if parent is not None:
    parent.children.append(n)
  return n


## ################################
## EXAMPLE TREE
## ################################
def createTree():
  ## level 0 (root)
  root = createNode("0")
  ## level 1
  n0 = createNode("00", root)
  n1 = createNode("01", root)
  ## level 2
  n00 = createNode("000", n0)
  n11 = createNode("011", n1)
  n12 = createNode("012", n1)
  n13 = createNode("013", n1)
  ## level 3
  n120 = createNode("0120", n12)
  n130 = createNode("0130", n13)
  ## level 4
  n1300 = createNode("01300", n130)
  ## return the tree root
  return root


## ################################
## PRINT TREE
## ################################
def printBreadthFirst(root):
  queue_nodes = [root]
  while len(queue_nodes) > 0:
    node = queue_nodes.pop(0)
    print(node.data)
    for child_node in node.children:
      queue_nodes.append(child_node)

def printDepthFirst(node, index=0):
  pre = "  " * index
  if index > 0: pre += "--"
  print(f"{index}: {pre} {node.data}")
  index += 1
  for child in node.children:
    printDepthFirst(child, index)


## ################################
## MAIN PROGRAM
## ################################
def main():
  root = createTree()
  ## print tree nodes
  print("Breath-First:")
  printBreadthFirst(root)
  print(" ")
  print("Depth-First:")
  printDepthFirst(root)


## ################################
## RUN PROGRAM
## ################################
if __name__ == "__main__":
  main()

## END OF PROGRAM