import math
from numpy import arange

# class that operates all needed calculation
class Calculations:

    # function that returns True if line is number, False- otherwise
    def is_number(line):
        if len(line) == 0:
            return False
        parts = line.split('.')
        if len(parts) > 2:
            return False
        if len(parts[0]) == 0:
            return False
        if line[0] == '-' and len(parts[0]) == 1:
            return False
        for c in line:
            if c != '-' and not c.isdigit() and c != '.':
                return False
        return True

    # Given function for computation practicum (variant 19)
    def function(x, y):
        return 2*x + y - 3

    # formula to compute constant in the solution of the given function
    def particular_sol(x0, y0):
        return (y0 + 2 * x0 - 1) / (math.e ** x0)

    # solution for the given Initial Value Problem
    def IVP_solution(x, x0, y0):
        return Calculations.particular_sol(x0, y0) * (math.e ** (x)) - 2 * x + 1

    # function that computes approximated values according to the given numerical method's formula
    def compute_by_method(x0, b, n, y0, method_formula):
        x_rows = []
        y_rows = []
        x = x0
        y = y0
        step = (b - x0)/n
        step = round(step,4)
        b = b + 0.01
        for x in arange(x0, b, step):
            x_rows.append(x)
            y_rows.append(y)
            y = method_formula(x, y, step)
        return [x_rows, y_rows]