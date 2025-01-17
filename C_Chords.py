from manim import *

class CMajorChords(Scene):
    def construct(self):
        # USE THE SAME TEXTEMPLATE OBJECT FOR MUSIXTEX
        musixtex = TexTemplate()
        musixtex.add_to_preamble(r"\usepackage{musixtex}")
        
        
        # C MAJOR
        cmajor = Tex(r"""
        \begin{music}
           \instrumentnumber{1}
           \setstaffs1{1}
           \startextract
              \Notes
              \zw{c e g} \en \endpiece
           \zendextract
        \end{music}
        """, tex_template=musixtex).scale(2)
        cmajortext = Text("CM - C Major/Dominant (I-III-V)", font="Zekton").scale(1.4).shift(UP*3)
        self.play(Write(cmajor))
        self.wait(2)
        self.play(Write(cmajortext))
        self.wait()


        # C MINOR
        cminor = Tex(r"""
        \begin{music}
           \instrumentnumber{1}
           \setstaffs1{1}
           \startextract
              \Notes
              \zwh{c ^e g} \en \endpiece
           \zendextract
        \end{music}
        """, tex_template=musixtex).scale(2)
        cminortext = Text("Cm - C Minor (I-bIII-V)", font="Zekton").scale(1.4).shift(UP*3)
        
        
        self.play(FadeOut(cmajor), FadeOut(cmajortext))
        self.wait(1)
        self.play(Write(cminor))
        self.wait()
        self.play(Write(cminortext))
        self.wait(2)
        
        # C5
        c5 = Tex(r"""
        \begin{music}
           \instrumentnumber{1}
           \setstaffs1{1}
           \startextract
              \Notes
              \zwh{c g} \en \endpiece
           \zendextract
        \end{music}
        """, tex_template=musixtex).scale(2)
        c5text = Text("C5 - C Power Chord (I-V)", font="Zekton").scale(1.4).shift(UP*3)
        
        
        self.play(FadeOut(cminor), FadeOut(cminortext))
        self.wait(1)
        self.play(Write(c5))
        self.wait()
        self.play(Write(c5text))
        self.wait(2)
        
        # Co
        co = Tex(r"""
        \begin{music}
           \instrumentnumber{1}
           \setstaffs1{1}
           \startextract
              \Notes
               \zwh{c _e _g} \en \endpiece
           \zendextract
        \end{music}
        """, tex_template=musixtex).scale(2)
        cotext = Text("Co - C Diminished (I-bIII-bV)", font="Zekton").scale(1.4).shift(UP*3)
        
        
        self.play(FadeOut(c5), FadeOut(c5text))
        self.wait(1)
        self.play(Write(co))
        self.wait()
        self.play(Write(cotext))
        self.wait(2)
        
        # C+
        cplus = Tex(r"""
        \begin{music}
           \instrumentnumber{1}
           \setstaffs1{1}
           \startextract
              \Notes
               \zwh{c e ^g} \en \endpiece
           \zendextract
        \end{music}
        """, tex_template=musixtex).scale(2)
        cplustext = Text("C+ - C Augmented(I-III-#V)", font="Zekton").scale(1.4).shift(UP*3)
        
        
        self.play(FadeOut(co), FadeOut(cotext))
        self.wait(1)
        self.play(Write(cplus))
        self.wait()
        self.play(Write(cplustext))
        self.wait(3)