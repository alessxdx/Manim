from manim import *

#Creating Getters 

#always_redraw will make the arrow follow the shape when it moves
class Getters(Scene): 
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = always_redraw(
            lambda: Line(
            start=rect.get_bottom(), end=circ.get_top(),buff=0.5)
            .add_tip()
            )

        self.play(Create(VGroup(rect,circ,arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)
        self.wait()

      

