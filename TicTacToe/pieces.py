from abc import ABC
from enum import Enum


class PieceType(Enum):
    CROSS = 'X'
    CIRCLE = 'O'
    HASH = '#'
    EMPTY = '.'


class Piece(ABC):
    piece_type: PieceType

    def __init__(self, piece_type: PieceType):
        self.piece_type = piece_type


class CrossPiece(Piece):
    def __init__(self):
        super().__init__(PieceType.CROSS)


class CirclePiece(Piece):
    def __init__(self):
        super().__init__(PieceType.CIRCLE)


class EmptyPiece(Piece):
    def __init__(self):
        super().__init__(PieceType.EMPTY)