from calculations import *
from numpy import arange

# class for calculated local/maximum errors
class MethodsErrors:

    # local error computation
    def compute_local_error(x0, b, n, y0, method):
        method_values = method(x0, b, n, y0)
        exact_values = ExactMethod.get_result(x0,b,n,y0)
        method_ys = method_values[1]
        exact_ys = exact_values[1]
        exact_xs = exact_values[0]
        y_rows = []
        x_rows = []
        y_temp_rows = []
        for i in range(len(exact_xs)):
            y_temp_rows.append(abs(exact_ys[i] - method_ys[i]))
        for i in range(len(exact_xs)):
            if i == 0:
                y_rows.append(0)
            else:
                y_rows.append(y_temp_rows[i] - y_temp_rows[i-1])
            x_rows.append(exact_xs[i])

        return [x_rows, y_rows]
    
    # maximum error computation
    def compute_global_error(x0, b, n0, n, y0, method):
        errors = []
        n_rows = []
        for i in range(int(n0),int(n)+1):
            method_values = method(x0,b,i,y0)
            exact_values = ExactMethod.get_result(x0,b,i,y0)
            y = exact_values[1][-1]
            m_point = method_values[1][-1]
            errors.append(abs(y - m_point))
            n_rows.append(i)
        return [n_rows, errors]

# class for the exact method
class ExactMethod:

    def get_result(x0, b, n, y0):
        x = x0
        step = (b - x0) / n
        step = round(step,4)
        x_rows = list()
        y_rows = list()
        b = b + 0.01
        for x in arange(x0, b, step):

            y = Calculations.IVP_solution(x, x0, y0)
            x_rows.append(x)
            y_rows.append(y)
            x = round(x,2)
        return [x_rows, y_rows]

# class that represents the Euler method
class EulerMethod:

    # returns approximated values of the method
    def get_result(x0, b, n, y0):
        return Calculations.compute_by_method(x0, b, n, y0, EulerMethod.formula)
    
    # returns local error values of the method
    def get_local_error(x0, b, n, y0):
        return MethodsErrors.compute_local_error(x0, b, n, y0, EulerMethod.get_result)
    
    # returns maximum error values of the method
    def get_global_error(x0, b, n0, n, y0):
        return MethodsErrors.compute_global_error(x0, b, n0, n, y0, EulerMethod.get_result)   

    # approach of this method to compute approximated values
    def formula(x, y, step):
        return y + step * Calculations.function(x, y)

# class that represents the Improved Euler method
class ImprovedEulerMethod:

    # returns approximated values of the method
    def get_result(x0, b, n, y0):
        return Calculations.compute_by_method(x0, b, n, y0, ImprovedEulerMethod.formula)
  
    # returns local error values of the method
    def get_local_error(x0, b, n, y0):
        return MethodsErrors.compute_local_error(x0, b, n, y0, ImprovedEulerMethod.get_result)

    # returns maximum error values of the method
    def get_global_error(x0, b, n0, n, y0):
        return MethodsErrors.compute_global_error(x0, b, n0, n, y0, ImprovedEulerMethod.get_result)    

    # approach of this method to compute approximated values
    def formula(x, y, step):
        return y + (step / 2) * (Calculations.function(x, y) + Calculations.function(x + step, y + step * Calculations.function(x, y)))

# class that represents the Runge Kutta method
class RungeKuttaMethod:

    # returns approximated values of the method
    def get_result(x0, b, n, y0):
        return Calculations.compute_by_method(x0, b, n, y0, RungeKuttaMethod.formula)

    # returns local error values of the method
    def get_local_error(x0, b, n, y0):
        return MethodsErrors.compute_local_error(x0, b, n, y0, RungeKuttaMethod.get_result)

    # returns maximum error values of the method
    def get_global_error(x0, b, n0, n, y0):
        return MethodsErrors.compute_global_error(x0, b, n0, n, y0, RungeKuttaMethod.get_result)
    
    # approach of this method to compute approximated values
    def formula(x, y, step):
        k_1 = Calculations.function(x, y)
        k_2 = Calculations.function(x + step / 2, y + (step / 2) * k_1)
        k_3 = Calculations.function(x + step / 2, y + (step / 2) * k_2)
        k_4 = Calculations.function(x + step, y + step * k_3)
        return y + (step / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)