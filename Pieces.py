class Piece(object):
    description = ''
    color = ''


class Pawn(Piece):
    horizontal_movement = 0
    vertical_movement = 1


class Rook(Piece):
    horizontal_movement = 1

class Knight(Piece):
    pass