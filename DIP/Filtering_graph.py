from manim import *

class filtering(Scene):
 def construct(self):
        # lowpass axis
        axes1 = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            axis_config={"color": GREEN},
        )

        # highpass axis
        axes2 = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            axis_config={"color": BLUE},
        )

        # bandpass axis
        axes3 = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            axis_config={"color": RED},
        )

         # bandstop axis
        axes4 = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            axis_config={"color": YELLOW},
        )


    # Scene 1 - displaying each graph individually
        # labeling axis individually for lowpass axis
        labels1 = MathTex("|H(w)|").move_to(axes1).shift(UP*3.5, LEFT*5)
        labels2 = MathTex("w").move_to(axes1).shift(DOWN*2.5, RIGHT*6.5)
        labels2_2 = axes1.x_axis.add_labels({1:MathTex("w_c")})
        # labeling axis individually for highpass axis
        labels3 = MathTex("|H(w)|").move_to(axes2).shift(UP*3.5, LEFT*5)
        labels4 = MathTex("w").move_to(axes2).shift(DOWN*2.5, RIGHT*6.5)
        labels4_2 = axes2.x_axis.add_labels({1:MathTex("w_c")})
        # labeling axis individually for bandpass axis
        labels5 = MathTex("|H(w)|").move_to(axes3).shift(UP*3.5, LEFT*5)
        labels6 = MathTex("w").move_to(axes3).shift(DOWN*2.5, RIGHT*6.5)
        labels6_2 = axes3.x_axis.add_labels({0.5:MathTex("w_1"), 1.5:MathTex("w_2")})
        # labeling axis individually for bandstop axis
        labels7 = MathTex("|H(w)|").move_to(axes4).shift(UP*3.5, LEFT*5)
        labels8 = MathTex("w").move_to(axes4).shift(DOWN*2.5, RIGHT*6.5)
        labels8_2 = axes4.x_axis.add_labels({0.5:MathTex("w_1"), 1.5:MathTex("w_2")})


        # We group the axes and labels togethe
        vg1 = VGroup(axes1, labels1, labels2, labels2_2) 
        vg2 = VGroup(axes2, labels3, labels4, labels4_2)
        vg3 = VGroup(axes3, labels5, labels6, labels6_2)
        vg4 = VGroup(axes4, labels7, labels8, labels8_2)
      

        # Heading/title
        h1 = Tex('Lowpass  filter')
        h1.shift(UP*2)
        h2 = Tex('Highpass  filter')
        h2.shift(UP*2)
        h3 = Tex('Bandpass  filter')
        h3.shift(UP*2)
        h4 = Tex('Bandstop  filter')
        h4.shift(UP*2)
        hgroup = VGroup(h1,h2,h3,h4)

        # Creating filters/graphs
        lowpass = axes1.plot(lambda x: 1 if x >= 0 and x <= 1 else 0 ,x_range=[0, 2, 0.001], use_smoothing=False, color=WHITE)
        highpass = axes2.plot(lambda x: 1 if x >= 1 else 0 ,x_range=[0, 2, 0.001], use_smoothing=False ,color=WHITE)
        bandpass = axes3.plot(lambda x: 1 if x >= 0.5 and x<= 1.5 else 0 ,x_range=[0, 2, 0.001], use_smoothing=False ,color=WHITE)
        bandstop = axes4.plot(lambda x: 0 if x >= 0.5 and x<= 1.5 else 1 ,x_range=[0, 2, 0.001], use_smoothing=False ,color=WHITE)

        # Creating area under graph
        area1 = axes1.get_area(lowpass,x_range=(0,1),color=PURPLE,opacity=0.3)
        area2 = axes2.get_area(highpass,x_range=(1,2),color=PURPLE,opacity=0.3)
        area3 = axes3.get_area(bandpass,x_range=(0.5,1.5),color=PURPLE,opacity=0.3)
        area4 = axes4.get_area(bandstop,x_range=(0,2),color=PURPLE,opacity=0.3)
        areagroup = VGroup(area1,area2,area3,area4)

        #Creating the scenes
        self.play(FadeIn(vg1))
        self.play(Create(lowpass),run_time=3)
        self.play(FadeIn(area1,h1))
        self.wait()
        self.play(FadeOut(vg1,lowpass,h1,area1))
        self.wait()

        self.play(FadeIn(vg2))
        self.play(Create(highpass),run_time=3)
        self.play(FadeIn(h2,area2))
        self.wait()
        self.play(FadeOut(vg2,highpass,h2,area2))
        self.wait()

        self.play(FadeIn(vg3))
        self.play(Create(bandpass),run_time=3)
        self.play(FadeIn(h3,area3))
        self.wait()
        self.play(FadeOut(vg3,bandpass,h3,area3))
        self.wait()

        self.play(FadeIn(vg4))
        self.play(Create(bandstop),run_time=3)
        self.play(FadeIn(h4,area4))
        self.wait()
        self.play(FadeOut(vg4,bandstop,h4,area4))
        self.wait()

    # Scene 2 - displaying all together
        vg1.scale(0.4).shift(UP*2,LEFT*4)
        vg2.scale(0.4).shift(DOWN*2,LEFT*4)   
        vg3.scale(0.4).shift(UP*2, RIGHT*2)
        vg4.scale(0.4).shift(DOWN*2,RIGHT*2)
        self.play(FadeIn(vg1, vg2, vg3, vg4))
        self.wait()
        
        h1.scale(0.5).shift(LEFT*3.6,UP*0.5)
        h2.scale(0.5).shift(LEFT*3.6,DOWN*3.5)
        h3.scale(0.5).shift(RIGHT*2.2,UP*0.5)
        h4.scale(0.5).shift(RIGHT*2.2,DOWN*3.5)

        lowpass = axes1.plot(lambda x: 1 if x >= 0 and x <= 1 else 0 ,x_range=[0, 2, 0.001], use_smoothing=False, color=WHITE)
        highpass = axes2.plot(lambda x: 1 if x >= 1 else 0 ,x_range=[0, 2, 0.001], use_smoothing=False ,color=WHITE)
        bandpass = axes3.plot(lambda x: 1 if x >= 0.5 and x<= 1.5 else 0 ,x_range=[0, 2, 0.001], use_smoothing=False ,color=WHITE)
        bandstop = axes4.plot(lambda x: 0 if x >= 0.5 and x<= 1.5 else 1 ,x_range=[0, 2, 0.001], use_smoothing=False ,color=WHITE)

        area1 = axes1.get_area(lowpass,x_range=(0,1),color=PURPLE,opacity=0.3)
        area2 = axes2.get_area(highpass,x_range=(1,2),color=PURPLE,opacity=0.3)
        area3 = axes3.get_area(bandpass,x_range=(0.5,1.5),color=PURPLE,opacity=0.3)
        area4 = axes4.get_area(bandstop,x_range=(0,2),color=PURPLE,opacity=0.3)
        areagroup = VGroup(area1,area2,area3,area4)
        
        self.play(Create(lowpass),Create(highpass),Create(bandpass),Create(bandstop),run_time=3)
        self.play(FadeIn(hgroup,areagroup))
        self.wait(2)
        

        
        