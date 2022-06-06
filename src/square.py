from figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.name = "square"
        if a > 0:
            self.a = self.b = a
        else:
            raise ValueError("Значение не правильное")
