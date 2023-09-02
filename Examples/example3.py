from manim import *

#Creating Getters ~ like arrows

#VGroup = Vector group (can put things and play tgt)
#buff is if you dont want the arrow to touch the shapes
class Getters(Scene): 
    def construct(self):

        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = Line(start=rect.get_bottom(), end=circ.get_top(),buff=0.5).add_tip()

        self.play(Create(VGroup(rect,circ,arrow)))
        self.wait()
        
        # this would only make the rectangle move but the arrow will stay
        self.play(rect.animate.to_edge(UR))

