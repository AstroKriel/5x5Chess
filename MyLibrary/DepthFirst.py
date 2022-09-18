from . import MyNode, ChessFuncs


## ################################
## SIMULATION
## ################################
def simulate(
    root: MyNode.Node,
    parent: MyNode.Node,
    depth: int,
    max_depth: int
  ):
  if (depth+1) > max_depth:
    return
  # ChessFuncs.print5x5Board(parent.board, depth)
  for next_board in ChessFuncs.getNextBoardStates(parent.board):
    if checkNodeOccurance(root, next_board.fen().split(" ")[0]):
      continue
    simulate(
      root      = root,
      parent    = MyNode.createNode(next_board, parent),
      depth     = depth+1,
      max_depth = max_depth
    )


## ################################
## NODE TRAVERSAL
## ################################
def traverseTree(node: MyNode.Node):
  ''' Template traversal '''
  node.board
  for child in node.children:
    traverseTree(child)

def printTree(node: MyNode.Node):
  print(node.board)
  for child in node.children:
    printTree(child)

# def countNumGames(
#     node: Node,
#     num_games: int
#   ):
#   ## count node if it lies at the end of a branch
#   if isinstance(node.name, list):
#     if len(node.children) == 0:
#       num_games += 1
#   ## count child-nodes
#   for child in node.children:
#     num_games = countNumGames(child, num_games)
#   ## return count
#   return num_games

# def getTreeNodes(
#     node: Node,
#     dict_network: dict
#   ):
#   ## append current node connection to children
#   dict_network.update({
#     str(node.name): [
#       str(child.name)
#       for child in node.children
#       if isinstance(child.name, list)
#     ]
#   })
#   ## append child-nodes
#   for child in node.children:
#     getTreeNodes(child, dict_network)

# def countTreeNodes(
#     node: Node,
#     num_nodes: int
#   ):
#   ## count current node
#   if isinstance(node.name, list):
#     num_nodes += 1
#   ## count child-nodes
#   for child in node.children:
#     num_nodes = countTreeNodes(child, num_nodes)
#   ## return count
#   return num_nodes

# def getNodeIndex(
#     node: Node,
#     ref_hands: list,
#     index: int
#   ):
#   ## check if the contents of the current node in the branch matches the reference
#   if node.name == ref_hands:
#     return index
#   ## increment the node index
#   if isinstance(node.name, list):
#     index += 1
#   ## check if the contents of any of the child-nodes match the reference
#   for child in node.children:
#     child_index = getNodeIndex(child, ref_hands, index)
#     if child_index is not None:
#       return child_index
#   ## none of the nodes matched the reference
#   return None

def checkNodeOccurance(
    node: MyNode,
    ref_fen: str
  ):
  ## check if the contents of the current node in the branch matches the reference
  if ref_fen in node.board.fen():
    return True
  ## check if the contents of any of the child-nodes match the reference
  for child in node.children:
    if checkNodeOccurance(child, ref_fen):
      return True
  ## none of the nodes matched the reference
  return False


## END OF LIBRARY