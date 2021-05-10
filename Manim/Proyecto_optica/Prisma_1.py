# Comando para ejecutar el programa y exportar video de muestra 
# en baja resolución, este además, muestra la lista de objetos
# a exportar, se elije ingresando el número correspondiente.
# python -m manim Prisma_1.py -pl
# Comando para ejecutar el programa y exportar todos los objetos
# en alta calidad.
# python -m manim Prisma_1.py -p

from big_ol_pile_of_manim_imports import *
import numpy as np

class Caminos(Scene):
    def construct(self):
        A=Dot((-2,0,0),color=GREY)
        B=Dot((2,0,0),color=GREY)
        C=Dot((-1,0,0),color=GREY)
        D=Dot((1,0,0),color=GREY)
        E=Dot((-4,0,0),color=GREY)
        F=Dot((4,0,0),color=GREY)
        circulo=Circle(color=GREY,radius=2)
        func1 = lambda t: np.array([t,np.sin(1.535*t),0])
        func2 = lambda t: np.array([t,2-0.5*t**2,0])
        func3 = lambda t: np.array([t,-0.5*t-1,0]) if t<=0 else np.array([t,0.5*t-1,0])
        func4 = lambda t: np.array([t,0,0])
        graph1 = ParametricFunction(func1,t_min=-2,t_max=2,color=WHITE)
        graph2 = ParametricFunction(func2,t_min=-2,t_max=2,color=WHITE)
        graph3 = ParametricFunction(func3,t_min=-2,t_max=2,color=WHITE)
        graph4 = ParametricFunction(func4,t_min=-2,t_max=2,color=WHITE)

        self.play(
            ShowCreation(A),
            ShowCreation(B),
            run_time=2
        )
        self.play(
            ShowCreation(graph1),
            run_time=5
        )
        self.play(
            Uncreate(graph1),
            run_time=1
        )
        self.play(
            ShowCreation(graph2),
            run_time=5.5
        )
        self.play(
            Uncreate(graph2),
            run_time=1
        )
        self.play(
            ShowCreation(graph3),
            run_time=4
        )
        self.play(
            Uncreate(graph3),
            run_time=1
        )
        self.play(
            ShowCreation(graph4),
            run_time=3
        )
        self.play(
            FadeOut(graph4),
            run_time=2
        )
        self.play(
            ShowCreation(circulo),
            Transform(A,C),
            Transform(B,D),
            run_time=3
        )
        camino1_1=Line([-1,0,0],[0,2,0],color=WHITE)
        camino1_2=Line([0,2,0],[1,0,0],color=WHITE)
        camino2_1=Line([-1,0,0],[-0.5,-np.sqrt(15)/2,0],color=WHITE)
        camino2_2=Line([-0.5,-np.sqrt(15)/2,0],[0.5,-np.sqrt(15)/2,0],color=WHITE)
        camino2_3=Line([0.5,-np.sqrt(15)/2,0],[1,0,0],color=WHITE)
        camino3_1=Line([-1,0,0],[-2,0,0],color=WHITE)
        camino3_2=Line([-2,0,0],[np.sqrt(3),-1,0],color=WHITE)
        camino3_3=Line([np.sqrt(3),-1,0],[1,0,0],color=WHITE)
        self.play(
            ShowCreation(camino1_1),
            ShowCreation(camino2_1),
            ShowCreation(camino3_1),
            run_time=2
        )
        self.play(
            ShowCreation(camino1_2),
            ShowCreation(camino2_2),
            ShowCreation(camino3_2),
            run_time=2
        )
        self.play(
            ShowCreation(camino2_3),
            ShowCreation(camino3_3),
            run_time=2
        )             
        self.play(
            FadeOut(camino2_1),
            FadeOut(camino2_2),
            FadeOut(camino2_3),
            FadeOut(camino3_1),
            FadeOut(camino3_2),
            FadeOut(camino3_3),            
            run_time=3
        )
        self.play(
            FadeOut(camino1_1),
            FadeOut(camino1_2),
            FadeOut(circulo),
            Transform(A,E),
            Transform(B,F),
            run_time=3
        )        
        func5 = lambda t: np.array([-0.5,t,0])
        func6 = lambda t: np.array([0.5,t,0])        
        graph5 = ParametricFunction(func5,t_min=-4,t_max=4,color=BLUE_E)
        graph6 = ParametricFunction(func6,t_min=-4,t_max=4,color=BLUE_E)
        self.play(
            ShowCreation(graph5),
            ShowCreation(graph6),
            run_time=3
        )
        self.wait(2)
        
        func1_1 = lambda t: np.array([t,(4/7)*(t+4),0])
        func1_2 = lambda t: np.array([t,2,0])
        func1_3 = lambda t: np.array([t,(-4/7)*(t-4),0])
        graph1_1 = ParametricFunction(func1_1,t_min=-4,t_max=-0.5,color=WHITE)
        graph1_2 = ParametricFunction(func1_2,t_min=-0.5,t_max=0.5,color=WHITE)
        graph1_3 = ParametricFunction(func1_3,t_min=0.5,t_max=4,color=WHITE)
        func2_1 = lambda t: np.array([t,0,0])
        func2_2 = lambda t: np.array([t,-(t+0.5),0])
        func2_3 = lambda t: np.array([t,(2/7)*t-1.15,0])
        graph2_1 = ParametricFunction(func2_1,t_min=-4,t_max=-0.5,color=WHITE)
        graph2_2 = ParametricFunction(func2_2,t_min=-0.5,t_max=0.5,color=WHITE)
        graph2_3 = ParametricFunction(func2_3,t_min=0.5,t_max=4,color=WHITE)
        func3_1 = lambda t: np.array([t,(-4/7)*t-16/7,0])
        func3_2 = lambda t: np.array([t,0.5*t-1.75,0])
        func3_3 = lambda t: np.array([t,(3/7)*t-1.71,0])
        graph3_1 = ParametricFunction(func3_1,t_min=-4,t_max=-0.5,color=WHITE)
        graph3_2 = ParametricFunction(func3_2,t_min=-0.5,t_max=0.5,color=WHITE)
        graph3_3 = ParametricFunction(func3_3,t_min=0.5,t_max=4,color=WHITE)                
        self.play(
            ShowCreation(graph1_1),
            ShowCreation(graph2_1),
            ShowCreation(graph3_1),
            rate_func=linear,
            run_time=3
        )
        self.play(
            ShowCreation(graph1_2),
            ShowCreation(graph2_2),
            ShowCreation(graph3_2),
            rate_func=linear,
            run_time=1
        )
        self.play(
            ShowCreation(graph1_3),
            ShowCreation(graph2_3),
            ShowCreation(graph3_3),
            rate_func=linear,
            run_time=3
        )
        self.wait(2)
        self.play(
            FadeOut(graph2_1),
            FadeOut(graph2_2),
            FadeOut(graph2_3),
            FadeOut(graph3_1),
            FadeOut(graph3_2),
            FadeOut(graph3_3),
            run_time=3
        )