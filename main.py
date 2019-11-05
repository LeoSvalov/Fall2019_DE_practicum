from methods import *
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from calculations import *


class Draw:

    @staticmethod
    def set_plot(curves, legend, window_id, title):
        plt.figure(window_id)
        for points in curves:
            plt.plot(points[0], points[1])
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.gcf().canvas.set_window_title(title)
        plt.title("y' = 2x + y − 3")

    @staticmethod
    def set_plot_of_results(curves, legend):
        plt.close(1)
        Draw.set_plot(curves, legend, 1, 'Graphs of results')

    @staticmethod
    def set_plot_of_global_errors(curves, legend):
        plt.close(2)
        Draw.set_plot(curves, legend, 2, 'Graphs of global errors')

        @staticmethod
    def set_plot_of_local_errors(curves, legend):
        plt.close(2)
        Draw.set_plot(curves, legend, 2, 'Graphs of local errors')


    
    def on_draw_button_clicked():
        
        x0 = x0_entry.get()
        y0 = y0_entry.get()
        x = x_entry.get()
        n = n_entry.get()

        
        if not Calculations.is_number(x0):
            info_label.configure(text='Incorrect X0.', background="brown")
            return
        if not Calculations.is_number(y0):
            info_label.configure(text='Incorrect Y0.', background="brown")
            return    
        if not Calculations.is_number(x):
            info_label.configure(text='Incorrect X.', background="brown")
            return
        if not Calculations.is_number(n):
            info_label.configure(text='Incorrect N.', background="brown")
            return
        info_label.configure(text='', background="brown")

        methods = list()
        
        if exact_method_flag.get():
            methods.append('Exact')
        if euler_method_flag.get():
            methods.append('Euler')
        if improved_euler_method_flag.get():
            methods.append('Improved Euler')
        if runge_kutta_method_flag.get():
            methods.append('Runge Kutta')
        

        if len(methods) == 0:
            info_label.configure(text='Select at least one method.')
            return

        
        show_plot(methods)

    @staticmethod
    def show_plots():
        plt.show()
        



def show_plot(methods):
        
    result_graphs = list()
    global_error_graphs = list()
    local_error_graphs = list()

    
    for method in methods:
        if method == 'Exact':
            result_graphs.append(ExactMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
        elif method == 'Euler':
            result_graphs.append(EulerMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
            global_error_graphs.append(EulerMethod.get_global_error(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
        elif method == 'Improved Euler':
            result_graphs.append(ImprovedEulerMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
            global_error_graphs.append(ImprovedEulerMethod.get_global_error(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
        elif method == 'Runge Kutta':
            result_graphs.append(RungeKuttaMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
            global_error_graphs.append(RungeKuttaMethod.get_global_error(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),float(y0_entry.get())))
    
  
    Draw.set_plot_of_results(result_graphs, methods)
    if 'Exact' in methods:
        methods.remove('Exact')
    Draw.set_plot_of_global_errors(global_error_graphs, methods)
    Draw.show_plots()




window = Tk()

# filling GUI with necessary fields

window.title("Menu")
window.geometry('250x500')
window.configure(background="brown")

info_label = Label(window, text='Input:', background="brown")
info_label.grid(column=0, row=0, sticky=W)

enter_x0_label = Label(window, text='X0:', background="brown")
enter_x0_label.grid(column=0, row=1, sticky=W)

x0_entry = Entry(window)
x0_entry.grid(column=0, row=2, sticky=W)

enter_y0_label = Label(window, text='Y0:', background="brown")
enter_y0_label.grid(column=0, row=3, sticky=W)

y0_entry = Entry(window)
y0_entry.grid(column=0, row=4, sticky=W)

enter_x_label = Label(window, text='X:', background="brown")
enter_x_label.grid(column=0, row=5, sticky=W)

x_entry = Entry(window)
x_entry.grid(column=0, row=6, sticky=W)


enter_n_label = Label(window, text='N:', background="brown")
enter_n_label.grid(column=0, row=7, sticky=W)

n_entry = Entry(window)
n_entry.grid(column=0, row=8, sticky=W)

mathods_label = Label(window, text='Methods:', background="brown")
mathods_label.grid(column=0, row=9, sticky=W)

exact_method_flag = BooleanVar()
exact_method_check_button = Checkbutton(window, text='Exact', variable=exact_method_flag, background="brown")
exact_method_check_button.grid(column=0, row=10, sticky=W)

euler_method_flag = BooleanVar()
euler_check_button = Checkbutton(window, text='Euler', variable=euler_method_flag, background="brown")
euler_check_button.grid(column=0, row=11, sticky=W)

improved_euler_method_flag = BooleanVar()
improved_euler_check_button = Checkbutton(window, text='Improved Euler',  variable=improved_euler_method_flag, background="brown")
improved_euler_check_button.grid(column=0, row=12, sticky=W)

runge_kutta_method_flag = BooleanVar()
runge_kutta_check_button = Checkbutton(window, text='Runge Kutta', variable=runge_kutta_method_flag, background="brown")
runge_kutta_check_button.grid(column=0, row=13, sticky=W)


draw_button = ttk.Button(window, text='Draw', command=Draw.on_draw_button_clicked)
draw_button.grid(column=0, row=14, sticky=N+S+W+E)

window.mainloop()