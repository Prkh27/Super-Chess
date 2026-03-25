import random
import math
def dice(n):# Dice rolling aspect using a parameter
  totdice = 0
  if n == "pass":
    return "the normal"
  for i in range(n):
    sindice = random.randint(1,6)
    totdice = totdice + sindice
  average = totdice/n
  if average % 1 >= 0.5:
    average = math.ceil(average)
  elif average % 1 < 0.5:
    average = math.floor(average)
  return average
def point(piece):# determines the point value of the piece about to be played
  piece = piece.lower()
  piece = piece.strip()
  pointvalue = 0
  if piece == "queen":
    pointvalue = 9
  elif piece == "rook":
    pointvalue = 5
  elif piece == "bishop":
    pointvalue = 3
  elif piece == "pawn":
    pointvalue = 1
  else:
    print("the piece you chose was either misspelled or a piece not controlled by the points in this system") 
    return "pass"
  return pointvalue
def algebranot(piece,square,take,color,castle):
  global whitelist
  global blacklist
  whitelist = []
  blacklist = []
  chespiece = piece.lower()
  chespiece = chespiece.strip()
  takepiece = take.lower()
  takepiece = takepiece.strip()
  team = color.lower()
  team = team.strip()
  fort = castle.lower()
  fort = fort.strip()
  algenot = ""
  if fort == "yes":
    side = input("is the castle king or queen side(king if right and queen if left(just type king or queen))")
    side = side.lower()
    side = side.strip()
    if side == "king":
      algenot = "0-0"
    elif side == "queen":
      algenot == "0-0-0"
    if team == "white":
      whitelist.append(algenot)
    elif team == "black":
      blacklist.append(algenot)
    return "just a placeholder"
  if chespiece == "queen":
    algenot = "Q"
  elif chespiece == "king":
    algenot = "K"
  elif chespiece == "rook":
    Algenot = "R" 
  elif chespiece == "bishop":
    Algenot = "B"
  elif chespiece == "knight":
    algenot = "N"
  elif chespiece == "pawn" or chespiece == "pawn attack":
    if "8" in square or "1" in square:
      promotion = input("what piece did you promote the pawn to?")
      promosplit = []
      for i in promotion:
        promosplit.append(i)
      promotion = promosplit[0]
      promotion = promotion.upper()
      algenot = square + "=" + promotion
      if team == "white":
        whitelist.append(algenot)
      elif team == "black":
        blacklist.append(algenot)
      return "just a placeholder"
  if takepiece == "yes":
    algenot = algenot + "x"
  algenot = algenot + square
  if team == "white":
    whitelist.append(algenot)
  elif team == "black":
    blacklist.append(algenot)
print("""Welcome to my game of super chess. 
In this, except for the king, knight, or pawn attack(put in as king), will be decided by a dice roll, 
in which the point value of the piece is how many dice rolled for movement. If a piece is blocking your movement for the dice roll,
then a pawn will stop before the piece and any other will take the piece.
The dice is then averaged and rounded on conventional rounding methods to control movement. 
If you checkmate someone, using normal rules, the checkmated person will create a chess puzzle
that must be neutral. 
If the one who checkmated in the base game wins the minigame, they win the game, but if the one who got checkmated in the main game wins,
the king has defended himself
successfully, and the game continues with any peices directly attacking the king being removed. """)
know = input("This system also has additional features based on algebraic notation. Do you know how algebraic notation works(it will be written for you)? ")
know = know.lower()
know = know.strip()
if know == "yes":
  print("you may continue playing. for simplicity's sake, a1 will be where the leftmost corner where the left rook is for white")
if know == "no":
  print("""This is a guide for notation from google
Algebraic chess notation uses uppercase letters to identify pieces (K, Q, R, B, N) and lowercase letters to identify board files (a-h). 
Pawns have no letter, designated only by their destination square. 
Piece Abbreviations (Uppercase):
K: King
Q: Queen
R: Rook
B: Bishop
N: Knight (used to distinguish from King)
(No letter): Pawn (e.g., \"e4\" indicates a pawn moves to e4) 
Board Coordinates:
Files (Columns): a, b, c, d, e, f, g, h (lowercase)
Ranks (Rows): 1, 2, 3, 4, 5, 6, 7, 8 
YouTube
YouTube
Action Symbols:
x: Captures (e.g., \"Bxf3\" means Bishop takes on f3)
+: Check (e.g., \"Qh5+\")
#: Checkmate (e.g., \"Qg7#\")
O-O: Kingside Castling
O-O-O: Queenside Castling
=: Promotion (e.g., \"e8=Q\")

A rank is basically the y axis, showing which row it is on and goes upwards with the bottom rank being 1 and top being 8
a file goes from the side that the ranks start, commonly from left to right. for simplicity's sake, a1 will be where the leftmost corner where the left rook is for white.""")
print("continue playing and type checkmate when on checkmate.")
overturn = 0
play = ""
minigame = ""
while minigame != "definite checkmate":
  while play != "checkmate":
    if overturn % 2 == 0:
      colplay = "white"
    elif overturn % 2 == 1:
      colplay = "black"
    piece = input(colplay + ", what piece are you planning to move(pawn attack counts as a separate peice so type pawn attack specifically(castle is also disregarded))?")
    print("You can move " + str(dice(point(piece))) + " space(s) with your piece.(none means it moves normally)")
    defense = input("do you wish to castle(yes or no)?")
    defense = defense.lower()
    defense = defense.strip()
    if defense == "yes":
      print(algebranot("blah","a1","no",colplay,"yes"))
    elif defense == "no":
      location = input("what square did you land on?")
      take = input("Did you take any pHiece?(select yes or no)")
      print(algebranot(piece, location, take, colplay, "no"))
    play = input("type checkmate if the opponent has been checkmated and type play if not.")
    overturn = overturn + 1
  loser = ""
  if colplay == "white":
    loser == "black"
  elif colplay == "black":
    loser == "white"
  print("as " + colplay + " has set up checkmate in the main game, " + loser + " must make a chess puzzle in which both teams must have an equivalent total point value\n(like the ones on chess.com)")
  print("if an advantage is discovered by " + colplay + ", then " + colplay + """wins the game(queen has 9 pts, rook has 5, knight has 3, bishop has 3, and pawn has 1) and a king
must be present on both sides. If """ + colplay + " wins, then they win the game completely. If " + loser + """ wins the game, then the game starts how it stopped but with any 
pieces directly attacking the king removed from the board as if captured by """ + loser + "." )
  minigame = input("Who won the minigame(Challenging and successfully being correct counts as winning)?")
  if minigame == colplay:
    minigame = "definite checkmate"
  elif minigame == loser:
    print("The algebraic notation for your main game is under so you can continue playing the original game")
    print("Black   White")
    for i in whitelist:
      print(whitelist[i] + "   " + blacklist[i])
    minigame = "play"
print("congratulations " + colplay + " for winning the game.")