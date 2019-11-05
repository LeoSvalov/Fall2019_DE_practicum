import math



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
    def compute_by_method(x0, b, n, y0, method_function):
        x_rows = list()
        y_rows = list()
        y = y0
        x = x0
        step = (b - x0) / n
        while abs(b - x) >= abs(step):
            x_rows.append(x)
            y_rows.append(y)
            try:
                y = method_function(x, y, step)
            except OverflowError:
                y = y0
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]


    @staticmethod
    def compute_global_error(x0, b, n, y0, method):
        method_values = method(x0, b, n, y0)
        x_rows = method_values[0]
        y_rows = method_values[1]
        for i in range(len(x_rows)):
            y = Calculations.IVP_solution(x_rows[i], x0, y0)
            y_rows[i] = abs(y_rows[i] - y)
        return [x_rows, y_rows]

    @staticmethod
    def IVP_solution(x, x0, y0):
        return Calculations.particular_sol(x0, y0) * (math.e ** (x)) + 2 * x - 1