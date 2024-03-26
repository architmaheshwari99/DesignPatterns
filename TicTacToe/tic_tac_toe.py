from collections import deque
from typing import List, Deque

from TicTacToe.board import Board, TicTacBoard
from TicTacToe.pieces import CrossPiece, CirclePiece, PieceType
from TicTacToe.players import Player


class TicTacToe:
    players: Deque[Player]
    game_board: Board

    def initializeGame(self):
        self.players = deque()
        playerA = Player("Archit", CrossPiece())
        playerB = Player("Casper", CirclePiece())

        self.players.append(playerA)
        self.players.append(playerB)

        self.game_board = TicTacBoard(3)
        self.game_board.createBoard()

    def startGame(self):
        noWinner = True
        while noWinner:
            playerMove = self.players.pop()

            isMoveInvalid = True
            i, j = 0, 0
            while isMoveInvalid:
                self.game_board.printBoard()
                try:
                    s = input("Enter your block")
                    i, j = s.split(' ')
                    i, j = int(i), int(j)
                    isMoveInvalid = self.ifIsMoveInvalid(i, j)
                # Can add custom exception messages here
                except Exception:
                    isMoveInvalid = True
                    pass


            self.game_board.board[i][j] = playerMove.playingPiece
            self.game_board.printBoard()

            winner = self.checkWinner(i, j, playerMove.playingPiece)
            if winner:
                return playerMove.name
            is_game_tied = self.checkForTie()
            if is_game_tied:
                return "No One"
            self.players.appendleft(playerMove)

    def checkForTie(self):
        empty_slot = False
        for i in range(3):
            for j in range(3):
                if self.game_board.board[i][j].piece_type == PieceType.EMPTY:
                    empty_slot = True

        return empty_slot

    def checkWinner(self, i, j, piece):
        winner = True
        for k in range(0, 3):
            if self.game_board.board[i][k].piece_type != piece.piece_type:
                winner = False

        if winner:
            return True

        for k in range(0, 3):
            if self.game_board.board[k][j].piece_type != piece.piece_type:
                winner = False

        if winner:
            return True

        for k in range(0, 3):
            if self.game_board.board[k][k].piece_type != piece.piece_type:
                winner = False

        if winner:
            return True

        for k in range(0, 3):
            if self.game_board.board[k][3-k-1].piece_type != piece.piece_type:
                winner = False

        if winner:
            return True

        return False

    def ifIsMoveInvalid(self, i, j):
        if self.game_board.board[i][j].piece_type != PieceType.EMPTY:
            return True

        return False

