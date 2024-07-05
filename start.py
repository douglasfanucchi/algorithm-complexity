from manim import *

class AlgorithmComplexity(Scene):
    def construct(self):
        numbers = [7, 6, 10, 0, 5, 25, 13]
        matrix = IntegerMatrix([numbers])

        algorithm = Code(
            code='''int i = 0;
while (i < n)
{
    int j = i + 1;
    while (j < n)
    {
        if (arr[j] < arr[i])
        {
            int tmp = arr[j];
            arr[j] = arr[i];
            arr[i] = tmp;
        }
        j = j + 1;
    }
    i = i + 1;
}''',
            tab_width=4,
            line_spacing=1,
            background="rectangle",
            language="C",
            font="Monospace",
        )

        firstNumber = matrix[0][0]
        arrowI = Arrow(max_stroke_width_to_length_ratio=0, color=BLUE).set_x(firstNumber.get_x()).set_y(firstNumber.get_y() - 1).rotate(PI/2)
        arrowJ = Arrow(max_stroke_width_to_length_ratio=0, color=RED).set_x(firstNumber.get_x()).set_y(firstNumber.get_y() - 1).rotate(PI/2)

        self.add(arrowI, arrowJ)
        self.add(arrowI)
        self.play(FadeIn(matrix))
        self.wait(1)

        for i in range(len(numbers)):
            self.play(arrowI.animate.set_x(matrix[0][i].get_x()), run_time=0.3)
            for j in range(i, len(numbers)):
                self.play(arrowJ.animate.set_x(matrix[0][j].get_x()), run_time=0.3)
                if (matrix[0][j].get_value() < matrix[0][i].get_value()):
                    i_position = matrix[0][i].get_x()
                    j_position = matrix[0][j].get_x()
                    self.play(matrix[0][i].animate.set_x(j_position), matrix[0][j].animate.set_x(i_position), run_time=0.3)
                    tmp = matrix[0][i]
                    matrix[0][i] = matrix[0][j]
                    matrix[0][j] = tmp
        self.wait(1)

        self.remove(matrix, arrowI, arrowJ)

        algorithm.move_to([-5, 0, 0]);
        lines = VGroup()
        algorithm.scale(0.8)
        for line in algorithm.code:
            lines += line
            for letter in line:
                self.play(
                    FadeIn(letter , run_time=0.005),
                    run_time=0.008,
                )
        self.wait(1)
        equation = MathTex("1")
        equation.set_x(0.5)

        table = Table([
            ["0", "1", "0", "1"],
            ["\%", "", "0", "100"]],
            col_labels=[MathTex("n"), MathTex("f(n)"), MathTex("2n^2"), MathTex("1")],
            include_outer_lines=True,
            element_to_mobject=MathTex
        )

        bigODefinition = MathTex("\exists c, N > 0 \mid \\forall n \geq N, f(n) \leq c \cdot g(n) \Rightarrow f(n) = \mathcal{O}(g(n))")

        self.play(self.hightlight([0], algorithm), FadeIn(equation))
        self.wait(1)
        self.play(self.hightlight([3, 14], algorithm))
        self.wait(1)
        self.play(Transform(equation, MathTex("1 + 2n").set_x(0.5)))
        self.wait(1)
        self.play(self.hightlight([8, 9, 10], algorithm))
        self.wait(1)
        self.play(self.hightlight([8, 9, 10, 12], algorithm))
        self.wait(1)
        self.play(Transform(equation, MathTex("1 + 2n + 4 \cdot \sum_{j=1}^{n-1}j").set_x(0.5)))
        self.wait(1)
        self.play(FadeOut(lines), Transform(equation, MathTex("f(n) = 1 + 2n + 4 \cdot \\frac{n(n-1)}{2}").set_x(0.5)))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 1 + 2n + 2 \cdot n(n-1)")))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 1 + 2n + 2 (n^2 - n)")))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 1 + 2n + 2n^2 - 2n")))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 1 + 2n^2")))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 2n^2 + 1")))
        self.wait(1)
        self.play(equation.animate.move_to([-4, 3, 0]))
        self.play(table.create())
        self.wait(1)
        i = 1
        while i <= 60:
            self.play([replace_in_table(table, 1, 0, MathTex(i)),
                        replace_in_table(table, 1, 1, MathTex(f(i))),
                        replace_in_table(table, 1, 2, MathTex(g(i))),
                        replace_in_table(table, 1, 3, MathTex(h(i))),
                        replace_in_table(table, 2, 2, MathTex("{:.2f}".format(g(i)/f(i) * 100))),
                        replace_in_table(table, 2, 3, MathTex(float("{:.2f}".format(h(i)/f(i) * 100))))
                    ], run_time=1)
            self.wait(4 if i == 1 else 2)
            i += 10 if i != 1 else 9

        self.play(equation.animate.move_to(ORIGIN), FadeOut(table))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 2n^2")))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = n^2")))
        self.wait(1)
        self.remove(equation)
        self.play(Create(bigODefinition), run_time=1.5)
        self.wait(1)

        equation = MathTex("f(n) = 2n^2 + 1")
        equation.move_to([-5, 2, 0])
        bigORelation = MathTex("f(n) = \mathcal{O}(g(n))")
        bigORelation.move_to([-5, 1, 0])
        resolution = MathTex("f(n) \leq c \cdot g(n)")

        self.play(bigODefinition.animate.move_to([-1, 3, 0]))
        self.play(Create(equation))
        self.wait(1)
        self.play(Create(bigORelation))
        self.wait(1)
        self.play(Transform(bigORelation, MathTex("f(n) = \mathcal{O}(n^2)").move_to([-5.2, 1, 0])))
        self.wait(1)
        self.play(Create(resolution))
        self.wait(1)
        self.play(Transform(resolution, MathTex("2n^2 + 1 \leq c \cdot n^2")))
        self.wait(1)
        self.play(Transform(resolution, MathTex("\\frac{2n^2 + 1}{n^2} \leq c")))
        self.wait(1)
        self.play(Transform(resolution, MathTex("2 + \\frac{1}{n^2} \leq c")))
        self.wait(1)
        i = 1
        N = MathTex("n = 1").move_to([0, -1, 0])
        self.play(Create(N))
        self.wait(1)
        while i <= 10:
            result = leftExpression(i)
            self.play([Transform(N, MathTex("n = " + str(i)).replace(N, dim_to_match=1)),
                       Transform(resolution, MathTex("{:.3f}".format(result) + "\leq c"))
                    ])
            if i == 0:
                self.wait(2)
            if i == 1:
                self.wait(1)
            i += 1
        self.wait(1)

        self.play([
            Transform(N, MathTex("n \\to +\infty").replace(N, dim_to_match=1)),
            Transform(resolution, MathTex("2 < c", font_size=60))
        ])
        self.wait(1)

        self.play(FadeOut(N), FadeOut(equation),
                  Transform(resolution, MathTex("2 + \\frac{1}{n^2} \leq c")),
                  FadeOut(bigORelation))
        self.wait(1)

        N = MathTex("n = 1").replace(N, dim_to_match=1)

        self.play(FadeIn(N), Transform(resolution, MathTex("2 + \\frac{1}{1^2} \leq c")))
        self.play(Transform(resolution, MathTex("2 + \\frac{1}{1} \leq c")))
        self.play(Transform(resolution, MathTex("2 + 1 \leq c")))
        self.play(Transform(resolution, MathTex("3 \leq c")))
        self.wait(1)

        bigORelation = MathTex("\\forall n \geq 1,\; 2n^2 + 1 \leq 3n^2 \Rightarrow f(n) = \mathcal{O}(n^2)")

        self.play(Transform(N, MathTex("N = 1").move_to([-6.175, 2, 0])),
                  Transform(resolution, MathTex("c = 3").move_to([-6.225, 1, 0])))
        self.wait(1)
        self.play(Create(bigORelation))
        self.wait(1)

        table = Table([["=1", "=2", "=3", "=4", "\cdots", "+\infty"],
                       ["\geq3", "\geq2.25", "\geq2.111...", "\geq2.0625", "\cdots", ">2"]],
                       row_labels=[MathTex("N"), MathTex("c")],
                       include_outer_lines=True,
                       element_to_mobject=MathTex
                    ).scale(0.8)
        self.play(FadeOut(bigODefinition), FadeOut(resolution), FadeOut(bigORelation), FadeOut(N))
        self.play(Create(table))

        self.wait(5)

    def hightlight(self, indexes, algorithm):
        animations = []
        for i, line in enumerate(algorithm.code):
            if i in indexes:
                animations += [line.animate.set_opacity(1)]
            else:
                animations += [line.animate.set_opacity(0.3)]
        return animations

def replace_in_table(table, row, col, new_element):
    mobj = table.get_rows()[row][col]
    new_element.move_to(mobj)
    return Transform(mobj, new_element)

# class Test(Scene):
#     def construct(self):
#         equation = MathTex("2 + \\frac{1}{n^2} \leq c")
#         self.add(equation)
#         i = 1
#         n = MathTex("n = 1").move_to([0, -1, 0])
#         while i <= 10:
#             self.play([
#                 Transform(n, MathTex("n = " + str(i)).replace(n, dim_to_match=1)),
#                 Transform(equation, MathTex("{:.11f}".format(leftExpression(i)) + "\leq c"))
#             ])
#             i+=1

def leftExpression(n):
    return 2 + 1/n**2

def f(n):
    return g(n) + h(n)

def g(n):
    return 2*n*n

def h(n):
    return 1
