import re


def readFile(input_file):
    f = open(input_file)
    lines_in_file = []

    types_of_pieces = {'K': 'King', 'Q': 'Queen', 'B': 'Bishop', 'N': 'Knight', 'R': 'Rook', 'P': 'Pawn'}
    colors_of_pieces = {'l': 'White', 'd': 'Black'}
    list_of_places = re.compile('[a-h][1-8]')

    for line in f:
        temp = ''
        if len(line.split()) == 1:
            if not line[0] in types_of_pieces.keys() or not line[1] in colors_of_pieces.keys():
                raise ValueError("ERROR: Incorrect Type Of Piece")
            if not len(re.findall(list_of_places, line[2:])) == 1:
                raise ValueError("ERROR: Incorrect Placement")
            temp = (colors_of_pieces[line[1]] + ' ' + types_of_pieces[line[0]] + ' placed on ' + line[2] + line[3])
        elif len(line.split()) == 2:
            if not len(re.findall(list_of_places, line)) == 2:
                raise ValueError("ERROR: Incorrect Place on Map")
            temp = ('Piece at ' + line.split()[0] + ' moved to ' + line.split()[1])
            if "*" in line.split()[1]:
                temp = temp + " and captures the piece at " + line.split()[1]
            temp = temp.replace("*", "")
        elif len(line.split()) == 4:
            if not len(re.findall(list_of_places, line)) == 4:
                raise ValueError("ERROR: Incorrect Place on Map")
            temp = ('Piece at ' + line.split()[0] + ' moved to ' + line.split()[1])
            temp += (' and piece at ' + line.split()[2] + ' moved to ' + line.split()[3])

        lines_in_file += [temp]
        print(temp)
