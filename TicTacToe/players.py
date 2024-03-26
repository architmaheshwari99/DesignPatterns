from abc import ABC

from TicTacToe.pieces import Piece


class Player(ABC):
    name: str
    playingPiece: Piece

    def __init__(self, name, playingPiece):
        self._name = name
        self._playingPiece = playingPiece

    @property
    def playingPiece(self):
        return self._playingPiece

    @playingPiece.setter
    def playingPiece(self, value):
        self._playingPiece = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


