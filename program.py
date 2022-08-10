dict_pawn = {
  "value" : 1.0,
  "count" : 5,
  "move_mask" : [ ],
}

dict_bishop = {
  "value" : 3.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_knight = {
  "value" : 3.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_castle = {
  "value" : 5.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_queen = {
  "value" : 9.0,
  "count" : 1,
  "move_mask" : [ ],
}

dict_king = {
  "value" : 100, # lol, for all intents and purposes this is the same as infinity
  "count" : 1,
  "move_mask" : [ ],
}

dict_pieces = {
  0 : dict_pawn,
  1 : dict_bishop,
  2 : dict_knight,
  3 : dict_castle,
  4 : dict_queen,
  5 : dict_king
}

def main():
  dict_pieces_w = dict_pieces.copy()
  dict_pieces_b = dict_pieces.copy()

if __name__ == "__main__":
  main()

## END OF PROGRAM