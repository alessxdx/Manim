from manim import *

#Position object S

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position /  #circle is the reference point (middle), whatever picture then is right,left,up down
        self.play(Create(circle), Create(square))  # show the shapes on screen

        self.wait(3)