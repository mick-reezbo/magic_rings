from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty, StringProperty

class RingsGame(Widget):
    rb1 = ObjectProperty(None)
    rb2 = ObjectProperty(None)
    rb3 = ObjectProperty(None)
    rb4 = ObjectProperty(None)
    rb5 = ObjectProperty(None)
    rb6 = ObjectProperty(None)
    rb7 = ObjectProperty(None)
    rb8 = ObjectProperty(None)
    rb9 = ObjectProperty(None)
    rb10 = ObjectProperty(None)
    bb1 = ObjectProperty(None)
    bb2 = ObjectProperty(None)
    bb3 = ObjectProperty(None)
    bb4 = ObjectProperty(None)
    bb5 = ObjectProperty(None)
    bb6 = ObjectProperty(None)
    bb7 = ObjectProperty(None)
    bb8 = ObjectProperty(None)
    bb9 = ObjectProperty(None)
    bb10 = ObjectProperty(None)
    cb1 = ObjectProperty(None)
    cb2 = ObjectProperty(None)
    cb3 = ObjectProperty(None)
    cb4 = ObjectProperty(None)
    cb5 = ObjectProperty(None)
    cb6 = ObjectProperty(None)
    cb7 = ObjectProperty(None)
    cb8 = ObjectProperty(None)
    cb9 = ObjectProperty(None)
    yb1 = ObjectProperty(None)
    yb2 = ObjectProperty(None)
    yb3 = ObjectProperty(None)
    yb4 = ObjectProperty(None)
    yb5 = ObjectProperty(None)
    yb6 = ObjectProperty(None)
    yb7 = ObjectProperty(None)
    yb8 = ObjectProperty(None)
    yb9 = ObjectProperty(None)
    pass

class RingsBoard(Widget):
    pass

class Ring(Widget):
    pass

class RedBall(Widget):
    r = StringProperty('')
    n = NumericProperty(None)
    pass

class BlackBall(Widget):
    r = StringProperty('')
    n = NumericProperty(None)
    pass

class CyanBall(Widget):
    r = StringProperty('')
    n = NumericProperty(None)
    pass

class YellowBall(Widget):
    r = StringProperty('')
    n = NumericProperty(None)
    pass

class RingsApp(App):

    def build(self):
        game = RingsGame()
        return game

if __name__ == '__main__':
    RingsApp().run()
