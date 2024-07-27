from abc import ABC, abstractmethod
from math import pi as PI

class Figure(ABC):
    '''
    abstract class for figures
    '''

    @abstractmethod
    def calculate_area(self, *args, **kwargs):
        '''
        abstract method for calculating area of a figure
        '''
        pass

class Triangle(Figure):

    def calculate_area(self, a: float, b: float, c: float):
        '''
        calculate area of triangle by 3 sides: a, b, c
        '''

        if not self.is_existing_triangle(a, b ,c):
            raise ValueError('Triangle does not exist')
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

    def is_existing_triangle(self, a, b, c):
        '''
        Check whether triangle is valid or not
        '''

        return (a + b > c and a + c > b and b + c > a)

    def is_right_triangle(self, a, b, c):
        '''
        find is triangle right angled or not
        '''

        return (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b)


class Circle(Figure):

    def calculate_area(self, r):
        '''
        calculate area of a circle by the radius r
        '''

        return PI * r**2


