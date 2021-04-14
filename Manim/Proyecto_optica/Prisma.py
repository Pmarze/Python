# Comando para ejecutar el programa y exportar video de muestra 
# en baja resolución, este además, muestra la lista de objetos
# a exportar, se elije ingresando el número correspondiente.
# python -m manim Funciones.py -pl
# Comando para ejecutar el programa y exportar todos los objetos
# en alta calidad.
# python -m manim funciones.py -p

from big_ol_pile_of_manim_imports import *
import numpy as np
class prisma(GraphScene):
    CONFIG={
        "x_min": -20,
        "x_max": 50,
        "y_min": -2,
        "y_max": 4,
        "x_axis_label": "",
        "y_axis_label": "",
        "graph_origin": 0 * DOWN + 2 * LEFT,
        "axes_color": BLACK
    }
    #defining graph functions
    def show_function_graph(self):
        self.setup_axes(animate=False)
        # Math function
        valin=1.1
        delva=0.01
        valdi=2.5
        deldi=0.25
        def func0(x):
            return 0.15**2*x+0.4
        def func1(x):
            return (np.sin(valin*x)-x/(valdi)**2)/3
        def func2(x):
            return (np.sin((valin+delva)*x)-x/(valdi+deldi)**2)/3
        def func3(x):
            return (np.sin((valin+delva*2)*x)-x/(valdi+deldi*2)**2)/3
        def func4(x):
            return (np.sin((valin+delva*3)*x)-x/(valdi+deldi*3)**2)/3
        def func5(x):
            return (np.sin((valin+delva*4)*x)-x/(valdi+deldi*4)**2)/3
        def func6(x):
            return (np.sin((valin+delva*5)*x)-x/(valdi+deldi*5)**2)/3
        def func7(x):
            return (np.sin((valin+delva*6)*x)-x/(valdi+deldi*6)**2)/3   
        def Triangulo1(x):
            return -1
        def Triangulo2(x):
            return 0.2*x+1
        def Triangulo3(x):
            return -0.2*x+1
        lt1=self.get_graph(Triangulo1,x_min=-10,x_max=10, color=LIGHT_GRAY)
        lt2=self.get_graph(Triangulo2,x_min=-10,x_max=0, color=LIGHT_GRAY)
        lt3=self.get_graph(Triangulo3,x_min=0,x_max=10, color=LIGHT_GRAY)
        x0=-3.45
        xf=20*np.pi
        lu0=self.get_graph(func0,x_min=-20,x_max=-3.5, color=WHITE)
        lu1=self.get_graph(func1,x_min=x0,x_max=xf, color=RED)
        lu2=self.get_graph(func2,x_min=x0,x_max=xf, color=ORANGE)
        lu3=self.get_graph(func3,x_min=x0,x_max=xf, color=YELLOW)
        lu4=self.get_graph(func4,x_min=x0,x_max=xf, color=GREEN)
        lu5=self.get_graph(func5,x_min=x0,x_max=xf, color=BLUE_C)
        lu6=self.get_graph(func6,x_min=x0,x_max=xf, color=PURPLE_E)
        lu7=self.get_graph(func7,x_min=x0,x_max=xf, color=PURPLE_C)

        self.play(ShowCreation(lt1),
            ShowCreation(lt2),
            ShowCreation(lt3),
            run_time=1)        
        self.play(ShowCreation(lu0),
            run_time=3)
        self.play(ShowCreation(lu1),
            ShowCreation(lu2),
            ShowCreation(lu3),
            ShowCreation(lu4),
            ShowCreation(lu5),
            ShowCreation(lu6),
            ShowCreation(lu7),
            run_time=6)
        self.wait(5)
        self.play(FadeOut(lt1),
            FadeOut(lt2),
            FadeOut(lt3),
            FadeOut(lu1),
            FadeOut(lu2),
            FadeOut(lu3),
            FadeOut(lu4),
            FadeOut(lu5),
            FadeOut(lu6),
            FadeOut(lu7),
            run_time=1)
    def construct(self):
        self.show_function_graph()

class onda(GraphScene):
    CONFIG={
        "x_min": -20,
        "x_max": 50,
        "y_min": -2,
        "y_max": 4,
        "x_axis_label": "",
        "y_axis_label": "",
        "graph_origin": 0 * DOWN + 2 * LEFT,
        "axes_color": BLACK
    }    
    #defining graph functions
    def show_function_graph(self):
        self.setup_axes(animate=False)    
        def func0(x):
            return 0.15**2*x+0.4
        def func1(x):
            return 2*np.sin(0.15*x)
        def func2(x):
            return 0
        x0=-5.5
        xf=21*np.pi        
        lu0=self.get_graph(func0,x_min=-20,x_max=-4, color=WHITE)
        senl=self.get_graph(func1,x_min=2*x0*np.pi,x_max=xf, color=WHITE)
        linx=self.get_graph(func2,x_min=3*x0*np.pi,x_max=xf+5, color=WHITE)
        self.play(Transform(lu0, senl),
            run_time=5)
        self.play(ShowCreation(linx),
            run_time=3)
    def construct(self):
        self.show_function_graph()