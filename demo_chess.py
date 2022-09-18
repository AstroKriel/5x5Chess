import os, chess
os.system("clear")

## ################################
## HELPER FUNCTIONS
## ################################
def legal5x5Moves(list_legal_8x8_moves):
  return [
    move for move in list_legal_8x8_moves
    if (int(str(move)[-1]) < 6) and (str(move)[-2] < "f")
  ]

def make5x5Board(fen):
  list_board_5x5 = []
  row_count = 5
  for row_8x8 in fen.split("/")[3:]:
    row_5x5 = ""
    for piece in row_8x8:
      if piece == " ": break
      elif piece in "12345678":
        row_5x5 += '- ' * int(piece)
      else: row_5x5 += f"{piece} "
    board_row = row_5x5[ :5*2] + f"| {row_count}"
    list_board_5x5.append(board_row)
    row_count -= 1
  list_board_5x5.append("---------")
  list_board_5x5.append("A B C D E")
  return list_board_5x5

def print5x5Board(fen):
  print("\n".join( make5x5Board(fen) ))
  print(" ")


## ################################
## MAIN PROGRAM
## ################################
## FEN generator: https://lichess.org/editor/8/8/8/8/8/8/8/8_w_-_-_0_1?color=white

def main():
  FEN_5x5 = "8/8/8/rnbqk3/ppppp3/8/PPPPP3/RNBQK3 w - - 0 1"
  board = chess.Board(FEN_5x5)
  print(board)
  print(" ")
  list_legal_8x8_moves = board.legal_moves
  for move in list_legal_8x8_moves:
    print(move)
  print(" ")
  list_legal_5x5_moves = legal5x5Moves(list_legal_8x8_moves)
  for move in list_legal_5x5_moves:
    print(move)
  print(" ")
  board.push(list_legal_5x5_moves[0])
  print(board.fen())
  print5x5Board(board.fen())


## ################################
## RUN PROGRAM
## ################################
if __name__ == "__main__":
  main()

## END OF PROGRAM