from manimlib import *

class PiDay(Scene):
    def construct(self):
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
        self.wait()
