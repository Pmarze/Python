# Comando para ejecutar el programa y exportar video de muestra 
# en baja resolución, este además, muestra la lista de objetos
# a exportar, se elije ingresando el número correspondiente.
# python -m manim Prisma.py -pl
# Comando para ejecutar el programa y exportar todos los objetos
# en alta calidad.
# python -m manim Prisma.py -p

from big_ol_pile_of_manim_imports import *
import numpy as np
class prisma(GraphScene):
    CONFIG={
        "x_min": -20,
        "x_max":  50,
        "y_min":  -2,
        "y_max":   4,
        "x_axis_label": "",
        "y_axis_label": "",
        "graph_origin": 1 * DOWN + 2 * LEFT,
        "axes_color": BLACK
    }
    #defining graph functions
    def show_function_graph(self):
        self.setup_axes(animate=False)
        # Math function
        valinic=1.1
        deltava=0.01
        valdivi=2.5
        deltadi=0.25
        def func0(x):
            return 0.15**2*x+0.25
        def func1(x):
            return (np.sin(valinic*x)+x/(valdivi)**2)/3
        def func2(x):
            return (np.sin((valinic+deltava)*x)+x/(valdivi+deltadi)**2)/3
        def func3(x):
            return (np.sin((valinic+deltava*2)*x)+x/(valdivi+deltadi*2)**2)/3
        def func4(x):
            return (np.sin((valinic+deltava*3)*x)+x/(valdivi+deltadi*3)**2)/3
        def func5(x):
            return (np.sin((valinic+deltava*4)*x)+x/(valdivi+deltadi*4)**2)/3
        def func6(x):
            return (np.sin((valinic+deltava*5)*x)+x/(valdivi+deltadi*5)**2)/3
        def func7(x):
            return (np.sin((valinic+deltava*6)*x)+x/(valdivi+deltadi*6)**2)/3
        def Triangulo1(x):
            return -1
        def Triangulo2(x):
            return 0.2*x+1
        def Triangulo3(x):
            return -0.2*x+1                
        linea1=self.get_graph(Triangulo1,x_min=-10,x_max=10)
        linea1.set_color(LIGHT_GRAY)
        linea2=self.get_graph(Triangulo2,x_min=-10,x_max=0)
        linea2.set_color(LIGHT_GRAY)
        linea3=self.get_graph(Triangulo3,x_min=0,x_max=10)
        linea3.set_color(LIGHT_GRAY)
        x0=-4
        xf=20*np.pi
        graph0=self.get_graph(func0,x_min=-20,x_max=-4, color=WHITE)
        graph1=self.get_graph(func1,x_min=x0,x_max=xf, color=RED)
        graph2=self.get_graph(func2,x_min=x0,x_max=xf, color=ORANGE)
        graph3=self.get_graph(func3,x_min=x0,x_max=xf, color=YELLOW)
        graph4=self.get_graph(func4,x_min=x0,x_max=xf, color=GREEN)
        graph5=self.get_graph(func5,x_min=x0,x_max=xf, color=BLUE_C)
        graph6=self.get_graph(func6,x_min=x0,x_max=xf, color=PURPLE_E)
        graph7=self.get_graph(func7,x_min=x0,x_max=xf, color=PURPLE_C)
        
        self.play(ShowCreation(linea1),
            ShowCreation(linea2),
            ShowCreation(linea3))
            #run_time=1)        
        self.play(ShowCreation(graph0),
            run_time=3)
        self.play(ShowCreation(graph1),
            ShowCreation(graph2),
            ShowCreation(graph3),
            ShowCreation(graph4),
            ShowCreation(graph5),
            ShowCreation(graph6),
            ShowCreation(graph7),
            run_time=6)
    def construct(self):
        self.show_function_graph()