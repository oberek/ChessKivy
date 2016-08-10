class ChessBoard(object):
    def __init__(self):
        self.chess_board = [
            {'a1': "-", 'b1': "-", 'c1': "-", 'd1': "-", 'e1': "-", 'f1': "-", 'g1': "-", 'h1': "-"},
            {'a2': "-", 'b2': "-", 'c2': "-", 'd2': "-", 'e2': "-", 'f2': "-", 'g2': "-", 'h2': "-"},
            {'a3': "-", 'b3': "-", 'c3': "-", 'd3': "-", 'e3': "-", 'f3': "-", 'g3': "-", 'h3': "-"},
            {'a4': "-", 'b4': "-", 'c4': "-", 'd4': "-", 'e4': "-", 'f4': "-", 'g4': "-", 'h4': "-"},
            {'a5': "-", 'b5': "-", 'c5': "-", 'd5': "-", 'e5': "-", 'f5': "-", 'g5': "-", 'h5': "-"},
            {'a6': "-", 'b6': "-", 'c6': "-", 'd6': "-", 'e6': "-", 'f6': "-", 'g6': "-", 'h6': "-"},
            {'a7': "-", 'b7': "-", 'c7': "-", 'd7': "-", 'e7': "-", 'f7': "-", 'g7': "-", 'h7': "-"},
            {'a8': "-", 'b8': "-", 'c8': "-", 'd8': "-", 'e8': "-", 'f8': "-", 'g8': "-", 'h8': "-"}]

    def printChessBoard(self):
        print("   A B C D E F G H")
        print("   _______________")
        for i in range(len(self.chess_board)):
            num = str(i + 1) + " |"
            print(num, end="")
            for k in self.chess_board[i]:
                print(self.chess_board[i][k], end=' ')

            print()
        return self.chess_board

    def placePiece(self, k, v):
        upper_or_lower = None
        if v[1] == 'd':
            upper_or_lower = v[0].upper()
        else:
            upper_or_lower = v[0].lower()
        self.chess_board[int(k[1]) - 1][k] = upper_or_lower

    def move_piece(self, from_spot, to_spot):
        value_in_from_spot = None
        row_it_was_in = -1
        for x in range(len(self.chess_board)):
            if from_spot in self.chess_board[x].keys():
                value_in_from_spot = self.chess_board[x].get(from_spot, None)
                row_it_was_in = x
                break
        # FIX THIS ASAP
        if value_in_from_spot is not None:
            for x in range(len(self.chess_board)):
                if to_spot in self.chess_board[x].keys():
                    self.chess_board[x][to_spot] = value_in_from_spot
                    break

        self.chess_board[row_it_was_in][value_in_from_spot] = "-"
