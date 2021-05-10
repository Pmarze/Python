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

class Reflexion(Scene):
    def construct(self):
        title1=TextMobject("Ley de Reflexion").scale(2).to_edge(np.array([0,2.5,0]))
        title2=TextMobject("$\\theta_1=\\theta_2$").scale(2).to_edge(np.array([0,0,0]))      
        title3=TextMobject("$15^\\circ=15^\\circ$").scale(2).to_edge(np.array([0,0,0]))
        title4=TextMobject("$18^\\circ=18^\\circ$").scale(2).to_edge(np.array([0,0,0]))
        title5=TextMobject("$58^\\circ=58^\\circ$").scale(2).to_edge(np.array([0,0,0]))
        title6=TextMobject("$50^\\circ=50^\\circ$").scale(2).to_edge(np.array([0,0,0]))
        tiempo=1.5
        self.play(
            Write(title1),
            Write(title2),
            run_time=3
        )
        self.play(
            Transform(title2,title3),
            run_time=tiempo
        )
        self.play(
            Transform(title2,title),
            run_time=tiempo
        )        
        self.play(
            Transform(title2,title5),
            run_time=tiempo
        )
        self.play(
            Transform(title2,title6),
            run_time=tiempo
        )                    

class N1N2(Scene):
    def construct(self):                
        func00 = lambda t: np.array([t,0,0])
        func01 = lambda t: np.array([0,t,0])
        graph00 = ParametricFunction(func00,t_min=-7,t_max=7,color=DARK_GREY)
        graph01 = ParametricFunction(func01,t_min=-4,t_max=4,color=DARK_GREY)
        func1 = lambda t: np.array([t,(-3/4)*t,0])
        graph1 = ParametricFunction(func1,t_min=-7,t_max=0,color=WHITE)
        func2 = lambda t: np.array([t,(-3/2)*t,0])
        graph2 = ParametricFunction(func2,t_min=0,t_max=7,color=WHITE)
        
        title1=TextMobject("$\\theta_1$").to_edge(np.array([-13,6,0]))
        title2=TextMobject("$\\theta_2$").to_edge(np.array([-15,11,0]))
        title3=TextMobject("$N_1$").scale(2).to_edge(np.array([-4,4,0]))
        title4=TextMobject("$N_2$").scale(2).to_edge(np.array([-4,-4,0]))
        title5=TextMobject("$\\theta_1$").scale(2).to_edge(np.array([8,3,0]))
        title6=TextMobject("$\\theta_2$").scale(2).to_edge(np.array([4,3,0]))
        title7=TextMobject("$\\neq$").scale(2).to_edge(np.array([6,3,0]))
        title8=TextMobject("$sin\\theta_1$").scale(1.5).to_edge(np.array([9,3,0]))
        title9=TextMobject("$\\longleftrightarrow$").scale(1.5).to_edge(np.array([6,3,0]))
        title10=TextMobject("$sin\\theta_2$").scale(1.5).to_edge(np.array([2,3,0]))                
        title11=TextMobject("$sin\\theta_1$",color=RED_E).scale(1.5).to_edge(np.array([9,3,0]))
        title12=TextMobject("$sin\\theta_2$",color=BLUE_E).scale(1.5).to_edge(np.array([2,3,0]))
        func3 = lambda t: np.array([0,t,0])
        graph3 = ParametricFunction(func3,t_min=0,t_max=4,color=RED_E)        
        func4 = lambda t: np.array([0,t,0])
        graph4 = ParametricFunction(func4,t_min=0,t_max=-4,color=BLUE_E)                
        tiempo=2
        self.play(
            ShowCreation(graph00),
            ShowCreation(graph01),
            rate_func=linear,
            run_time=tiempo
        )        
        self.play(
            ShowCreation(graph1),
            rate_func=linear,
            run_time=tiempo
        )
        self.play(
            ShowCreation(graph2),
            rate_func=linear,
            run_time=tiempo*0.5
        )        
        self.play(
            Write(title1),
            Write(title2),
            Write(title3),
            Write(title4),
            run_time=2
        )
        self.play(
            Transform(title1,title5),
            Transform(title2,title6),
            run_time=2
        )
        self.play(
            Write(title7),
            run_time=2
        )
        self.play(
            Transform(title1,title8),
            Transform(title2,title10),
            Transform(title7,title9),            
            run_time=2
        )
        self.wait(2)
        self.play(
            Transform(title1,title11),
            Transform(title2,title12),
            ShowCreation(graph3),
            ShowCreation(graph4),
            run_time=3
        ) 
        self.play(
            #FadeOut(title1),
            #FadeOut(title2),
            FadeOut(title3),
            FadeOut(title4),
            #FadeOut(title7),
            FadeOut(graph00),
            FadeOut(graph01),
            FadeOut(graph1),
            FadeOut(graph2),
            FadeOut(graph3),
            FadeOut(graph4),
            run_time=2
        )      
        title13=TextMobject("$n_1sin\\theta_1$").scale(1.5).to_edge(np.array([-8,0,0]))
        title14=TextMobject("$=$").scale(1.5).to_edge(np.array([0,0,0]))
        title15=TextMobject("$n_2sin\\theta_2$").scale(1.5).to_edge(np.array([8,0,0]))         
        self.play(
            Transform(title1,title13),
            Transform(title2,title15),
            Transform(title7,title14),
            run_time=2
        )
        title16=TextMobject("$n_i=\\frac{c}{v_i}$").scale(2.5).to_edge(np.array([-5,0,0]))        
        title17=TextMobject("Vel. de la luz \\\\ en el vacio \\\\ Vel. de la luz \\\\ en el medio").scale(1.5).to_edge(np.array([5,0,0]))        
        self.wait(2)
        self.play(
            Transform(title1,title16),
            Transform(title2,title17),
            FadeOut(title7),
            run_time=2
        )
        self.wait(2)
        title18=TextMobject("Angulo de \\\\ redireccion").scale(2).to_edge(np.array([-3,2,0]))
        title19=TextMobject("$\\theta_2=\\frac{n_1sen\\theta_1}{n_2}$").scale(2).to_edge(np.array([0,0,0]))
        self.play(
            Write(title18),
            Transform(title1,title19),
            FadeOut(title2),
            run_time=2
        )        
        self.wait(2)