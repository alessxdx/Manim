from manim import *

class ConvolutionSumAnimation(Scene):
    def construct(self):
        # Define input signals
        f = [0, 1, 2, 1, 0]  # Example signal f[n]
        g = [1, -1, 2]       # Example signal g[n]

        # Calculate convolution sum
        conv_result = [0] * (len(f) + len(g) - 1)

        for n in range(len(conv_result)):
            for k in range(len(g)):
                if n - k >= 0 and n - k < len(f):
                    conv_result[n] += f[n - k] * g[k]

        # Create axes
        axes = Axes(
            x_range=(-0.5, len(conv_result) - 1 + 0.5),
            y_range=(-2, 6),
            axis_config={"color": BLUE},
        )

        # Create plot for the convolution result
        plot_conv = axes.plot(lambda x: conv_result[int(x)])

        # Display convolution result plot
        self.play(Create(axes), Create(plot_conv))
        self.wait()
