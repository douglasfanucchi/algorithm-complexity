from manim import *

class AlgorithmComplexity(Scene):
    def construct(self):
        numbers = [7, 6, 10, 25, 5, 11, 13, 18, 22, 0]
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

        equation = MathTex("1")
        equation.set_x(0.5)

        table = Table([
            ["0", "1", "0", "1"],
            ["\%", "", "0", "100"]],
            col_labels=[MathTex("n"), MathTex("f(n)"), MathTex("2n^2"), MathTex("1")],
            include_outer_lines=True,
            element_to_mobject=MathTex
        )

        self.play(self.hightlight([0], algorithm), FadeIn(equation))
        self.wait(1)
        self.play(self.hightlight([3, 14], algorithm), Transform(equation, MathTex("1 + 2n").set_x(0.5)))
        self.wait(1)
        self.play(self.hightlight([8, 9, 10], algorithm))
        self.wait(1)
        self.play(self.hightlight([8, 9, 10, 12], algorithm))
        self.wait(1)
        self.play(Transform(equation, MathTex("1 + 2n + 4 \cdot \sum_{k=1}^{n-1}k").set_x(0.5)))
        self.wait(1)
        self.play(FadeOut(lines), Transform(equation, MathTex("f(n) = 1 + 2n + 4 \cdot \\frac{(n)(n-1)}{2}").set_x(0.5)))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 2n^2 + 1")))
        self.wait(1)
        self.play(equation.animate.move_to([-4, 3, 0]))
        self.wait(1)
        self.play(table.create())
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

def f(n):
    return g(n) + h(n)

def g(n):
    return 2*n*n

def h(n):
    return 1
