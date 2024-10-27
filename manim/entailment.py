from manim import *

class Entailment1(Scene):
    def construct(self):
        t1 = Tex("Let $a,b$ be propositions",height =.6)
        s1 = MathTex(r"a\models b",height=1)
        
        t1.to_edge(UP*4)
        self.play(
            FadeIn(t1)
        )
        self.wait()
        self.play(
            FadeIn(s1)
        )
        self.wait()
class Entailment2(Scene):
    def construct(self):
        A_def = MathTex(r"A\subseteq\mathbb{N}, A\ne \emptyset",height =.6)
        s1 = MathTex(r"\forall n \in A.\text{IsPrime}(n)\models \exists n \in A.\text{IsPrime}(n)",height=.7)
        
        A_def.to_edge(UP)
        self.play(
            FadeIn(A_def)
        )
        self.wait()
        self.play(
            FadeIn(s1)
        )
        self.wait()