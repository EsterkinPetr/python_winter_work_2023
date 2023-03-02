class Shape:
    def __init__(self, colour, square):
        self.color = colour
        self.square = square

    def set_color(self, color):

        self.color = color

    def ask_color(self):

        print(self.color)

    def set_square(self, square):

        self.square = square

    def ask_square(self):
        return self.square


a = Shape('white', 15)
a.set_color('red')
a.ask_color()
b = Shape('colourless', 0)
b.set_color('green')
b.set_square(20)
b.ask_color()
print(b.ask_square())

