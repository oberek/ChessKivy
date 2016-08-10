from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import consoleBoard
import fileio


class MyApp(App):
    def build(self):
        file = fileio.FileIO('input.log')
        file.readFile()
        initial_file_placements = file.placed_pieces
        piece_movements = file.move_to

        chess_board = consoleBoard.ChessBoard()
        chess_board.printChessBoard()
        print(initial_file_placements)

        for k, v in initial_file_placements.items():
            chess_board.placePiece(k, v)
            chess_board.printChessBoard()
            print()

        for from_spot,to_spot in piece_movements.items():
            chess_board.move_piece(from_spot, to_spot)
            chess_board.printChessBoard()
            print()

        self.title = 'Chess'
        num_of_cols = 8
        return self.make_gui_board(num_of_cols)

    def make_gui_board(self, num_of_cols):
        layout = GridLayout(cols=num_of_cols)
        for x in range(0, num_of_cols):
            if x % 2 == 1:
                for x in range(0, num_of_cols):
                    if x % 2 == 0:
                        layout.add_widget(Button(background_color=(0.0, 0.0, 0.0, 1.0)))
                    else:
                        layout.add_widget(Button(background_color=(1.0, 1.0, 1.0, 1.0)))
            else:
                for x in range(0, num_of_cols):
                    if x % 2 == 1:
                        layout.add_widget(Button(background_color=(0.0, 0.0, 0.0, 1.0)))
                    else:
                        layout.add_widget(Button(background_color=(1.0, 1.0, 1.0, 1.0)))
        return layout


MyApp().run()
