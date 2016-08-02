from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import fileio


class MainApp(App):
    class MyApp(App):
        def build(self):
            fileio.readFile('input.log')
            self.title = 'Chess'
            numOfCols = 8
            layout = GridLayout(cols = numOfCols)
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
