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

class Snel(Scene):
    def construct(self):
        title1=TextMobject("Ley de refraccion/Snell").scale(2).to_edge(np.array([0,2.5,0]))   
        title2=TextMobject("$n_1sin\\theta_1=n_2sin\\theta_2$").scale(2).to_edge(np.array([0,0,0]))
        self.play(
            Write(title1),
            Write(title2),
            run_time=2
        )
        self.wait(2)
        self.play(
            FadeOut(title1),
            FadeOut(title2),
            run_time=2
        )        

class Mano(ThreeDScene):
    def construct(self):
        E=Arrow([0,0,0], [ -3,0,0],color=BLUE_C)    # centro
        B=Arrow([0,0,0], [ 0,0,3],color=RED_C)      # arriba
        P=Arrow([0,0,0], [ 0,3,0],color=GREEN)        # derecha
        axes = ThreeDAxes()
        #self.set_camera_orientation(phi=-45 * DEGREES,theta=45*DEGREES) #-90
        self.set_camera_orientation(phi=65 * DEGREES,theta=135*DEGREES) #-90
        self.play(
            #ShowCreation(axes),
            ShowCreation(E),
            ShowCreation(B),
            rate_func=linear,
            run_time=4
        )
        self.move_camera(phi=-65*DEGREES,theta=45*DEGREES,rate_func=linear,run_time=2)
        E1=Arrow([0,0,0], [ 0,0,-3],color=BLUE_C)    # centro
        B1=Arrow([0,0,0], [ 4,0,0],color=RED_C)      # arriba
        P1=Arrow([0,0,0], [ 0,4,0],color=GREEN)        # derecha        
        self.play(
            Transform(E,E1),
            Transform(B,B1),
            rate_func=linear,
            run_time=2
        )
        self.wait(2)
        self.play(
            ShowCreation(P1),
            rate_func=linear,
            run_time=4
        )

class Max(Scene):
    def construct(self):
        title1=TextMobject("Ecuaciones de Maxwell").scale(2)
        title2=TextMobject("Ecuaciones \\\\ de\\\\ Maxwell").scale(2)
        title3=TextMobject("$c\\leq 299,792,458~~ m/s$").scale(2)
        title4=TextMobject("Principio de Fermat").scale(2)
        self.play(
            Write(title1),
            run_time=2
        )
        self.play(
            FadeOut(title1),
            run_time=2
        )        
        self.play(
            Write(title2),
            run_time=2
        )        
        self.play(
            FadeOut(title2),
            run_time=2
        )
        self.play(
            Write(title3),
            run_time=2
        )        
        self.play(
            FadeOut(title3),
            run_time=2
        )           
        self.play(
            Write(title4),
            run_time=2
        )        
        self.play(
            FadeOut(title4),
            run_time=2
        )          

class sc1317(Scene):
    def construct(self):    
        title1=TextMobject("Ley de Snell").scale(2).to_edge(np.array([-2,2,0]))   
        title2=TextMobject("Willebrord Snell \\\\ Van Royen").scale(2).to_edge(np.array([-2.5,7,0]))   
        self.play(
            Write(title1),
            run_time=2
        )
        self.play(
            Write(title2),
            run_time=2
        )        

class textosv1(Scene):
    def construct(self):
        title1=TextMobject("Mecanica\\\\ ondulatoria").to_edge(np.array([-3,0,0]))   
        title2=TextMobject("Teoria \\\\ electromagnetica\\\\ de la luz").to_edge(np.array([-0,0,0]))  
        title3=TextMobject("Lentes \\\\ y \\\\ espejos").to_edge(np.array([4,0,0]))  
        self.play(
            Write(title1),
            Write(title2),
            Write(title3),
            run_time=3
        )
        self.play(
            FadeOut(title1),
            FadeOut(title2),
            FadeOut(title3),
            run_time=3
        )

class textosv3(Scene):
    def construct(self):    
        title1=TextMobject("LENTES").scale(2).to_edge(np.array([0,2,0]))   
        title2=TextMobject("Siglo XI D.C.").scale(1.5).to_edge(np.array([3,0,0]))   
        title3=TextMobject("Siglo VII A.C").scale(1.5).to_edge(np.array([-3,0,0]))   
        self.play(
            Write(title1),
            run_time=3
        )
        self.play(
            FadeOut(title1),
            run_time=3
        )
        self.play(
            Write(title2),
            Write(title3),
            run_time=3
        )
        self.play(
            FadeOut(title2),
            FadeOut(title3),
            run_time=3
        )                
        title4=TextMobject("Lentes \\\\ convexos").scale(1).to_edge(np.array([3,0,0]))   
        title5=TextMobject("Lentes \\\\ concavos").scale(1).to_edge(np.array([-3,0,0]))   
        self.play(
            Write(title4),
            Write(title5),
            run_time=3
        )
        self.play(
            FadeOut(title4),
            FadeOut(title5),
            run_time=3
        )       
        title6=TextMobject("Lentes convergentes").scale(2).to_edge(np.array([0,3,0]))   
        title7=TextMobject("Lentes divergentes").scale(2).to_edge(np.array([0,-3,0]))           
        self.play(
            Write(title6),
            Write(title7),
            run_time=3
        )
        self.play(
            FadeOut(title6),
            FadeOut(title7),
            run_time=3
        )
        title8=TextMobject("Focos").scale(2).to_edge(np.array([0,0,0]))   
        title9=TextMobject("Distancia focal").scale(2).to_edge(np.array([0,-3,0]))           
        title10=TextMobject("d").scale(1).to_edge(np.array([0,3,0])) 
        self.play(
            Write(title8),
            Write(title9),
            Write(title10),
            run_time=3
        )
        self.play(
            FadeOut(title8),
            FadeOut(title9),
            FadeOut(title10),
            run_time=3
        )        
        title11=TextMobject("$\\frac{1}{d}=P$").scale(2).to_edge(np.array([0,3,0]))   
        title12=TextMobject("Dioptrias").scale(2).to_edge(np.array([0,-3,0]))           
        self.play(
            Write(title11),
            Write(title12),
            run_time=3
        )
        self.play(
            FadeOut(title11),
            FadeOut(title12),
            run_time=3
        )       
        title13=TextMobject("Miopia").scale(2).to_edge(np.array([0,3,0]))   
        title14=TextMobject("Hipermetropia").scale(2).to_edge(np.array([0,-3,0]))           
        self.play(
            Write(title13),
            Write(title14),
            run_time=3
        )
        self.play(
            FadeOut(title13),
            FadeOut(title14),
            run_time=3
        )
        title15=TextMobject("P").scale(1).to_edge(np.array([0,-3,0]))   
        title16=TextMobject("P").scale(3).to_edge(np.array([0,3,0]))           
        self.play(
            Write(title15),
            run_time=3
        )
        self.play(
            Transform(title15,title16),
            run_time=4
        )        
        self.play(
            FadeOut(title15),
            run_time=2
        )
        title15=TextMobject("P").scale(1).to_edge(np.array([0,0,0]))   
        title16=TextMobject("P").scale(3).to_edge(np.array([0,0,0]))           
        self.play(
            Write(title15),
            run_time=3
        )
        self.play(
            Transform(title15,title16),
            run_time=4
        )        
        self.play(
            FadeOut(title15),
            run_time=2
        )        
        title17=TextMobject("$P=\\frac{1}{f}$").scale(2).to_edge(np.array([0,0,0]))             
        self.play(
            Write(title17),
            run_time=3
        )
        self.play(
            FadeOut(title17),
            run_time=3
        )   
        title18=TextMobject("Lente de Fresnel").scale(2).to_edge(np.array([0,3,0]))   
        title19=TextMobject("Agustin Jean Fresnel").scale(1).to_edge(np.array([0,-3,0]))           
        self.play(
            Write(title18),
            Write(title19),
            run_time=3
        )
        self.play(
            FadeOut(title18),
            FadeOut(title19),
            run_time=3
        )
class textosf(Scene):
    def construct(self):
        title1=TextMobject("P").scale(2).to_edge(np.array([-11,7.75,0]))
        title2=TextMobject("$=\\frac{1}{}$").scale(2).to_edge(np.array([0,0,0]))
        title3=TextMobject("f").scale(1.5).to_edge(np.array([12.8,-6,0]))
        title4=TextMobject("P").scale(3).to_edge(np.array([-10.5,7.25,0]))
        title5=TextMobject("f").scale(0.5).to_edge(np.array([12.85,-6,0]))
        title6=TextMobject("P").scale(1).to_edge(np.array([-11,8.25,0]))
        title7=TextMobject("f").scale(2).to_edge(np.array([12.8,-6,0]))                        
        self.play(
            Write(title1),
            Write(title2),
            Write(title3),
            run_time=3
        )
        self.play(
            Transform(title1,title4),
            Transform(title3,title5),
            run_time=3
        )
        self.play(
            Transform(title1,title6),
            Transform(title3,title7),
            run_time=3
        )        

class textosv3_2(Scene):
    def construct(self):
        title1=TextMobject("$\\frac{1}{x^2}$").scale(2).to_edge(np.array([0,0,0]))   
        title2=TextMobject("$x$").scale(2).to_edge(np.array([0,0,0]))           
        self.play(
            Write(title2),
            run_time=3
        )
        self.play(
            Transform(title2,title1),
            run_time=2
        )
        self.wait(1)
        self.play(
            FadeOut(title2),
            run_time=3
        )
        title3=TextMobject("Relatividad General").scale(2).to_edge(np.array([0,3,0]))   
        title4=TextMobject("$G_{\\mu \\nu}+\\Lambda g_{\\mu \\nu}=\\frac{8\\pi G}{c^4}T_{\\mu \\nu}$").scale(2).to_edge(np.array([0,-4,0]))           
        self.play(
            Write(title3),
            Write(title4),
            run_time=3
        )
        self.play(
            FadeOut(title3),
            FadeOut(title4),
            run_time=3
        )
        title5=TextMobject("Geodesica").scale(2).to_edge(np.array([0,3,0]))   
        title6=TextMobject("Lente gravitacional").scale(2).to_edge(np.array([0,-3,0]))           
        self.play(
            Write(title5),
            Write(title6),
            run_time=3
        )
        self.play(
            FadeOut(title5),
            FadeOut(title6),
            run_time=3
        )    
        title7=TextMobject("Albert Einstein").scale(1.5).to_edge(np.array([-3,-2,0]))   
        title8=TextMobject("1912").scale(2).to_edge(np.array([4,0,0]))           
        self.play(
            Write(title7),
            Write(title8),
            run_time=3
        )
        self.play(
            FadeOut(title8),
            run_time=3
        )
        self.play(
            FadeOut(title7),
            run_time=3
        )        
        title9=TextMobject("Espejos").scale(2).to_edge(np.array([-3,2,0]))   
        title10=TextMobject("Reflexion especular").scale(2).to_edge(np.array([3,0,0]))           
        title11=TextMobject("Imagen \\\\ virtual").scale(2).to_edge(np.array([-3,3,0]))           
        self.play(
            Write(title9),
            run_time=3
        )
        self.play(
            FadeOut(title9),
            run_time=3
        )                     
        self.play(
            Write(title10),
            run_time=3
        )
        self.play(
            FadeOut(title10),
            run_time=3
        )
        self.play(
            Write(title11),
            run_time=3
        )
        self.play(
            FadeOut(title11),
            run_time=3
        )
        title12=TextMobject("Espejos planos").scale(2).to_edge(np.array([0,3,0]))   
        title13=TextMobject("Espejos  curvos").scale(2).to_edge(np.array([0,3,0]))           
        title14=TextMobject("Espejos convexos").scale(2).to_edge(np.array([0,3,0]))           
        title15=TextMobject("Espejos concavos").scale(2).to_edge(np.array([0,3,0]))
        self.play(
            Write(title12),
            run_time=3
        )
        self.play(
            FadeOut(title12),
            run_time=3
        )                     
        self.play(
            Write(title13),
            run_time=3
        )
        self.play(
            FadeOut(title13),
            run_time=3
        )
        self.play(
            Write(title14),
            run_time=3
        )
        self.play(
            FadeOut(title14),
            run_time=3
        )                                     
        self.play(
            Write(title15),
            run_time=3
        )
        self.play(
            FadeOut(title15),
            run_time=3
        )          
        self.play(
            Write(title12),
            run_time=3
        )                        
        self.play(
            Transform(title12,title13),
            run_time=3
        )        
        self.play(
            Transform(title12,title14),
            run_time=3
        )
        self.play(
            Transform(title12,title15),
            run_time=3
        )                

class Constructiva(Scene):
    def get1_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 1*(np.sin(5*(x+dx)/2)-1),
            x_min=-8,x_max=8,
            color=BLUE_D
        )
    def get2_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 1*(np.sin(5*(x+dx)/2)-3),
            x_min=-8,x_max=8,
            color=YELLOW_C
        )
    def get3_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: (1*(np.sin(5*(x+dx)/2)+1*(np.sin(5*(x+dx)/2))))+2,
            x_min=-8,x_max=8,
            color=GREEN_B
        )
    def get4_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 1*(np.sin(5*(x+dx)/2)-1),
            x_min=-8,x_max=8,
            color=BLUE_D
        )
    def get5_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: -1*(np.sin(5*(x+dx)/2)+3),
            x_min=-8,x_max=8,
            color=YELLOW_C
        )
    def get6_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: (1*(np.sin(5*(x+dx)/2)-1*(np.sin(5*(x+dx)/2))))+2,
            x_min=-8,x_max=8,
            color=GREEN_B
        )
    def get7_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 1*(np.sin(2*(x+dx)/2)-1),
            x_min=-8,x_max=8,
            color=BLUE_D
        )
    def get8_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: -1*(np.sin(5*(x+dx)/2)+3),
            x_min=-8,x_max=8,
            color=YELLOW_C
        )
    def get9_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: (1*(np.sin(2*(x+dx)/2)-1)*(np.sin(5*(x+dx)/2)))+2,
            x_min=-8,x_max=8,
            color=GREEN_B
        )        
    def construct(self):
        sine1_function=self.get1_sine_wave()
        sine2_function=self.get2_sine_wave()
        sine3_function=self.get3_sine_wave()
        sine4_function=self.get4_sine_wave()
        sine5_function=self.get5_sine_wave()
        sine6_function=self.get6_sine_wave()  
        sine7_function=self.get7_sine_wave()
        sine8_function=self.get8_sine_wave()
        sine9_function=self.get9_sine_wave()                
        d_theta=ValueTracker(0)
        func1 = lambda t: np.array([t,2,0])
        func2 = lambda t: np.array([t,-1,0])
        func3 = lambda t: np.array([t,-3,0])
        centro1 = ParametricFunction(func1,t_min=-8,t_max=8,color=DARK_GREY)
        centro2 = ParametricFunction(func2,t_min=-8,t_max=8,color=DARK_GREY)
        centro3 = ParametricFunction(func3,t_min=-8,t_max=8,color=DARK_GREY)
        def update1_wave(func):
            func.become(
                self.get1_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update2_wave(func):
            func.become(
                self.get2_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update3_wave(func):
            func.become(
                self.get3_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update4_wave(func):
            func.become(
                self.get4_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update5_wave(func):
            func.become(
                self.get5_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update6_wave(func):
            func.become(
                self.get6_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update7_wave(func):
            func.become(
                self.get7_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update8_wave(func):
            func.become(
                self.get8_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update9_wave(func):
            func.become(
                self.get9_sine_wave(dx=d_theta.get_value())
            )
            return func                              
        sine1_function.add_updater(update1_wave)
        sine2_function.add_updater(update2_wave)
        sine3_function.add_updater(update3_wave)
        sine4_function.add_updater(update4_wave)
        sine5_function.add_updater(update5_wave)
        sine6_function.add_updater(update6_wave)
        sine7_function.add_updater(update7_wave)
        sine8_function.add_updater(update8_wave)
        sine9_function.add_updater(update9_wave)        
        self.play(
            ShowCreation(centro1),
            ShowCreation(centro2),
            ShowCreation(centro3),
            run_time=2
        )
        self.play(
            ShowCreation(sine7_function),
            ShowCreation(sine8_function),
            rate_func=linear,
            run_time=5
        )
        self.play(
            ShowCreation(sine9_function),
            rate_func=linear,
            run_time=5
        )
        self.play(
            d_theta.increment_value,4*PI,
            rate_func=linear,
            run_time=5
        )
        self.play(
            Uncreate(sine7_function),
            Uncreate(sine8_function),
            Uncreate(sine9_function),
            run_time=3
        )
        self.play(
            ShowCreation(sine1_function),
            ShowCreation(sine2_function),
            rate_func=linear,
            run_time=5
        )
        self.play(
            ShowCreation(sine3_function),
            rate_func=linear,
            run_time=5
        )
        self.play(
            d_theta.increment_value,4*PI,
            rate_func=linear,
            run_time=5
        )
        self.play(
            Uncreate(sine1_function),
            Uncreate(sine2_function),
            Uncreate(sine3_function),
            run_time=3
        )
        self.play(
            ShowCreation(sine4_function),
            ShowCreation(sine5_function),
            rate_func=linear,
            run_time=5
        )
        self.play(
            ShowCreation(sine6_function),
            rate_func=linear,
            run_time=5
        )
        self.play(
            d_theta.increment_value,4*PI,
            rate_func=linear,
            run_time=5
        )        

class Choque(Scene):
    def get1_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: -1 if x-dx/2<(-4/2.75)*np.pi else(3*(np.sin(2.75*(x-dx/2)/2))-1 if x-dx/2<(-2/2.75)*np.pi else -1 ),
            x_min=-8,x_max=8,
            color=WHITE
        )
    def get2_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: -1 if x+dx/2<(4/2.75)*np.pi else(3*(np.sin(2.75*(x+dx/2)/2))-1 if x+dx/2<(6/2.75)*np.pi else -1 ),
            x_min=8,x_max=-8,
            color=WHITE
        )
    def construct(self):
        sine1_function=self.get1_sine_wave()
        sine2_function=self.get2_sine_wave()        
        d_theta=ValueTracker(0)
        func1 = lambda t: np.array([t,0,0])
        cenro1 = ParametricFunction(func1,t_min=-8,t_max=8,color=DARK_GREY)        
        def update1_wave(func):
            func.become(
                self.get1_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update2_wave(func):
            func.become(
                self.get2_sine_wave(dx=d_theta.get_value())
            )
            return func            
        sine1_function.add_updater(update1_wave)
        sine2_function.add_updater(update2_wave)
        self.play(
            ShowCreation(sine1_function),
            ShowCreation(sine2_function),
            rate_func=linear,
            run_time=2
        )
        self.play(
            d_theta.increment_value,8*PI,
            rate_func=linear,
            run_time=5
        )

class Choquesum(Scene):
    def get1_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: -1 if x-dx/4<=(-4/2.75)*np.pi else(2.25*(np.sin(2.75*(x-dx/4)/2))-1 if x-dx/4<=(-2/2.75)*np.pi else -1 ),
            x_min=-8,x_max=8,
            color=WHITE
        )
    def get2_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: -1 if x+dx/4<=(4/2.75)*np.pi else(2.25*(np.sin(2.75*(x+dx/4)/2))-1 if x+dx/4<=(6/2.75)*np.pi else -1 ),
            x_min=8,x_max=-8,
            color=WHITE
        )
    def get3_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: (2.25*(np.sin(2.75*(x+dx/4)/2))+2.25*(np.sin(2.75*(x-dx/4)/2)))-1,
            x_min=0,x_max=0.75*np.pi,
            color=RED_C
        )        
    def construct(self):
        sine1_function=self.get1_sine_wave()
        sine2_function=self.get2_sine_wave()    
        sine3_function=self.get2_sine_wave()
        d_theta=ValueTracker(0)        
        func1 = lambda t: np.array([0.75*np.pi,t,0])
        cenro1 = ParametricFunction(func1,t_min=-8,t_max=8,color=DARK_GREY)
        func2 = lambda t: np.array([-0*np.pi,t,0])
        cenro2 = ParametricFunction(func2,t_min=-8,t_max=8,color=DARK_GREY)                
        def update1_wave(func):
            func.become(
                self.get1_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update2_wave(func):
            func.become(
                self.get2_sine_wave(dx=d_theta.get_value())
            )
            return func
        def update3_wave(func):
            func.become(
                self.get3_sine_wave(dx=d_theta.get_value())
            )
            return func
        sine1_function.add_updater(update1_wave)
        sine2_function.add_updater(update2_wave)
        sine3_function.add_updater(update3_wave)
        self.play(
            ShowCreation(sine1_function),
            ShowCreation(sine2_function),
            ShowCreation(sine3_function),
            rate_func=linear,
            run_time=2
        )
        self.play(
            d_theta.increment_value,10*PI,
            rate_func=linear,
            run_time=10
        )        
        self.wait(2)

class Derecha(Scene):
    def get1_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: 0 if x-dx/2<=(-4/1.75)*np.pi else(3.5*(np.sin(1.75*(x-dx/2)/2)) if x-dx/2<=(-2/1.75)*np.pi else 0 ),
            x_min=-8,x_max=8,
            color=WHITE
        )
    def construct(self):
        sine1_function=self.get1_sine_wave()
        d_theta=ValueTracker(0)
        func1 = lambda t: np.array([t,3.5*(np.sin(3.5*(t/2)/2)),0])
        onda1 = ParametricFunction(func1,t_min=-2*np.pi,t_max=2*np.pi,color=WHITE)
        func2 = lambda t: np.array([t,-3.5*(np.sin(3.5*(t/2)/2)),0])
        onda2 = ParametricFunction(func2,t_min=-2*np.pi,t_max=2*np.pi,color=WHITE)
        func3 = lambda t: np.array([t,3.5*(np.sin(3.5*(t/2)/2)),0])
        onda3 = ParametricFunction(func3,t_min=-2*np.pi,t_max=2*np.pi,color=WHITE)
        def update1_wave(func):
            func.become(
                self.get1_sine_wave(dx=d_theta.get_value())
            )
            return func
        sine1_function.add_updater(update1_wave)
        self.play(
            ShowCreation(sine1_function),
            rate_func=linear,
            run_time=2
        )
        self.play(
            d_theta.increment_value,4*PI,
            rate_func=linear,
            run_time=4
        )
        self.play(
            Uncreate(sine1_function),
            run_time=3
        )
        self.play(
            ShowCreation(onda1),
            run_time=3
        )
        for i in range(0,3):
            self.play(
                Transform(onda1,onda2),
                rate_func=linear,
                run_time=2
            )
            self.play(
                Transform(onda1,onda3),
                rate_func=linear,
                run_time=2
            )        

class Fourier(Scene):
    def construct(self):
        title1=TextMobject("Transformada \\\\ de \\\\ Fourier").scale(2).to_edge(np.array([0,2,0]))
        title2=TextMobject("$\\int_{-\\infty}^\\infty f(x)e^{-i\\omega t}dt$").scale(2).to_edge(np.array([0,-2,0]))
        title3=TextMobject("$\\int \\limits_{-\\infty}^{\\infty} f(x)e^{-i\\omega t}dt$").scale(2).to_edge(np.array([0,-2,0]))
        
        self.play(
            Write(title1),
            Write(title2),
            run_time=3
        )