from manim import *

class SuperpositionAnimation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-6, 6],
            y_range=[-2, 2],
            axis_config={"color": WHITE},
        )
        number_plane = NumberPlane()
        axes_labels = axes.get_axis_labels()

        # Create two  waves
        wave1 = axes.plot(lambda x: 1 * np.sin(x), color=BLUE)
        wave2 = axes.plot(lambda x: 0.5 * np.cos(x), color=GREEN)
        
        # labeling axis and graph
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        func_label_1 = MathTex("y={sin(x)}",color=BLUE).scale(0.75).move_to(RIGHT*2 + UP*1.75)
        func_label_2 = MathTex("y={0.5cos(x)}",color=GREEN).scale(0.75).move_to(RIGHT*3 +DOWN*1.25,)
        func_label_3 = MathTex("y={sin(x)+0.5cos(x)}",color=ORANGE).scale(0.75).move_to(RIGHT*2+UP*2)


        # Display the waves
        # self.add(number_plane)
        self.play(Create(VGroup(axes,labels)))
        self.play(Create(wave1,run_time=3),Create(wave2,run_time=3))
        self.play(Create(VGroup(func_label_1,func_label_2)))
        self.wait(1)

        # Create the combined wave
        combined_wave = axes.plot(lambda x: 1 * np.sin(x) + 0.5 * np.cos(x), color=ORANGE)
        
        # Display the combined wave
        self.play(FadeOut(VGroup(wave2,func_label_1,func_label_2)))
        self.play(Transform(wave1, combined_wave))
        self.play(Create(func_label_3))

        # Wait for a moment
        self.wait(2)


        
