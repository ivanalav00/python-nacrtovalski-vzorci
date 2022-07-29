import turtle
from oblika import Oblika

#prvi podsistem
class Trikotnik(Oblika):

    def narisi(self, velikost):
        tur = turtle.Turtle()

        for i in range(velikost * 4):
            tur.forward(i * 8)
            tur.right(120)

        turtle.done()

#drugi podsistem
class Kvadrat(Oblika):

    def narisi(self, velikost):
        tur = turtle.Turtle()

        tur.forward(velikost)
        tur.left(90)
        tur.forward(velikost)
        tur.left(90)
        tur.forward(velikost)
        tur.left(90)
        tur.forward(velikost)

        turtle.done()

#tretji podsistem
class Krog(Oblika):

    def narisi(self, velikost):
        tur = turtle.Turtle()
        tur.circle(velikost)

        turtle.done()


