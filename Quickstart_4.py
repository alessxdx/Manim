from manim import *

class Picture(Scene):
    def construct(self):

        #adding image steps
        img = ImageMobject("media/images/5de63e00-8139-11e9-8828-a832c8cf2861.png")
        self.add(img)

        # #animating image to move
        img.generate_target().shift(LEFT * 3)
        self.play(MoveToTarget(img))


        # k = ValueTracker(0)

        # numPlane = NumberPlane()
        # self.add(numPlane)

        # ax1 = Axes()
        # self.add(ax1)

        # graph1 = ax1.plot(lambda x: np.cos(x))
        # self.add(graph1)

        # dot = always_redraw(Dot().move_to(ax1.c2p(k, graph1.underlying_function(k))))
        # dot = Dot().move_to(ax1.c2p(0, graph1.underlying_function(0)))
        # self.add(dot)

        # self.play(k.animate.set_value(3))