from manim import *

class LTI(Scene):
    def construct(self):
        Func1 = MathTex("x(t)")
        Func2 = MathTex("y(t)")
        rectangle = Rectangle(color = RED)
        a1 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a2 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        group1 = VGroup(Func1, a1, rectangle, a2, Func2).arrange(RIGHT, buff=0.5)
        Func3 = MathTex("x(t)")
        Func4 = MathTex("y(t)")
        rectangle2 = Rectangle(color = RED)
        a3 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a4 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        group2 = VGroup(Func3, a3, rectangle2, a4, Func4).arrange(RIGHT, buff=0.5).shift(LEFT * 2, UP * 2).scale(0.5)
        self.add(rectangle)
        self.play(Write(Func1))
        self.play(GrowArrow(a1))
        self.play(GrowArrow(a2))
        self.play(Write(Func2))
        self.wait()
        self.play(Transform(group1, group2))

        Func1_delay = MathTex("x1(t)=x(t-T)")
        Func2_delay = MathTex("y1(t)=y(t-T)")
        rectangle3 = Rectangle(color = RED)
        a5 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a6 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        group3 = VGroup(Func1_delay, a5, rectangle3, a6, Func2_delay).arrange(RIGHT, buff=0.5).scale(0.75)
        animations = [ FadeIn(group3),]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))
        self.wait()