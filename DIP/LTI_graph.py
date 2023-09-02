from manim import *

class LTI(Scene):
    def construct(self):
        # input axis
        axes1 = Axes(
            x_range=[0, 4],
            y_range=[0, 2],
            axis_config={"color": GREEN},
        )
        # impulse axis
        axes2 = Axes(
            x_range=[0, 4],
            y_range=[0, 2],
            axis_config={"color": WHITE},
        )
        # output axis
        axes3 = Axes(
            x_range=[0, 4],
            y_range=[0, 2],
            axis_config={"color": BLUE},
        )

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
        vg1.scale(0.5).shift(UP*2)
        vg2.scale(0.5).shift(DOWN*2)   
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
        
        self.play(Create(VGroup(impulse_signal,input_signal)))
        self.play(FadeOut(impulse_signal,input_signal,vg1,vg2),run_time=2)
        

    # Scene 2
        # labeling axis individually for output axis
        labels5 = Tex("y(t)").move_to(axes3).shift(UP*3, LEFT*5)
        labels6 = Tex("t").move_to(axes3).shift(DOWN*2.5, RIGHT*6)

        vg3 = VGroup(axes3,labels5,labels6)
        vg3.scale(0.75)
        self.add(vg3)
        self.wait(1)

        output_signal = axes3.plot_line_graph(
            x_values = [0, 1, 3],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)
        
        self.play(Create(output_signal,run_time=3))
        self.play(FadeOut(vg3,output_signal))

    # Scene 3
        self.add(vg1, vg2) 
        self.wait(2)

        input_delay = axes1.plot_line_graph(
            x_values =[1,1],
            y_values=[0,1],
        )
        
        self.play(Create(impulse_signal),Create(input_delay))
        self.wait()
        self.play(FadeOut(impulse_signal,input_delay,vg1,vg2))

    # Scene 4
        labels5 = Tex("y(t)").move_to(axes3).shift(UP*3, LEFT*5)
        labels6 = Tex("t").move_to(axes3).shift(DOWN*2, RIGHT*6)

        vg3.scale(0.9).shift(LEFT*0.5)
        self.add(vg3)
        self.wait(1)

        output_delay = axes3.plot_line_graph(
            x_values = [1, 2, 4],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)
        
        self.play(Create(output_delay,run_time=3))
        self.play(FadeOut(vg3,output_delay))