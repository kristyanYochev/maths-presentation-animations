from manimlib.imports import *
import os
import pyclbr


class WindScene(Scene):
    def construct(self):
        magentic_north = Vector(3 * UP)
        magentic_north_label = TexMobject("N_{M}")
        magentic_north_label.move_to(magentic_north)

        self.play(ShowCreation(magentic_north))
        self.play(Write(magentic_north_label))

        gs_tip = 3.5 * RIGHT
        gs = Vector(gs_tip)
        gs_label = TexMobject("GS")
        gs_label.move_to(gs)

        self.play(ShowCreation(gs))
        self.play(Write(gs_label))

        tas_tip = normalize(np.array([1.5, 1, 0])) * 3
        tas = Vector(tas_tip)
        tas_label = TexMobject("TAS")
        tas_label.move_to(tas)

        self.play(ShowCreation(tas))
        self.play(Write(tas_label))

        wind_tip = 3.5 * RIGHT - tas_tip
        wind = Vector(wind_tip)
        wind_label = TexMobject("W/V")
        wind_label.move_to(wind)  

        self.play(ShowCreation(wind))
        self.play(Write(wind_label))
        self.wait()

        new_wind = Vector(wind_tip)
        new_wind.shift(tas_tip)
        new_wind_label = TexMobject("W/V")
        new_wind_label.move_to(new_wind)

        self.play(Transform(wind, new_wind))
        self.play(Transform(wind_label, new_wind_label))
