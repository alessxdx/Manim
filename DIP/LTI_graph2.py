from manim import *

class LTI(Scene):
    def construct(self):
        # input axis
        axes1 = Axes(
            x_range=[0, 4],
            y_range=[0, 2],
            axis_config={"color": GREEN},
        ).add_coordinates()

        # impulse axis
        axes2 = Axes(
            x_range=[0, 4],
            y_range=[0, 2],
            axis_config={"color": WHITE},
        ).add_coordinates()

        # output axis
        axes3 = Axes(
            x_range=[0, 4],
            y_range=[0, 2],
            axis_config={"color": BLUE},
        ).add_coordinates()

        # number_plane = NumberPlane()
        # self.add(number_plane)

    # Scene 1 
        # labeling axis individually for input axis
        labels1 = Tex("x(t)").move_to(axes1).shift(UP*3, LEFT*5)
        labels2 = Tex("t").move_to(axes1).shift(DOWN*2.5, RIGHT*6)

        # labeling axis individually for impulse axis
        labels3 = Tex("h(t)").move_to(axes2).shift(UP*3, LEFT*5)
        labels4 = Tex("t").move_to(axes2).shift(DOWN*2.5, RIGHT*6)
        

        # We group the axes and labels together, scale and add
        vg1 = VGroup(axes1, labels1, labels2) 
        vg2 = VGroup(axes2, labels3,labels4)
        vg1.scale(0.45).shift(UP*2)
        vg2.scale(0.45).shift(DOWN*2)   
        self.add(vg1, vg2) 
        self.wait(2)
        

        # Creating impulse h(t) & input x(t) signal
        input_signal = axes1.plot_line_graph(x_values=[0,0], y_values=[0,1])
        impulse_signal = axes2.plot_line_graph(
            x_values = [0, 1, 3],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)
        
        a1 = Arrow(start=LEFT, end=RIGHT, buff=1.5,color=BLUE).shift(LEFT*0.5)
        a1.shift(RIGHT*0.25)

        # labeling axis individually for output axis
        labels5 = Tex("y(t)").move_to(axes3).shift(UP*3, LEFT*5)
        labels6 = Tex("t").move_to(axes3).shift(DOWN*2.5, RIGHT*6)

        vg3 = VGroup(axes3,labels5,labels6)
        vg3.scale(0.45).shift(RIGHT*4.2)
       
        output_signal = axes3.plot_line_graph(
            x_values = [0, 1, 3],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)

        eq = MathTex('x(t)*h(t)=y(t)')
        eq.shift(UP*0.5+LEFT*0.25).scale(0.6)

        self.play(Create(VGroup(input_signal,impulse_signal),run_time=5))
        self.wait(2)
        self.play(VGroup(impulse_signal,input_signal,vg1,vg2).animate.shift(LEFT*4))
        self.play(GrowArrow(a1))
        self.add(eq)
        self.add(vg3)
        self.wait(2)
        self.play(Create(output_signal,run_time=5))
        self.play(FadeOut(impulse_signal,input_signal,output_signal,vg1,vg2,vg3,a1,eq),run_time=2)

        
    #  Scene 2
        self.play(FadeIn(vg1, vg2))
        self.wait(2)

        input_delay = axes1.plot_line_graph(
            x_values =[1,1],
            y_values=[0,1],
        )
        
        eq = MathTex('x(t-1)*h(t)=y(t-1)')
        eq.shift(UP*0.3+LEFT*0.25).scale(0.45)
        
        output_delay = axes3.plot_line_graph(
            x_values = [1, 2, 4],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)
        
        self.play(Create(impulse_signal),Create(input_delay),run_time=5)
        self.wait()
        self.play(GrowArrow(a1))
        self.add(eq)
        self.add(vg3)
        self.wait(2)
        self.play(Create(output_delay,run_time=5))
        self.play(FadeOut(impulse_signal,input_delay,output_delay,vg1,vg2,vg3,a1,eq),run_time=2)
