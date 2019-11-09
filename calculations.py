import math
from methods import *
from numpy import arange

class Calculations:

    @staticmethod
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

   
    @staticmethod
    def function(x, y):
        return 2*x + y - 3

   
    @staticmethod
    def particular_sol(x0, y0):
        return (y0 + 2 * x0 - 1) / (math.e ** x0)


    @staticmethod
    def compute_Euler(x0, b, n, y0):
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
            y = y + step * Calculations.function(x,y)
            x = round(x,2)


        return [x_rows, y_rows]

    @staticmethod
    def compute_ImprovedEuler(x0, b, n, y0):
        x_rows = []
        y_rows = []
        x = x0
        y = y0
        step = (b - x0)/n
        step = round(step,4)
        b = b + 0.01
        for x in arange(x0, b , step):
            x_rows.append(x)
            y_rows.append(y)
            y = y + (step / 2) * (Calculations.function(x, y) + Calculations.function(x + step, y + step * Calculations.function(x, y)))
            x = round(x,2)
        return [x_rows, y_rows]

    @staticmethod
    def compute_RungeKutta(x0, b, n, y0):
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
            k_1 = Calculations.function(x, y)
            k_2 = Calculations.function(x + step / 2, y + (step / 2) * k_1)
            k_3 = Calculations.function(x + step / 2, y + (step / 2) * k_2)
            k_4 = Calculations.function(x + step, y + step * k_3)
            y = y + (step / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
            x = round(x,2)
            



        return [x_rows, y_rows]        

    @staticmethod
    def IVP_solution(x, x0, y0):
        return Calculations.particular_sol(x0, y0) * (math.e ** (x)) - 2 * x + 1