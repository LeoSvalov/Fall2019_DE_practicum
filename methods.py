from calculations import *


class ExactMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        x = x0
        step = (b - x0) / n

        x_rows = list()
        y_rows = list()

        while x <= b:
            y = Calculations.IVP_solution(x, x0, y0)
            x_rows.append(x)
            y_rows.append(y)
            x += step

        return [x_rows, y_rows]


class EulerMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        return Calculations.compute_by_method(x0, b, n, y0, EulerMethod.function)

    @staticmethod
    def get_global_error(x0, b, n, y0):
        return Calculations.compute_global_error(x0, b, n, y0, EulerMethod.get_result)

    @staticmethod
    def function(x, y, step):
        return y + step * Calculations.function(x, y)


class ImprovedEulerMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        return Calculations.compute_by_method(x0, b, n, y0, ImprovedEulerMethod.function)

    @staticmethod
    def get_global_error(x0, b, n, y0):
        return Calculations.compute_global_error(x0, b, n, y0, ImprovedEulerMethod.get_result)

    @staticmethod
    def function(x, y, step):
        return y + (step / 2) * (Calculations.function(x, y) + Calculations.function(x + step, y + step * Calculations.function(x, y)))


class RungeKuttaMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        return Calculations.compute_by_method(x0, b, n, y0, RungeKuttaMethod.function)

    @staticmethod
    def get_global_error(x0, b, n, y0):
        return Calculations.compute_global_error(x0, b, n, y0, RungeKuttaMethod.get_result)

    @staticmethod
    def function(x, y, step):
        k_1 = Calculations.function(x, y)
        k_2 = Calculations.function(x + step / 2, y + (step / 2) * k_1)
        k_3 = Calculations.function(x + step / 2, y + (step / 2) * k_2)
        k_4 = Calculations.function(x + step, y + step * k_3)
        return y + (step / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
