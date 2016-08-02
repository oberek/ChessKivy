def readFile(inputFile):
    f = open(inputFile)
    linesInFile = []

    typesOfPieces = {'K': 'King', 'Q': 'Queen', 'B': 'Bishop', 'N': 'Knight', 'R': 'Rook', 'P': 'Pawn'}
    colorsOfPieces = {'l': 'White', 'd': 'Black'}

    for line in f:
        temp = ''
        if len(line.split()) == 1:
            if not line[0] in typesOfPieces.keys() or not line[1] in colorsOfPieces.keys():
                raise ValueError("Incorrect type of piece")
            temp = (colorsOfPieces[line[1]] + ' ' + typesOfPieces[line[0]] + ' placed on ' + line[2] + line[3])
        elif len(line.split()) == 2:
            if not line.split()[0][0].isalpha() or not line.split()[0][1].isnumeric() or not line.split()[1][0].isalpha() or not line.split()[1][1].isnumeric():
                raise ValueError("Incorrect Place on Map")
            temp = ('Piece at ' + line.split()[0] + ' moved to ' + line.split()[1])
        elif len(line.split()) == 4:
            if not line.split()[0][0].isalpha() or not line.split()[0][1].isnumeric() or not line.split()[1][0].isalpha() or not line.split()[1][1].isnumeric():
                raise ValueError("Incorrect Place on Map")
            if not line.split()[2][0].isalpha() or not line.split()[2][1].isnumeric() or not line.split()[3][0].isalpha() or not line.split()[3][1].isnumeric():
                raise ValueError("Incorrect Place on Map")
            temp = ('Piece at ' + line.split()[0] + ' moved to ' + line.split()[1])
            temp += (' and piece at ' + line.split()[2] + ' moved to ' + line.split()[3])

        linesInFile += [temp]
        print(temp)

