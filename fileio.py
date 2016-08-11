import re
import collections


class FileIO(object):
    placed_pieces_keys = []
    placed_pieces_values = []
    move_from = {}
    move_to = {}
    counter = 0

    def __init__(self, input_file):
        self.input_file = input_file

    def readFile(self):
        f = open(self.input_file)

        # Dicts
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
                self.placed_pieces_keys.append(str(line[2:4].replace("\n", "")))
                self.placed_pieces_values.append(line[:2])

            elif len(line.split()) == 2:
                two_locations = line.split()
                if not len(re.findall(list_of_places, line)) == 2:
                    raise ValueError("ERROR: Incorrect Place on Map")
                temp = ('Piece at ' + two_locations[0] + ' moved to ' + two_locations[1])
                if "*" in two_locations[1]:
                    temp = temp + " and captures the piece at " + line.split()[1]
                temp = temp.replace("*", "")
                self.move_from[self.counter]= two_locations[0]
                self.move_to[self.counter] = two_locations[1]
                self.counter += 1

            elif len(line.split()) == 4:
                two_locations = line.split()
                if not len(re.findall(list_of_places, line)) == 4:
                    raise ValueError("ERROR: Incorrect Place on Map")
                temp = ('Piece at ' + line.split()[0] + ' moved to ' + line.split()[1])
                temp += (' and piece at ' + line.split()[2] + ' moved to ' + line.split()[3])
                self.move_from[self.counter] = two_locations[0]
                self.move_to[self.counter] = two_locations[1]
                self.counter += 1
                self.move_from[self.counter]= two_locations[2]
                self.move_to[self.counter] = two_locations[3]
                self.counter += 1

            print(temp)

