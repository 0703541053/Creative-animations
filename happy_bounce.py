from manim import *

class HappyBounce(Scene):
    def construct(self):
        # Create a happy bouncing ball
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1)
        
        # Add face details
        smile = Arc(angle=PI, radius=0.3, color=YELLOW).shift(0.3*DOWN)
        eyes = VGroup(
            Dot(0.2*LEFT + 0.2*UP, color=WHITE),
            Dot(0.2*RIGHT + 0.2*UP, color=WHITE)
        )
        face = VGroup(ball, smile, eyes)
        
        # Animate it
        self.play(Create(face))
        self.play(face.animate.shift(UP*2), rate_func=there_and_back)
        self.play(face.animate.scale(1.2), rate_func=there_and_back)
        self.wait()