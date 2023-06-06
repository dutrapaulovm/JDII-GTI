from enum import Enum
from os import system
from math import inf as infinity
from Position import Position 
import numpy as np
import random
import time
from io import StringIO

color2num = dict(
    gray=30,
    red=31,
    green=32,
    yellow=33,
    blue=34,
    magenta=35,
    cyan=36,
    white=37,
    crimson=38,
)


def colorize(
    string: str, color: str, bold: bool = False, highlight: bool = False
) -> str:
    """Returns string surrounded by appropriate terminal colour codes to print colourised text.

    Args:
        string: The message to colourise
        color: Literal values are gray, red, green, yellow, blue, magenta, cyan, white, crimson
        bold: If to bold the string
        highlight: If to highlight the string

    Returns:
        Colourised string
    """
    attr = []
    num = color2num[color]
    if highlight:
        num += 10
    attr.append(str(num))
    if bold:
        attr.append("1")
    attrs = ";".join(attr)
    return f"\x1b[{attrs}m{string}\x1b[0m"

MAP = [
    "+-----+",
    "| : : |",    
    "| : : |",        
    "+-----+",
]

class Board:

    class State(Enum):
        IA = 1
        HUMAN = -1
        DRAW = 0
        CONTINUE = 2
        
        def __str__(self):
           return format(self.value)                                            
        
        def __int__(self):
            return self.value

    class Mark(Enum):
        X = "X"
        O = "O"
        EMPTY = " "
        def __str__(self):
           return format(self.value)                                            
        
        def __int__(self):
            return self.value        

    board = [[Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
             [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
             [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
             ]    

    turnToPlayer = State.IA
    currentMark = Mark.X
    availablePositions = []
    moves = []
    width = 3
    height = 3
    is_winner = False
    state = State.CONTINUE

    # Class Constructor
    def __init__(self):
        self.desc = np.asarray(MAP, dtype="c")
        self.create_available_positions()

    # Generate a random move and return the position    
    def random_move(self):
        position = None
        if (len(self.availablePositions) >= 1):
            #pos = random.randint(0, len(self.availablePositions))
            position = random.choice(self.availablePositions) #self.availablePositions[pos]            

        return position

    # Switch the turn of player    
    def switch_players(self):
        if (self.turnToPlayer is self.State.IA):
            self.turnToPlayer = self.State.HUMAN
            self.currentMark = self.Mark.O            
        else:
            self.turnToPlayer = self.State.IA
            self.currentMark = self.Mark.X

    def get_current_mark(self):
        return self.currentMark

    def get_winner(self):
        print(str(self.state))
        if (self.state == self.State.IA):
            return "IA"
        else:
            if (self.state == self.State.HUMAN):
                return "HUMAN"
            else:
                if (self.state == self.State.DRAW):
                    return "DRAW"
                else:
                    if (self.state.value[0] == self.State.CONTINUE):
                        return "CONTINUE"

    # Set the position on the board and if there is a valid position
    def set_move(self, x, y):
        pos = 0
        if (self.is_empty_position(x, y) and self.has_avaiable_positions()):
            for a in self.availablePositions:
                if (a.x == x and a.y == y):
                    self.availablePositions.pop(pos)
                    self.board[x][y] = self.currentMark                    
                    p = Position(x, y)
                    self.moves.append(p)
                    self.switch_players()
                    break
                pos = pos + 1
                
    # Set the position on the board and if there is a valid position
    def set_move(self, x, y):
        pos = 0
        if (self.is_empty_position(x, y) and self.has_avaiable_positions()):
            for a in self.availablePositions:
                if (a.x == x and a.y == y):
                    self.availablePositions.pop(pos)
                    self.board[x][y] = self.currentMark                    
                    p = Position(x, y)
                    self.moves.append(p)
                    self.switch_players()
                    break
                pos = pos + 1
                
    def set_simulate_move(self, x, y, mark):
        pos = 0
        if (self.is_empty_position(x, y) and self.has_avaiable_positions()):
            for a in self.availablePositions:
                if (a.x == x and a.y == y):
                    self.availablePositions.pop(pos)
                    self.board[x][y] = mark                  
                    p = Position(x, y)
                    self.moves.append(p)                    
                    break
                pos = pos + 1

	# Set the position on the board empty
    def set_empty(self, x, y):
        self.board[x][y] = self.Mark.EMPTY

	#Undo the movement
    def undo_move(self):
        if (len(self.moves) > 0):
            lastMove = self.moves.pop()
            self.board[lastMove.x][lastMove.y] = self.Mark.EMPTY
            self.availablePositions.append(lastMove)
            self.switch_players()
            self.is_winner = False
            
	#Undo the movement
    def undo_simulate_move(self):
        if (len(self.moves) > 0):
            lastMove = self.moves.pop()
            self.board[lastMove.x][lastMove.y] = self.Mark.EMPTY
            self.availablePositions.append(lastMove)            
            self.is_winner = False            

	# Checks if has a winner, but not set it
    def check_winner(self):
        state = self.State.CONTINUE
        mark = self.Mark.EMPTY
        is_winner = False

		#Horizontal
        for x in range(self.width):
            if self.equals_value(self.board[x][0], self.board[x][1], self.board[x][2]):
                is_winner = True
                mark = self.board[x][0]

		#Vertical
        for y in range(self.width):
            if self.equals_value(self.board[0][y], self.board[1][y], self.board[2][y]):
                is_winner = True
                mark = self.board[0][y]

		#Diagonal 1
        for y in range(self.width):
            if self.equals_value(self.board[0][0], self.board[1][1], self.board[2][2]):
                is_winner = True
                mark = self.board[0][0]

		#Diagonal 2
        for y in range(self.width):
            if self.equals_value(self.board[2][0], self.board[1][1], self.board[0][2]):
                is_winner = True
                mark = self.board[2][0]

        if (mark == self.Mark.X and is_winner):
            state = self.State.IA
        elif (mark == self.Mark.O and is_winner):
            state = self.State.HUMAN
        elif (not is_winner and not self.has_avaiable_positions()):
            state = self.State.DRAW            
        
        return state

	# Checks if has a winner
    def has_winner(self):
        state = self.State.CONTINUE
        mark = self.Mark.EMPTY

		#Horizontal
        for x in range(self.width):
            if self.equals_value(self.board[x][0], self.board[x][1], self.board[x][2]):
                self.is_winner = True
                mark = self.board[x][0]

		#Vertical
        for y in range(self.width):
            if self.equals_value(self.board[0][y], self.board[1][y], self.board[2][y]):
                self.is_winner = True
                mark = self.board[0][y]

		#Diagonal 1
        for y in range(self.width):
            if self.equals_value(self.board[0][0], self.board[1][1], self.board[2][2]):
                self.is_winner = True
                mark = self.board[0][0]

		#Diagonal 2
        for y in range(self.width):
            if self.equals_value(self.board[2][0], self.board[1][1], self.board[0][2]):
                self.is_winner = True
                mark = self.board[2][0]

        if (mark == self.Mark.X and self.is_winner):
            state = self.State.IA
        elif (mark == self.Mark.O and self.is_winner):
            state = self.State.HUMAN
        elif (not self.is_winner and not self.has_avaiable_positions()):
            state = self.State.DRAW
            
        self.state = state
        return self.state

    #Reset the board
    def reset(self):
        self.board = [[self.Mark.EMPTY, self.Mark.EMPTY, self.Mark.EMPTY],
                      [self.Mark.EMPTY, self.Mark.EMPTY, self.Mark.EMPTY],
                      [self.Mark.EMPTY, self.Mark.EMPTY, self.Mark.EMPTY],
                      ]
        self.turnToPlayer = self.State.IA
        self.currentMark = self.Mark.X
        self.is_winner = False
        self.availablePositions.clear()
        self.moves.clear()
        self.create_available_positions()
    
    #Create avaiable positions
    def create_available_positions(self):
        for i in range(self.width):
            for j in range(self.height):
                pos = Position(i, j)
                self.availablePositions.append(pos)

    # Checks if values are equals
    def equals_value(self, a, b, c):
        val = ((a != self.Mark.EMPTY) and (a == b) and (b == c) and (b == c))
        return val

	# Get the turn to player
    def get_turn_to_player(self):
        return self.turnToPlayer

	# Checks if the position is empty
    def is_empty_position(self, x, y):
        #print("Empty Position: " + str(self.board[x][y]) + " X: " + str(x) + " Y: " + str(y))
        return (self.board[x][y] == self.Mark.EMPTY)

	# Get the size of avaiable positions
    def size_available_positions(self):
        return len(self.availablePositions)

	# Get the size of movements
    def size_moves(self):
        return len(self.moves)

	# Get the size of avaiable positions
    def has_avaiable_positions(self):
        return (len(self.availablePositions) >= 1)

	#Print the all avaiable positions
    def print_avaiable_positions(self):
        outfile = StringIO()         

        out = self.desc.copy().tolist()
        out = [[c.decode("utf-8") for c in line] for line in out]        

        for a in self.availablePositions:
            print("X: " + str(a.y) + " Y: " + str(a.x))

	# Print the board
    def print_move(self):
        print("******************************")
        print("Board")
        for i in range(self.width):
            print(str(self.board[i][0]) + "|" +str(self.board[i][1]) + "|" + str(self.board[i][2]))
            print("******************************")
