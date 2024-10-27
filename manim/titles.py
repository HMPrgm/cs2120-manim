from manim import *


class Main(Scene):
    def construct(self):
        text = Tex(r"Predicates", height=.5)
        text.to_edge(UP + LEFT)
        self.play(
            FadeIn(text)
        )
        self.wait()
        text2 = Tex(r"Quantifiers", height=.5)
        text2.to_edge(UP + LEFT)
        self.play(
            Transform(text,text2)
        )
        self.wait()
class Main2(Scene):
    def construct(self):
        text = Tex(r"Entailment", height=.5)
        text.to_edge(UP + LEFT)
        self.play(
            FadeIn(text)
        )
        self.wait()
        text2 = Tex(r"Relations", height=.5)
        text2.to_edge(UP + LEFT)
        self.play(
            Transform(text,text2)
        )
        self.wait()