from manim import *

class Quantifiers1(Scene):
    def construct(self):
        n_def = MathTex(r"n\in\mathbb{R}", height=1)
        
        self.play(
            FadeIn(n_def)
        )
        self.wait() 
        n_plus_1_greater = MathTex(r"n+1>n",height=1)
        self.play(
            Transform(n_def,n_plus_1_greater)
        )
        self.wait() 
        n_predicate = MathTex(r"G(n+1,n)",height=1)
        self.play(
            Transform(n_def,n_predicate)
        )
        self.wait() 
class Quantifiers2(Scene):
    def construct(self):
        n_def = MathTex(r"\forall", height=1)
        
        self.play(
            FadeIn(n_def)
        )
        self.wait() 
        n_def_2 = MathTex(r"\forall n \in \mathbb{R}.G(n+1,n)", height=1)
        
        self.play(
            Transform(n_def,n_def_2)
        )
        self.wait() 
class Quantifiers3(Scene):
    def construct(self):
        n_def = Tex(r"$\forall x\in X$ checks some condition for every $x\in X$")
        
        self.play(
            FadeIn(n_def)
        )
        self.wait() 
        
class Quantifiers4(Scene):
    def construct(self):
        n_def = Tex(r"$\exists x\in X$ checks some condition for at least 1 $x\in X$")
        
        self.play(
            FadeIn(n_def)
        )
        self.wait() 
class IsPrime1(Scene):
    def construct(self):
        n_def = Tex(r"$\text{IsPrime}(x)$")
        
        self.play(
            FadeIn(n_def)
        )
        self.wait() 
        n_def2 = Tex(r"$\text{IsPrime}(x)=x \text{ is a prime number}$")
        
        self.play(
            Transform(n_def,n_def2)
        )
        self.wait() 
class IsPrime2(Scene):
    def construct(self):
        n_def = Tex(r"$\exists x\in A.\text{IsPrime}(x)$", height=.9)
        n_def1 = Tex(r"$\exists x\in A.\text{IsPrime}(x)=\top$", height=.9)
        n_def2 = Tex(r"$\exists x\in A.\text{IsPrime}(x)=\bot$", height=.9)
        A_def_1 = MathTex(r"A=\{4,6,8\}",height = .8) 
        A_def_2 = MathTex(r"A=\{2,4,6,8\}",height = .8) 
        VGroup(n_def,A_def_1).arrange(DOWN)
        VGroup(n_def2,A_def_1).arrange(DOWN)
        VGroup(n_def1,A_def_2).arrange(DOWN)
        self.play(
            FadeIn(n_def)
        )
        self.wait()
        
        self.play(
            Transform(n_def,n_def2),
            FadeIn(A_def_1)
        )
        self.wait()
        self.play(
            Transform(n_def,n_def1),
            Transform(A_def_1,A_def_2)
        )
        self.wait()

class AndOrs1(Scene):
    def construct(self):
        set_A = MathTex(r"A=\{2,3,5,7\}",height=.7)
        forAllCase = MathTex(r"\forall x\in A.\text{IsPrime}(x)",height=.7)
        forAllCaseEq = MathTex(r"\forall x\in A.\text{IsPrime}(x)\equiv",height=.7)
        andCase = MathTex(r"\text{IsPrime}(2)\land\text{IsPrime}(3)\land\text{IsPrime}(5)\land\text{IsPrime}(7)",height =.6)
        VGroup(forAllCase,andCase).arrange(DOWN)
        VGroup(forAllCaseEq,andCase).arrange(DOWN)
        # VGroup(n_def2,A_def_1).arrange(DOWN)
        # VGroup(n_def1,A_def_2).arrange(DOWN)
        self.play(
            FadeIn(set_A)
        )
        self.wait()
        self.play(
            FadeOut(set_A),
            FadeIn(forAllCase)
            
        )
        self.wait()
        self.play(
            Transform(forAllCase,forAllCaseEq),
            FadeIn(andCase)
            
        )
        self.wait()

class AndOrs2(Scene):
    def construct(self):
        existsCaseEq = MathTex(r"\exists x\in A.\text{IsPrime}(x)\equiv",height=.7)
        orCase = MathTex(r"\text{IsPrime}(2)\lor\text{IsPrime}(3)\lor\text{IsPrime}(5)\lor\text{IsPrime}(7)",height =.6)
        VGroup(existsCaseEq,orCase).arrange(DOWN)
        # VGroup(n_def2,A_def_1).arrange(DOWN)
        # VGroup(n_def1,A_def_2).arrange(DOWN)
        self.play(
            FadeIn(existsCaseEq),
            FadeIn(orCase)
            
        )
        self.wait()
        
class MovieEx1(Scene):
    def construct(self):
        likesMovie = MathTex(r"\text{LikesMovie(s,m)} = s \text{ likes to watch }m",height=.7)
        hatesMovie = MathTex(r"\text{HatesMovie(s,m)} = s \text{ absolutely hates }m",height=.7)
        VGroup(likesMovie,hatesMovie).arrange(DOWN)
        # VGroup(n_def2,A_def_1).arrange(DOWN)
        # VGroup(n_def1,A_def_2).arrange(DOWN)
        self.play(
            FadeIn(likesMovie)
        )
        self.wait()
        self.play(
            FadeIn(hatesMovie)
        )
        self.wait()
        
class MovieEx2(Scene):
    def construct(self):
        S = MathTex(r"S = \text{Discrete Math Students}",height=.5)
        M = MathTex(r"M = \text{Movies}",height=.5)
        VGroup(S,M).arrange(DOWN)
        # VGroup(n_def2,A_def_1).arrange(DOWN)
        # VGroup(n_def1,A_def_2).arrange(DOWN)
        self.play(
            FadeIn(S)
        )
        self.wait()
        self.play(
            FadeIn(M)
        )
        self.wait()
class MovieEx3(Scene):
    def construct(self):
        s1 = MathTex(r"1. ~\forall s\in S.~\exists m\in M.~\text{LikesMovie(s,m)}",height=.54)
        s2 = MathTex(r"2. ~\exists m\in M.~\forall s\in S.~\text{LikesMovie(s,m)}",height=.54)
        s3 = MathTex(r"3.~ \exists s\in S.~\forall m\in M.~\text{LikesMovie(s,m)}",height=.54)
        s4 = MathTex(r"4. ~\exists s\in S.~\exists m\in M.~\text{HatesMovie(s,m)}",height=.54)
        s5 = MathTex(r"5. ~\exists s\in S.~\forall m\in M.~\lnot\text{HatesMovie(s,m)}",height=.54)
        
        VGroup(s1,s2,s3,s4,s5).arrange(DOWN,aligned_edge=LEFT,buff=.4)
        # VGroup(n_def1,A_def_2).arrange(DOWN)
        self.play(
            FadeIn(s1),
            FadeIn(s2),
            FadeIn(s3),
            FadeIn(s4),
            FadeIn(s5),
        )
        self.wait()
class MovieEx4(Scene):
    def construct(self):
        s1 = MathTex(r"\forall s\in S.~\exists m\in M.~\text{LikesMovie(s,m)}",height=.8)
        t1 = Text("\"Every student likes some movie\"")
        VGroup(s1,t1).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(s1)
        )
        self.wait()
        self.play(
            FadeIn(t1)
        )
        self.wait()
class MovieEx5(Scene):
    def construct(self):
        s1 = MathTex(r"\exists m\in M.~\forall s\in S.~\text{LikesMovie(s,m)}",height=.8)
        t1 = Text("\"There's a movie everyone likes\"")
        VGroup(s1,t1).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(s1)
        )
        self.wait()
        self.play(
            FadeIn(t1)
        )
        self.wait()
class MovieEx6(Scene):
    def construct(self):
        s1 = MathTex(r"\exists s\in S.~\forall m\in M.~\text{LikesMovie(s,m)}",height=.8)
        t1 = Text("\"Some student likes all movies\"")
        VGroup(s1,t1).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(s1)
        )
        self.wait()
        self.play(
            FadeIn(t1)
        )
        self.wait()
class MovieEx7(Scene):
    def construct(self):
        s1 = MathTex(r"\exists s\in S.~\exists m\in M.~\text{HatesMovie(s,m)}",height=.8)
        t1 = Text("\"Some student hates some movie\"")
        VGroup(s1,t1).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(s1)
        )
        self.wait()
        self.play(
            FadeIn(t1)
        )
        self.wait()
class MovieEx8(Scene):
    def construct(self):
        s1 = MathTex(r"\exists s\in S.~\forall m\in M.~\lnot\text{HatesMovie(s,m)}",height=.8)
        t1 = Text("\"Some student doesn’t hate any movies\"")
        VGroup(s1,t1).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(s1)
        )
        self.wait()
        self.play(
            FadeIn(t1)
        )
        self.wait()
class DeMorgan1(Scene):
    def construct(self):
        
        t1 = Tex(r"There exists a number in the set $\{2, 4, 6\}$ which is not prime",height=.4)
        t2 = Tex(r"It is not the case that every number in the set $\{2, 4, 6\}$ is prime",height=.4)
        VGroup(t1,t2).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(t1)
        )
        self.wait()
        self.play(
            FadeIn(t2)
        )
        self.wait()
        defA=MathTex(r"A=\{2,4,6\}")
        defA.to_edge(UP)
        self.play(
            FadeIn(defA)
        )
        self.wait()
        
        s1 = MathTex(r"\exists n\in A. \lnot \text{IsPrime}(n)",height=.7)
        s2 = MathTex(r"\lnot\forall n\in A. \text{IsPrime}(n)",height=.7)
        VGroup(s1,t2).arrange(DOWN,buff=.4)
        VGroup(t1,s2).arrange(DOWN,buff=.4)
        self.play(
            Transform(t1,s1)
        )
        self.wait()
        self.play(
            Transform(t2,s2)
        )
        self.wait()
class DeMorgan2(Scene):
    def construct(self):
        t1 = Text("DeMorgan's Law")
        s1 = MathTex(r"\lnot a\lor \lnot b\equiv \lnot(a \land b)",height=.8)
        
        t1.to_edge(UP)
        self.play(
            FadeIn(t1)
        )
        self.wait()
        self.play(
            FadeIn(s1)
        )
        self.wait()
class DeMorgan3(Scene):
    def construct(self):
        s1 = MathTex(r"\exists n\in A. \lnot \text{IsPrime}(n)",height=.7)
        s11 = MathTex(r"\exists n\in A. \lnot \text{IsPrime}(n)",height=.7)
        o1 = MathTex(r"\lnot\text{IsPrime}(2)\lor\lnot\text{IsPrime}(4)\lor\lnot\text{IsPrime}(6)",height=.7)
        o11 = MathTex(r"\lnot\text{IsPrime}(2)\lor\lnot\text{IsPrime}(4)\lor\lnot\text{IsPrime}(6)",height=.7)
        o2 = MathTex(r"\lnot(\text{IsPrime}(2)\land\text{IsPrime}(4)\land\text{IsPrime}(6))",height=.7)
        o22 = MathTex(r"\lnot(\text{IsPrime}(2)\land\text{IsPrime}(4)\land\text{IsPrime}(6))",height=.7)
        s2 = MathTex(r"\lnot\forall n\in A. \text{IsPrime}(n)",height=.7)
        eq = MathTex(r"\equiv",height=.4)
        VGroup(s1,eq,o1).arrange(DOWN,buff=.4)
        # VGroup(o1,eq,o2).arrange(DOWN,buff=.4)
        # VGroup(o2,eq,s2).arrange(DOWN,buff=.4)
        # VGroup(s1,eq,s2).arrange(DOWN,buff=.4)
        self.play(
            FadeIn(s1),
            FadeIn(eq),
            FadeIn(o1)
        )
        self.wait()
        VGroup(o11,eq,o2).arrange(DOWN,buff=.4)

        self.play(
            Transform(s1,o11),
            Transform(o1,o2)
        )
        self.wait()
        VGroup(o22,eq,s2).arrange(DOWN,buff=.4)

        self.play(
            Transform(s1,o22),
            Transform(o1,s2)
        )
        self.wait()
        VGroup(s11,eq,s2).arrange(DOWN,buff=.4)

        self.play(
            Transform(s1,s11)
        )
        self.wait()
        # VGroup(s1,eq,o1).arrange(DOWN,buff=.4)
        # self.play(
        #     FadeIn(s1),
        #     FadeIn(eq),
        #     FadeIn(o1)
        # )
        # self.wait()
        # VGroup(s1,eq,o1).arrange(DOWN,buff=.4)
        # self.play(
        #     FadeIn(s1),
        #     FadeIn(eq),
        #     FadeIn(o1)
        # )
        # self.wait()
class DeMorgan4(Scene):
    def construct(self):
        t1 = Text("DeMorgan's Laws for Quantifiers")
        s1=MathTex(r"\exists x\in A.\lnot Q(x)\equiv\lnot\forall x\in A. Q(x)",height=.7)
        s2=MathTex(r"\forall x\in A.\lnot Q(x)\equiv\lnot\exists x\in A. Q(x)",height=.7)
        VGroup(s1,s2).arrange(DOWN,buff=.6)
        t1.to_edge(UP)
        self.play( FadeIn(t1))
        self.wait()
        self.play(
            FadeIn(s1),
            FadeIn(s2)
        )
        self.wait()
        