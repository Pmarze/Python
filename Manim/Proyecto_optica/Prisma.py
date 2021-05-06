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
            run_time=2                 # La duración de la animación es 3s
        )
        self.play(
            Write(title2),
            run_time=2
        )

        self.wait()

        title3 = TextMobject(
        "1880"           # Salto de línea con \\\\
        )
        title3.scale(1.5)
        title3.to_edge(np.array([-3,0.5,0]))
        self.play(
            Transform(title1, title3)
        )
        
        self.wait()
        
        self.play(
            FadeOut(title2),
            run_time=1
        )

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
            Write(title4),
            Write(title5),
            Write(title6),
            Write(title7),
            run_time=2                 # La duración de la animación es 3s
        )

        self.wait()

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

class EyB(Scene):
    def construct(self):
        #self.add(NumberPlane())
        self.para_function1()      

    def para_function1(self):
        title1= TexMobject(
            "\\vec{E}")           
        title2= TexMobject(
            "\\vec{B}")      
        title3= TexMobject(
            "E"
        )     
        title4= TexMobject(
            "M"
        )             
        title1.to_edge(np.array([-6.75,7,0]))
        title1.scale(4)               
        title2.to_edge(np.array([6.75,7,0]))
        title2.scale(4)     
        title3.to_edge(np.array([-11.5,0,0]))
        title3.scale(6)   
        title4.to_edge(np.array([11.5,0,0]))
        title4.scale(6)           
        func1 = lambda t: np.array([-3.5,t,0])
        graph1 = ParametricFunction(func1,t_min=1.25,t_max=4,color=RED_C)
        func2 = lambda t: np.array([-3.5,t,0])
        graph2 = ParametricFunction(func2,t_min=-1.0,t_max=-4,color=RED_C)
        func3 = lambda t: np.array([3.5,t,0])
        graph3 = ParametricFunction(func3,t_min=1.25,t_max=4,color=GREEN_D)
        func4 = lambda t: np.array([3.5,t,0])
        graph4 = ParametricFunction(func4,t_min=-1.0,t_max=-4,color=GREEN_D)
        
        func5 = lambda t: np.array([t,0,0])
        graph5 = ParametricFunction(func5,t_min=-4.5,t_max=-7,color=RED_C)
        graph6 = ParametricFunction(func5,t_min=-2.5,t_max=-0.20,color=RED_C)
        func7= lambda t: np.array([t,0.26795*t+0.93783,0])
        graph8 = ParametricFunction(func7,t_min=-2.5,t_max=-0.155,color=RED_C)
        graph9 = ParametricFunction(func7,t_min=-4.5,t_max=-7,color=RED_C)
        func8= lambda t: np.array([t,0.57733*t+2.02066,0])
        graph10 = ParametricFunction(func8,t_min=-2.5,t_max=0,color=RED_C)
        graph11 = ParametricFunction(func8,t_min=-4.5,t_max=-7,color=RED_C)
        func9= lambda t: np.array([t,t+3.5,0])
        graph12 = ParametricFunction(func9,t_min=-2.5,t_max=0,color=RED_C)
        graph13 = ParametricFunction(func9,t_min=-4.5,t_max=-7,color=RED_C)
        
        func10= lambda t: np.array([t,-t-3.5,0])
        graph14 = ParametricFunction(func10,t_min=-2.5,t_max=0,color=RED_C)
        graph15 = ParametricFunction(func10,t_min=-4.5,t_max=-7,color=RED_C)
        func11= lambda t: np.array([t,-0.26795*t-0.93783,0])
        graph16 = ParametricFunction(func11,t_min=-2.5,t_max=-0.155,color=RED_C)
        graph17 = ParametricFunction(func11,t_min=-4.5,t_max=-7,color=RED_C)
        func12= lambda t: np.array([t,-0.57733*t-2.02066,0])
        graph18 = ParametricFunction(func12,t_min=-2.5,t_max=0,color=RED_C)
        graph19 = ParametricFunction(func12,t_min=-4.5,t_max=-7,color=RED_C)

        # elipses
        func20= lambda t: np.array([3+np.cos(t)/2.5,0+np.sin(t),0])
        graph20 = ParametricFunction(func20,t_min=0.3*np.pi,t_max=1.7*np.pi,color=GREEN_D)

        func21= lambda t: np.array([2.75+2*np.cos(t)/2.5,0+2*np.sin(t),0])
        graph21 = ParametricFunction(func21,t_min=0.2*np.pi,t_max=1.8*np.pi,color=GREEN_D)

        func22= lambda t: np.array([2.5+3*np.cos(t)/2.5,0+3*np.sin(t),0])
        graph22 = ParametricFunction(func22,t_min=0.18*np.pi,t_max=1.82*np.pi,color=GREEN_D)

        func23= lambda t: np.array([2.1+3.5*np.cos(t)/2.25,0+3.5*np.sin(t),0])
        graph23 = ParametricFunction(func23,t_min=0.2*np.pi,t_max=1.8*np.pi,color=GREEN_D)

        func24= lambda t: np.array([1.70+4.35*np.cos(t)/2.25,0+4*np.sin(t),0])
        graph24 = ParametricFunction(func24,t_min=0.1*np.pi,t_max=1.9*np.pi,color=GREEN_D)

        # elipses invertidas       
        func25= lambda t: np.array([4-np.cos(t)/2.5,0-np.sin(t),0])
        graph25 = ParametricFunction(func25,t_max=0.3*np.pi,t_min=1.7*np.pi,color=GREEN_D)

        func26= lambda t: np.array([4.25-2*np.cos(t)/2.5,0+2*np.sin(t),0])
        graph26 = ParametricFunction(func26,t_min=0.2*np.pi,t_max=1.8*np.pi,color=GREEN_D)

        func27= lambda t: np.array([4.5-3*np.cos(t)/2.5,0+3*np.sin(t),0])
        graph27 = ParametricFunction(func27,t_min=0.18*np.pi,t_max=1.82*np.pi,color=GREEN_D)

        func28= lambda t: np.array([4.9-3.5*np.cos(t)/2.25,0+3.5*np.sin(t),0])
        graph28 = ParametricFunction(func28,t_min=0.2*np.pi,t_max=1.8*np.pi,color=GREEN_D)

        func29= lambda t: np.array([5.20-4.2*np.cos(t)/2.25,0+4*np.sin(t),0])
        graph29 = ParametricFunction(func29,t_min=0.1*np.pi,t_max=1.9*np.pi,color=GREEN_D)

        # puntos
        dot=Dot()
        self.play(
            Write(title1),
            Write(title2),
            ShowCreation(graph1),
            ShowCreation(graph2),
            ShowCreation(graph3),
            ShowCreation(graph4),
            ShowCreation(graph5),
            ShowCreation(graph6),
            ShowCreation(graph8),
            ShowCreation(graph9), 
            ShowCreation(graph10),
            ShowCreation(graph11),
            ShowCreation(graph12),
            ShowCreation(graph13),
            ShowCreation(graph14),
            ShowCreation(graph15),
            ShowCreation(graph16),
            ShowCreation(graph17),
            ShowCreation(graph18),
            ShowCreation(graph19),
            ShowCreation(graph20),
            ShowCreation(graph21),
            ShowCreation(graph22),
            ShowCreation(graph23),
            ShowCreation(graph24),
            ShowCreation(graph25),
            ShowCreation(graph26),
            ShowCreation(graph27),
            ShowCreation(graph28),
            ShowCreation(graph29),
            run_time=3
        )
        self.wait()
        self.play(
            FadeOut(graph1),
            FadeOut(graph2),
            FadeOut(graph3),
            FadeOut(graph4),
            FadeOut(graph5),
            FadeOut(graph6),
            FadeOut(graph8),
            FadeOut(graph9),
            FadeOut(graph10),
            FadeOut(graph11),
            FadeOut(graph12),
            FadeOut(graph13),
            FadeOut(graph14),
            FadeOut(graph15),
            FadeOut(graph16),
            FadeOut(graph17),
            FadeOut(graph18),
            FadeOut(graph19),
            FadeOut(graph20),
            FadeOut(graph21),
            FadeOut(graph22),
            FadeOut(graph23),
            FadeOut(graph24),
            FadeOut(graph25),
            FadeOut(graph26),
            FadeOut(graph27),
            FadeOut(graph28),
            FadeOut(graph29),
        run_time=2)
        
        self.play(
            Write(title3),
            Write(title4),
            Transform(title1, title3),
            Transform(title2, title4),
            run_time=2
        )
        for i in range(-7,-2):
            for j in range(-4,2):
                dot = Dot((i,j,0),color=BLUE_D)
                dot1 = Dot((i,abs(j),0),color=BLUE_D)
                dot2 = Dot((abs(i),j,0),color=BLUE_D)
                dot3 = Dot((abs(i),abs(j),0),color=BLUE_D)
                self.play(
                    ShowCreation(dot),
                    ShowCreation(dot1),
                    ShowCreation(dot2),
                    ShowCreation(dot3),
                    run_time=0.0001
                )
        for i in range(-2,1):
            for j in range(-4,-1):
                dot = Dot((i,j,0),color=BLUE_D)
                dot1 = Dot((i,abs(j),0),color=BLUE_D)
                dot2 = Dot((abs(i),j,0),color=BLUE_D)
                dot3 = Dot((abs(i),abs(j),0),color=BLUE_D)
                self.play(
                    ShowCreation(dot),
                    ShowCreation(dot1),
                    ShowCreation(dot2),
                    ShowCreation(dot3),                     
                    run_time=0.0001
                )
                
        dot4 = Dot((0,-2,0))
        dot5 = Dot((0,2,0))                
        self.play(
            ShowCreation(dot4),
            ShowCreation(dot5),                    
            run_time=0.0001
        )

class Electro_correjido(Scene):
    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 2*np.sin((x+dx)/2),
            x_min=-8,x_max=8,
            color=WHITE
        )
    def centro(self,dx=0):
        return FunctionGraph(
            lambda x: 0,
            x_min=-8,x_max=8,
            color=WHITE
        )
    def construct(self):
        sine_function=self.get_sine_wave()
        lineacentro=self.centro()
        d_theta=ValueTracker(0)
        def update_wave(func):
            func.become(
                self.get_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update_centro(func):
            func.become(
                self.centro(dx=d_theta.get_value())
            )
            return func
        sine_function.add_updater(update_wave)
        lineacentro.add_updater(update_centro)
        self.play(ShowCreation(sine_function),
            run_time=3
        )
        self.wait()
        self.play(
            d_theta.increment_value,4*PI,
            rate_func=linear,
            run_time=5
        )
        self.play(
            ShowCreation(lineacentro),
            run_time=1
        )
        #for x in range(0,6):
        for i in range(0,10):
            x=i/2+1
            flecha1=Arrow([x,0,0], [x, 2*np.sin((x)/2), 0],color=RED)
            flecha2=Arrow([-x,0,0], [-x, -2*np.sin((x)/2), 0],color=BLUE)
            flecha3=Arrow([-x-6,0,0], [-x-6, 2*np.sin((x)/2), 0],color=RED)
            flecha4=Arrow([x+6,0,0], [x+6, -2*np.sin((x)/2), 0],color=BLUE)
            self.play(
                ShowCreation(flecha1),
                ShowCreation(flecha2),
                ShowCreation(flecha3),
                ShowCreation(flecha4),
                run_time=0.35
            )
        self.play(
            Uncreate(sine_function),
            Uncreate(lineacentro),
            run_time=2
        )        

ThreeDAxes(
    x_min=-10,
    x_max= 10,
    y_min=-10,
    y_max= 10,
    z_min=-10,
    z_max= 10,
)
class Onda3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(
            phi=0 * DEGREES,
            theta=90*DEGREES) #-90
        for i in range(0,10):
            x=i/2+1
            flecha1=Arrow([x,0,0], [x, 2*np.sin((x)/2), 0],color=BLUE)
            flecha2=Arrow([-x,0,0], [-x, -2*np.sin((x)/2), 0],color=RED)
            flecha3=Arrow([-x-6,0,0], [-x-6, 2*np.sin((x)/2), 0],color=BLUE)
            flecha4=Arrow([x+6,0,0], [x+6, -2*np.sin((x)/2), 0],color=RED)
            self.play(
                #ShowCreation(axes),
                ShowCreation(flecha1),
                ShowCreation(flecha2),
                ShowCreation(flecha3),
                ShowCreation(flecha4),
                run_time=0.01
            )        
        self.wait(2)
        func1 = lambda t: np.array([t,0,0])
        centro = ParametricFunction(func1,t_min=10,t_max=-10,color=DARK_GREY)
        self.play(
            ShowCreation(centro),
            run_time=2
        )        
        self.move_camera(
            phi=90*DEGREES,
            theta=90*DEGREES,  #-90
            run_time=3)
        for i in range(0,10):
            x=i/2+1
            flecha1=Arrow([x,0,0], [x,0, 2*np.sin((x)/2)],color=GREEN_D)
            flecha2=Arrow([-x,0,0], [-x,0, -2*np.sin((x)/2)],color=MAROON_D)
            flecha3=Arrow([-x-6,0,0], [-x-6,0, 2*np.sin((x)/2)],color=GREEN_D)
            flecha4=Arrow([x+6,0,0], [x+6,0, -2*np.sin((x)/2)],color=MAROON_D)
            self.play(
                ShowCreation(flecha1),
                ShowCreation(flecha2),
                ShowCreation(flecha3),
                ShowCreation(flecha4),
                run_time=0.1
            )
        self.move_camera(phi=65*DEGREES,theta=115*DEGREES,run_time=4)

class Particula(ThreeDScene):
    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 2*np.sin((x+dx)/2),
            x_min=-1.5*PI/2,x_max=8,
            color=WHITE
        )    
    def construct(self):
        title = TextMobject(
        "Campo Electrico")     
        title.to_edge(np.array([5.5,2,0]))
        title.scale(1.5)  
        sine_function=self.get_sine_wave()
        d_theta=ValueTracker(0)
        def update_wave(func):
            func.become(
                self.get_sine_wave(dx=d_theta.get_value())
            )
            return func
        sine_function.add_updater(update_wave)
        axes = ThreeDAxes()
#        circle=Circle(radius=2,arc_center=np.array([3,0,0]),color=WHITE)
        sphere = ParametricSurface(
            lambda u, v: np.array([
                0.5*np.cos(u)*np.cos(v)-3*PI/2,
                0.5*np.cos(u)*np.sin(v)-2,
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[BLUE_E, BLUE_D],
            resolution=(15, 32)).scale(1)        
        sphere_up = ParametricSurface(
            lambda u, v: np.array([
                0.5*np.cos(u)*np.cos(v)-3*PI/2,
                0.5*np.cos(u)*np.sin(v)+2,
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[BLUE_E, BLUE_D],
            resolution=(15, 32)).scale(1)
        sphere_down = ParametricSurface(
            lambda u, v: np.array([
                0.5*np.cos(u)*np.cos(v)-3*PI/2,
                0.5*np.cos(u)*np.sin(v)-2,
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[BLUE_E, BLUE_D],
            resolution=(15, 32)).scale(1)
        self.set_camera_orientation(phi=0 * DEGREES,theta=-90*DEGREES) #-90        
        #self.set_camera_orientation(phi=65 * DEGREES,theta=115*DEGREES)
        self.play(
        #ShowCreation(axes),
        Write(title),
        ShowCreation(sine_function),
        ShowCreation(sphere),
        run_time=3
        )
        tpart=2
        for i in range(0,6):
            self.play(
                d_theta.increment_value,2*PI,
                Transform(sphere,sphere_up),
                rate_func=linear,
                run_time=tpart
            )        
            self.play(
                d_theta.increment_value,2*PI,
                Transform(sphere,sphere_down),
                rate_func=linear,
                run_time=tpart
            )