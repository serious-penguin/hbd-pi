from manimlib import *
import os
import sys
import datetime

sys.path.append(".")
from pi_creature_animations import Blink
from pi_creature import Mortimer
from pi_creature import Randolph

class PiDay(Scene):
    def construct(self):

        randy = Randolph()
        self.play(FadeIn(randy))

        bubble = SpeechBubble(
            direction=RIGHT,
            height=2,
            width=3,
        )
        now = datetime.datetime.now()
        bubble.next_to(randy, UL, buff=0)
        bubble.write(r"Happy $\pi$ day " + str(now.year) + "   ")
        self.add(bubble)
        self.add(bubble.content)
        # self.add(randy)

        # self.play(randy.change, "pondering")
        for x in range(10):
            self.play(Blink(randy))
            self.wait(2)


        """
        grid = Tex(r"\pi").get_grid(20, 20, height=10)
        self.add(grid)

        # self.play(grid.animate.shift(LEFT))

        # The same applies for any method, including those setting colors.
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(RED, GREEN, BLUE))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # The method Mobject.apply_complex_function lets you apply arbitrary
        # complex functions, treating the points defining the mobject as
        # complex numbers.
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        # Even more generally, you could apply Mobject.apply_function,
        # which takes in functions form R^3 to R^3
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]), # i
                    p[1] + 0.5 * math.sin(p[0]), # j
                    p[2]  # k
                ]
            ),
            run_time=5,
        )
        """
        self.wait()
