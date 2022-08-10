#!/usr/bin/env python3

import os
os.system("clear")

## ################################
## NODE STRUCTURE
## ################################
class Node():
  def __init__(self, data):
    self.data = data
    self.children = []


## ################################
## EXAMPLE TREE
## ################################
def createTree():
  ## level 0 (root)
  n0 = Node("0")
  ## level 1
  n00 = Node("00")
  n01 = Node("01")
  ## level 2
  n000 = Node("000")
  n011 = Node("011")
  n012 = Node("012")
  n013 = Node("013")
  ## level 3
  n0120 = Node("0120")
  n0130 = Node("0130")
  ## level 4
  n01300 = Node("01300")
  ## establish hierarchy
  n0.children    += [ n00, n01 ]
  n00.children   += [ n000 ]
  n01.children   += [ n011, n012, n013 ]
  n012.children  += [ n0120 ]
  n013.children  += [ n0130 ]
  n0130.children += [ n01300 ]
  ## return tree root
  return n0


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