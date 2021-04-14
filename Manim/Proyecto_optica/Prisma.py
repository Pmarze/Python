# Comando para ejecutar el programa y exportar video de muestra 
# en baja resolución, este además, muestra la lista de objetos
# a exportar, se elije ingresando el número correspondiente.
# python -m manim Funciones.py -pl
# Comando para ejecutar el programa y exportar todos los objetos
# en alta calidad.
# python -m manim funciones.py -p

from big_ol_pile_of_manim_imports import *
import numpy as np
class graphx(GraphScene):
    CONFIG={
        "x_min": -20,
        "x_max": 50,
        "y_min": -2,
        "y_max": 2,
        #"x_axis_label": "$x$",
        #"y_axis_label": "$y$",
        "graph_origin": 0.5 * DOWN + 3 * LEFT,
    }
    #defining graph functions
    def show_function_graph(self):
        self.setup_axes(animate=True)
        # Math function
        def func0(x):
            return np.sin(x)
        def func1(x):
            return np.sin(x)
        def func2(x):
            return np.sin(x+np.pi/4)
        def func3(x):
            return np.sin(x+2*np.pi/4)
        def func4(x):
            return np.sin(x+3*np.pi/4)   
        def Triangulo1(x):
            return -0.5
        def Triangulo2(x):
            return 0.1*x+0.5
        def Triangulo3(x):
            return -0.1*x+0.5                
        linea1=self.get_graph(Triangulo1,x_min=-10,x_max=10)
        linea1.set_color(BLUE_B)
        linea2=self.get_graph(Triangulo2,x_min=-10,x_max=0)
        linea2.set_color(BLUE_B)
        linea3=self.get_graph(Triangulo3,x_min=0,x_max=10)
        linea3.set_color(BLUE_B)
        graph0=self.get_graph(func0,x_min=-5*np.pi,x_max=-3.325)
        graph0.set_color(WHITE)        
        graph1=self.get_graph(func1,x_min=6.15,x_max=15*np.pi)
        graph1.set_color(RED)
        graph2=self.get_graph(func2,x_min=5.45,x_max=15*np.pi)
        graph2.set_color(YELLOW)
        graph3=self.get_graph(func3,x_min=4.75,x_max=15*np.pi)
        graph3.set_color(GREEN)
        graph4=self.get_graph(func4,x_min=4,x_max=15*np.pi)
        graph4.set_color(PURPLE)        
        self.play(ShowCreation(linea1),ShowCreation(linea2),ShowCreation(linea3),
            run_time=1)        
        self.play(ShowCreation(graph0),
            run_time=3)
        self.play(ShowCreation(graph1),ShowCreation(graph2),ShowCreation(graph3),ShowCreation(graph4),
            run_time=6)
    def construct(self):
        self.show_function_graph()