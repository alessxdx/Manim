from manim import *

class Superpos(Scene):
    def construct(self):
        x1 = MathTex("x1(t)")
        x2 = MathTex("x2(t)")
        a1 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a2 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a3 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a4 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        y1 = MathTex("y1(t)")
        y2 = MathTex("y2(t)")
        rec1 = Rectangle(color=RED)
        rec2 = Rectangle(color=RED)
        group1 = VGroup(x1, a1, rec1, a2, y1).arrange(RIGHT, buff=0.5).shift(LEFT*3, UP*2).scale(0.50)
        group2 = VGroup(x2, a3, rec2, a4, y2).arrange(RIGHT, buff=0.5).shift(RIGHT*3, UP*2).scale(0.50)
        self.play(Write(x1))
        self.play(GrowArrow(a1))
        self.play(FadeIn(rec1))
        self.play(GrowArrow(a2))
        self.play(Write(y1))
        self.play(Write(x2))
        self.play(GrowArrow(a3))
        self.play(FadeIn(rec2))
        self.play(GrowArrow(a4))
        self.play(Write(y2))

        x3 = MathTex("x3(t)=a1x1(t)+a2x2(t)")
        y3 = MathTex("y3(t)=a1y1(t)+a2y2(t)")
        rec3 = Rectangle(color=RED)
        a5 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        a6 = Arrow(start=LEFT, end=RIGHT, color=WHITE)
        group3 = VGroup(x3, a5, rec3, a6, y3).arrange(RIGHT, buff=0.5).shift(DOWN*2).scale(0.60)
        animations = [ FadeIn(group3), ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))
        self.wait(2)
        
