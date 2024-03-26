from abc import ABC, abstractmethod
from typing import List

from TicTacToe.pieces import Piece, EmptyPiece


class Board(ABC):
    x: int
    board: List[List[Piece]]

    def __init__(self, x):
        self.x = x
        self.board = []

    @abstractmethod
    def createBoard(self):
        pass

    @abstractmethod
    def printBoard(self):
        pass


# For Tic Tac Toe, creating an interface of the board might not be super useful

class TicTacBoard(Board):
    def __init__(self, x):
        super().__init__(x)

    def createBoard(self):
        for i in range(self.x):
            temp=[]
            for j in range(self.x):
                temp.append(EmptyPiece())
            self.board.append(temp)

    def printBoard(self):
        for i in range(self.x):
            for j in range(self.x):
                print("| ", self.board[i][j].piece_type.value, " | ", end=' ')
            print()
        print()

