from manim import *


class Predicate2(Scene):
    def construct(self):
        text = Tex(r"$x$ is greater than $y$", height=1)
        self.play(
            FadeIn(text)
        )
        self.wait()
        transform_predicate = MathTex(r"G(x,y)", height=1)
        self.play(
            Transform(text, transform_predicate)
        )
        self.wait()
        
        predicate_true = MathTex(r"G(4,3)=\top", height=1)
        self.play(
            Transform(text, predicate_true)
        )
        self.wait()
        predicate_false = MathTex(r"G(5,7)=\bot", height=1)
        self.play(
            Transform(text, predicate_false)
        )
        self.wait()

class Predicate1(Scene):
    def construct(self):
        predicate = MathTex(r"Q(x)", height=1)
        self.play(
            FadeIn(predicate)
        )
        self.wait()
        transform_predicate = MathTex(r"Q(x)=\top\text{ or }\bot", height=1)
        self.play(
            Transform(predicate, transform_predicate)
        )
        self.wait()
        
        # title = Tex(r"This is some \LaTeX")
        # basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}") 
        # VGroup(title, basel).arrange(DOWN)
        # self.play(
        #     Write(title),
        #     FadeIn(basel, shift=UP),
        # )
        # self.wait()

        # transform_title = Tex("That was a transform")
        # transform_title.to_corner(UP + LEFT)
        # self.play(
        #     Transform(title, transform_title),
        #     LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        # )
        # self.wait()