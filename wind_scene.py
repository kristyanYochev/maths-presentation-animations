from manimlib.imports import *
import os
import pyclbr


class WindScene(Scene):
    def construct(self):
        v = Vector(2.9 * UP)
        nm_text = TexMobject("N_{M}")
        nm_text.shift(3.1 * UP)

        self.play(Write(nm_text))
        self.play(ShowCreation(v))
        
