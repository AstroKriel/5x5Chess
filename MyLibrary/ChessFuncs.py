import chess


LIST_PIECE_VALUE = {
  "P": 10,
  "N": 30,
  "B": 30,
  "R": 50,
  "Q": 90,
  "K": 100,
  "p": -10,
  "n": -30,
  "b": -30,
  "r": -50,
  "q": -90,
  "k": -100
}


## ################################
## PRINT 5x5 BOARD
## ################################
def make5x5Board(fen: str, depth: int=0):
  pre_space = "   " * 5 * depth
  list_board_5x5 = []
  list_board_5x5.append(fen)
  row_count = 5
  for row_8x8 in fen.split("/")[3:]:
    row_5x5 = ""
    for piece in row_8x8:
      if piece == " ": break
      elif piece in "12345678":
        row_5x5 += "-- " * int(piece)
      else:
        row_5x5 += "w" if ("A" < piece and piece < "Z") else "b"
        row_5x5 += f"{piece.upper()} "
    list_board_5x5.append(pre_space + row_5x5[ :3*5] + f"| {row_count}")
    row_count -= 1
  list_board_5x5.append(pre_space + "---" * 5)
  list_board_5x5.append(pre_space + "A  B  C  D  E")
  return list_board_5x5

def print5x5Board(board: chess.Board, depth: int=0):
  print(depth)
  print("\n".join( make5x5Board(board.fen(), depth) ))
  print(" ")


## ################################
## COMPUTE FUNCTIONS
## ################################
def checkGameOver(board: chess.Board):
  return (
    board.is_stalemate() or
    board.can_claim_threefold_repetition() or
    board.is_fivefold_repetition() or
    board.is_insufficient_material() or
    board.is_seventyfive_moves()
  )

def legal5x5Moves(board: chess.Board):
  return [
    move for move in board.legal_moves
    if (int(str(move)[-1]) < 6) and (str(move)[-2] < "f")
  ]

def getNextBoardStates(board: chess.Board):
  list_next_boards = []
  list_next_moves = legal5x5Moves(board)
  for move in list_next_moves:
    board.push(move)
    list_next_boards.append(board.copy())
    board.pop()
  return list_next_boards


## END OF LIBRARY