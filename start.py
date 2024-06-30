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

        self.play(lines.animate.set_y(-3), lines.animate.scale(0.7))
        self.play(self.hightlight([0], algorithm), FadeIn(equation))
        self.wait(1)
        self.play(self.hightlight([3, 14], algorithm), Transform(equation, MathTex("1 + 2n")))
        self.wait(1)
        self.play(self.hightlight([8, 9, 10], algorithm))
        self.wait(1)
        self.play(self.hightlight([8, 9, 10, 12], algorithm))
        self.wait(1)
        self.play(Transform(equation, MathTex("1 + 2n + 4 \cdot \sum_{k=1}^{n-1}k")))
        self.wait(1)
        self.play(FadeOut(lines), Transform(equation, MathTex("f(n) = 1 + 2n + 4 \cdot \\frac{(n)(n-1)}{2}")))
        self.wait(1)
        self.play(Transform(equation, MathTex("f(n) = 2n^2 + 1")))
        self.wait(5)

    def hightlight(self, indexes, algorithm):
        animations = []
        for i, line in enumerate(algorithm.code):
            if i in indexes:
                animations += [line.animate.set_opacity(1)]
            else:
                animations += [line.animate.set_opacity(0.3)]
        return animations
