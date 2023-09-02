from manim import *

class LTI(Scene):
    def construct(self):
        # Create axes
        axes1 = Axes(
            x_range=[0, 3],
            y_range=[0, 2],
            axis_config={"color": GREEN},
        )
        axes2 = Axes(
            x_range=[0, 3],
            y_range=[0, 2],
            axis_config={"color": WHITE},
        )
        axes3 = Axes(
            x_range=[0, 3],
            y_range=[0, 2],
            axis_config={"color": BLUE},
        )

        # number_plane = NumberPlane()

        # !!!!!!!!!!!!!!!!!!! CHANGED THIS
        # labels1 = axes1.get_axis_labels(y_label="x(t)")
        # labels2 = axes1.get_axis_labels(x_label="t")
        # !!!!!!!!!!!!!!!!!!! TO THIS
        labels1 = Tex("x(t)").move_to(axes1).shift(UP*3, LEFT*5)
        labels2 = Tex("t").move_to(axes1).shift(DOWN*2.5, RIGHT*6)
        # !!!!!!!!!!!!!!!!!!! If you want to position your axes labels separately this is how you can do it :)

        labels3 = axes2.get_axis_labels(Tex("t"), Tex("y(t)"))
        # labels3 = axes2.get_axis_labels(y_label="h(t)")
        # labels4 = axes2.get_axis_labels(x_label="t")
        labels5 = axes3.get_axis_labels(x_label="t",y_label="y(t)")

        # ADDED THIS 
        vg1 = VGroup(axes1, labels1, labels2) # We group the axes and labels together
        vg2 = VGroup(axes2, labels3)
        vg3 = VGroup(axes3, labels5)
        # self.add(number_plane)

        # !!!!!!!!!!!!!!!!!!! CHANGED THIS CODE
        # self.add(axes1.move_to(DOWN).scale(0.5).shift(UP*3),axes2.move_to(UP).scale(0.5).shift(DOWN*3))
        # self.add(labels1.shift(RIGHT*1.75))
        # self.add(labels2.shift(UL*3))
        # !!!!!!!!!!!!!!!!!!! TO THIS
        vg1.scale(0.5).shift(UP*2)
        vg2.scale(0.5).shift(DOWN*2)   
        self.add(vg1, vg2)    
        # !!!!!!!!!!!!!!!!!!! Doing the positioning and adding operations separately makes it more readable 

        # self.add(labels3.shift(DOWN*4 + RIGHT*1.75))
        # self.add(labels4.shift(UL*2))
        self.wait()

        impulse_signal = axes2.plot_line_graph(x_values=[0,0], y_values=[0,1])
        input_signal = axes1.plot_line_graph(
            x_values = [0, 1, 3],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)
        

        self.play(Create(impulse_signal),Create(input_signal))
        self.play(FadeOut(VGroup(impulse_signal,input_signal,axes1,axes2,labels1,labels2,labels3)),run_time=2)
        self.wait(1)

        output_signal = axes3.plot_line_graph(
            x_values = [0, 1, 3],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)
        
        self.add(axes3.scale(0.5))
        self.add(labels5)
        self.wait(1)
        self.play(Create(output_signal.scale(0.5),run_time=3))
        self.play(FadeOut(axes3,labels5,output_signal))

        input_delay =  axes1.plot_line_graph(
            x_values = [1, 1, 3],
            y_values = [0, 1, 0],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,)

        # self.add(axes1.move_to(DOWN).scale(0.5).shift(UP*3),axes2.move_to(UP).scale(0.5).shift(DOWN*3))
        # self.add(labels1.shift(RIGHT*1.75))
        # self.add(labels2.shift(UL*3))
        # self.add(labels3.shift(DOWN*4 + RIGHT*1.75))
        # self.add(labels4.shift(UL*2))    
        # self.wait()

        # self.play(Create(impulse_signal),Create(input_delay))

