from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import consoleBoard
import fileio


class MyApp(App):
    def build(self):
        fileio.readFile('input.log')
        consoleBoardSim = consoleBoard.ChessBoard
        consoleBoardSim.printChessBoard()

        self.title = 'Chess'
        numOfCols = 8
        return self.makeGuiBoard(numOfCols)

    def makeGuiBoard(self, numOfCols):
        layout = GridLayout(cols=numOfCols)
        for x in range(0, numOfCols):
            if x % 2 == 1:
                for x in range(0, numOfCols):
                    if x % 2 == 0:
                        layout.add_widget(Button(background_color=(0.0, 0.0, 0.0, 1.0)))
                    else:
                        layout.add_widget(Button(background_color=(1.0, 1.0, 1.0, 1.0)))
            else:
                for x in range(0, numOfCols):
                    if x % 2 == 1:
                        layout.add_widget(Button(background_color=(0.0, 0.0, 0.0, 1.0)))
                    else:
                        layout.add_widget(Button(background_color=(1.0, 1.0, 1.0, 1.0)))
        return layout

MyApp().run()
