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

class electro(Scene):
    def construct(self):
        #self.add(NumberPlane())
        self.para_function1()      

    def para_function1(self):
        func1 = lambda t: np.array([t,2*np.sin(0.7*t),0])
        func2 = lambda t: np.array([t,0,0])
        graph1 = ParametricFunction(func1,t_min=-10,t_max=10,color=WHITE)
        graph2 = ParametricFunction(func2,t_min=-10,t_max=10,color=BLUE_A)
        self.play(ShowCreation(graph1),
            run_time=6)
        self.play(ShowCreation(graph2),
            run_time=2)
        for i in range(-6,-4):
            func3 = lambda t: np.array([i,t,0])
            func4 = lambda t: np.array([-i,t,0])
            func5 = lambda t: np.array([-i+0.5,t,0])
            func6 = lambda t: np.array([i-0.5,t,0])
            graph3 = ParametricFunction(func3,t_min=0,t_max=2*np.sin(0.7*i),color=RED)
            graph6 = ParametricFunction(func6,t_min=0,t_max=2*np.sin(0.7*(i-0.5)),color=RED)
            graph4 = ParametricFunction(func4,t_min=0,t_max=-2*np.sin(0.7*i),color=BLUE_E)
            graph5 = ParametricFunction(func5,t_min=0,t_max=-2*np.sin(0.7*(i-0.5)),color=BLUE_E)
            self.play(ShowCreation(graph3),
                ShowCreation(graph4),
                ShowCreation(graph5),
                ShowCreation(graph6))
        for i in range(-4,1):
            func3 = lambda t: np.array([i,t,0])
            func4 = lambda t: np.array([-i,t,0])
            func5 = lambda t: np.array([-i+0.5,t,0])
            func6 = lambda t: np.array([i-0.5,t,0])
            graph3 = ParametricFunction(func3,t_min=0,t_max=2*np.sin(0.7*i),color=BLUE_E)
            graph6 = ParametricFunction(func6,t_min=0,t_max=2*np.sin(0.7*(i-0.5)),color=BLUE_E)
            graph4 = ParametricFunction(func4,t_min=0,t_max=-2*np.sin(0.7*i),color=RED)
            graph5 = ParametricFunction(func5,t_min=0,t_max=-2*np.sin(0.7*(i-0.5)),color=RED)
            
            self.play(ShowCreation(graph3),
                ShowCreation(graph4),
                ShowCreation(graph5),
                ShowCreation(graph6))        
        for i in range(-4,0):
            func3 = lambda t: np.array([i,t,0])
            func4 = lambda t: np.array([-i,t,0])
            graph3 = ParametricFunction(func3,t_min=0,t_max=2*np.sin(0.7*i),color=BLUE_E)
            graph4 = ParametricFunction(func4,t_min=0,t_max=-2*np.sin(0.7*i),color=RED)
            self.play(ShowCreation(graph3),
                ShowCreation(graph4))
        self.play(FadeOut(graph1),
            run_time=2)

class TextoCampo(Scene):
    def construct(self):
        title = TextMobject(
        "CAMPO \\\\"           # Salto de línea con \\\\
        " ELECTROMAGNETICO"
        )
        title.scale(2.3)
        self.play(
            Write(title),      # de arriba hacia abajo el parámetro es DOWN
            run_time=2                  # La duración de la animación es 3s
        )
        self.wait()

class TextoJames(Scene):
    def construct(self):
        title1 = TextMobject(
        "1880"           # Salto de línea con \\\\
        )
        title2 = TextMobject(
        "James C. Maxwell "           # Salto de línea con \\\\
        )        
        title1.to_edge(np.array([-5,0,0]))
        title1.scale(3)
        title2.to_edge(np.array([5,-0.5,0]))
        title2.scale(1.5)
        self.play(
            Write(title1),      # de arriba hacia abajo el parámetro es DOWN
            Write(title2),
            run_time=2                 # La duración de la animación es 3s
        )

        self.wait()

        title3 = TextMobject(
        "1880"           # Salto de línea con \\\\
        )
        title3.scale(1.5)
        title3.to_edge(np.array([-3,0.5,0]))
        title4 = TexMobject(
            "\\nabla \\cdot E=\\frac{\\rho}{\\epsilon_0}"
        )
        title4.scale(1.25)
        title5 = TexMobject(
            "\\nabla \\cdot B=0"
        )
        title5.scale(1.25)
        title6 = TexMobject(
            "\\nabla \\times E=-\\frac{\\partial B}{\\partial t}"
        )
        title6.scale(1.25)
        title7 = TexMobject(
            "\\nabla \\times B=\\mu_0 J"
        )
        title7.scale(1.25)
        title4.to_edge(np.array([-3,3.0,0]))                                
        title5.to_edge(np.array([-3,6.75,0]))
        title6.to_edge(np.array([-3,-4.5,0]))
        title7.to_edge(np.array([-3,-2.0,0]))
        self.play(
            Transform(title1, title3),
            Write(title4),
            Write(title5),
            Write(title6),
            Write(title7),
            run_time=2                 # La duración de la animación es 3s
        )
        title8 = TexMobject(
            "Leyes~de~Gauss"
        )
        title9 = TexMobject(
            "Ley~de~Faraday"
        )
        title10= TexMobject(
            "Ley~de~Ampere"
        )    
        title8.to_edge(np.array([7,5.5,0]))
        title8.scale(1.25)
        title9.to_edge(np.array([7,-5,0]))
        title9.scale(1.25)
        title10.to_edge(np.array([7,-2.0,0]))
        title10.scale(1.25)
        self.play(
            FadeOut(title2),
            run_time=1
        )
        self.play(
            Write(title8),
            Write(title9),
            Write(title10),
            run_time=2                 # La duración de la animación es 3s
        )            
        
        self.wait()
        
        title11= TexMobject(
            "\\nabla \\times B=\\mu_0 J+\\mu_0\\epsilon_0\\frac{\\partial E}{\\partial t}"
        )
        title12= TexMobject(
            "Ley~de"
        )
        title13= TexMobject(
            "Ampere-Maxwell"
        )        
        title11.scale(1.25)
        title11.to_edge(np.array([-1,-0.75,0]))
        title12.to_edge(np.array([9,-2.0,0]))
        title12.scale(1.25)        
        title13.to_edge(np.array([3,-0.5,0]))
        title13.scale(1.25)             
        self.play(
            Transform(title10, title12),
            Transform(title7, title11),
            Write(title13),
            run_time=2                 # La duración de la animación es 3s
        )  
        self.wait()