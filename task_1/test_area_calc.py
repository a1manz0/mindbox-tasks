import unittest
from area_calc import AreaCalculator
from figures import Figure
from math import pi


class TestAreaCalc(unittest.TestCase):

    def test_add_figure(self):
        area_calculator = AreaCalculator()
        class NewFigure(Figure):
            def calculate_area(self):
                pass
        figure_name = 'figure_name'
        area_calculator.add_figure(NewFigure(), figure_name)
        self.assertIn(figure_name, area_calculator.figures)

    def test_new_figure_calculate_area(self):
        area_calculator = AreaCalculator()
        class NewFigure(Figure):
            def calculate_area(self, a=0):
                return a+100
        fig_name = 'figure_name'
        area_calculator.add_figure(NewFigure(), fig_name)
        a = 23
        self.assertEqual(a+100, area_calculator.calculate_area(fig_name, a=a))

    def test_calculate_area_without_figure_type(self):
        area_calculator = AreaCalculator()
        with self.assertRaises(ValueError):
            area_calculator.calculate_area(a=3, b=4, c=5)

    def test_add_formula_with_wrong_args(self):
        area_calculator = AreaCalculator()
        class NewFigure(Figure):
            def calculate_area(self, a=0):
                return a+100
        fig_name = 'figure_name'
        area_calculator.add_figure(NewFigure(), fig_name)
        with self.assertRaises(TypeError):
            area_calculator.add_figure('figure', fig_name)
        with self.assertRaises(ValueError):
            area_calculator.add_figure(NewFigure())

    def test_is_existing_triangle(self):
        area_calculator = AreaCalculator()
        a, b, c = 3, 4, 5
        self.assertEqual(True, area_calculator.get('triangle').is_existing_triangle(a, b, c))
        a, b,c = 5, 8, 3
        self.assertEqual(False, area_calculator.get('triangle').is_existing_triangle(a, b, c))

    def test_calculate_area_of_triangle(self):
        area_calculator = AreaCalculator()
        a, b, c = 12, 14, 18
        s = (a + b + c) / 2
        out = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        self.assertEqual(out, area_calculator.calculate_area('triangle', a, b, c))

    def test_is_right_triangle(self):
        area_calculator = AreaCalculator()
        a, b, c = 12, 14, 18
        self.assertEqual(False, area_calculator.get('triangle').is_right_triangle(a, b, c))
        a, b, c = 3, 4, 5
        self.assertEqual(True, area_calculator.get('triangle').is_right_triangle(a, b, c))

    def test_calculate_area_of_circle(self):
        area_calculator = AreaCalculator()
        r = 10
        self.assertEqual(pi * r**2, area_calculator.calculate_area('circle', r))



if __name__ == '__main__':
    unittest.main()
