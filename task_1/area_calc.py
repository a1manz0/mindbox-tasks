from typing import Optional
from figures import Figure, Triangle, Circle

class AreaCalculator():
    def __init__(self) -> None:
        self.figures = {
            'triangle': Triangle(),
            'circle': Circle()
        }

    def get(self, figure_type: str):
        return self.figures.get(figure_type)

    def calculate_area(self, figure_type: Optional[str] = None,
                       *args, **kwargs):
        '''
        calculates the area of a figure, after specifying the type of 
        figure there are positional and named variables that 
        are used to calculate the area
        '''

        if figure_type is None:
            raise ValueError('figure_type is not defined')

        return self.figures.get(figure_type).calculate_area(*args, **kwargs)

    def add_figure(self, figure: Figure, figure_name: Optional[str] = None):
        '''
        adds a figure to the dict
        '''

        if figure_name is None:
            raise ValueError('Formula name is not defined')
        if not isinstance(figure, Figure):
            raise TypeError('figure must inherit from Figure')
        self.figures[figure_name] = figure


