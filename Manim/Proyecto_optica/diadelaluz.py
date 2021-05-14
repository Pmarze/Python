from os import write
from manimlib import *
import numpy as np

#Lo siguiente no necesita ser renderizado
class DrawLine(Scene):
    def construct(self):
        START = (-10,0,0)
        END =   (10,0,0)
        ang1 = (-2,3,0)
        origen = (0,0,0)
        ang12 = (0,3,0)
        ang2 = (0,-3,0)
        ang21 = (1,-3,0)
        line = Line(START,END);
        self.play(ShowCreation(line))
        line2 = Line(ang1, origen);
        self.play(ShowCreation(line2))
        line3 = Line(ang12, origen);
        self.play(ShowCreation(line3))
        line4 = Line(ang2, origen);
        self.play(ShowCreation(line4))
        line5 = Line(ang21, origen);
        self.play(ShowCreation(line5))
        angle = math.radians(90)
        arc =  Arc(radius=0.3,angle=angle)
        self.play(ShowCreation(arc))
        
#maningl diadelaluz.py storyboard1
# To watch one of these scenes, run the following:
# manimgl diadelaluz.py <nombre de la escena> 
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.



class escena01_06(Scene):
    def construct(self):
        text1 = Text('Mecánica Ondulatoria',font="Consolas",font_size=20)
        text2 = Text('Teoría Electromagnética',font="Consolas",font_size=20)
        text3 = Text('Óptica: lentes y espejos',font="Consolas",font_size=20)
        posicion1 = np.array([-5,1,0])
        posicion2 = np.array([0,-1,0])
        posicion3 = np.array([5,-3,0])
        text1.move_to(posicion1)
        text2.move_to(posicion2)
        text3.move_to(posicion3)
        self.play(Write(text1),Write(text2),Write(text3))
        self.wait(3)

class escena01_03(Scene):
    def construct(self):
        text1 = Text('Movimiento armónico simple',font="Consolas",font_size=70)
        posicion = np.array([0,3,0])
        text1.move_to(posicion)
        self.play(FadeIn(text1, UP))
        self.wait(3)
        
class escenas02_05to02_06(Scene):
    def construct(self):
        text1 = Text('Periodicidad',font="Consolas",font_size=50)
        text2 = Text('Hay un punto de equilibrio',font="Consolas",font_size=50)
        posicion = np.array([-3.5,3.5,0])
        text1.move_to(posicion)
        text2.move_to(posicion)
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))
        self.wait(2)

class escena03_01(Scene):
    def construct(self):
        start = (0,-3,0)
        end = (0,3,0)
        dashedLine = DashedLine(start,end)
        self.play(Write(dashedLine))
        self.wait()
        rect = Rectangle(height=1.5,width=1.5)
        self.play(ShowCreation(rect))
        self.wait()

        q1 = (2,-0.75,0)
        q2 = (-4,-0.75,0)
        line = Line(q1,q2);
        self.play(ShowCreation(line))

        q3 = (-4,0.5,0)
        line2 = Line(q2,q3)
        self.play(ShowCreation(line2))

        inicio = (-2,2,0)
        final = (2,2,0)
        arrow = Arrow(inicio,final)
        self.play(Write(arrow))
        self.wait()
        text = Text('F',font="Consolas",font_size=50)
        asd = np.array([2,2.5,0])
        text.move_to(asd)
        self.play(Write(text))


        arrow2= Arrow((4,0.5,0),(2,0.5,0))
        self.play(Write(arrow2))
        self.wait()
        text1 = Text('No fricción',font="Consolas",font_size=50)
        posicion1 = np.array([-3,-3,0])
        text1.move_to(posicion1)
        self.play(Write(text1))
        text2 = Text('No pérdida\nde energía',font="Consolas",font_size=50)
        posicion2 = np.array([3,-3,0])
        text2.move_to(posicion2)
        self.play(Write(text2))

class escena03_03(Scene):
    def construct(self):
        texto = Text('"Acoplados"',font="Consolas",font_size=70)
        pos = np.array([0,3.2,0])
        texto.move_to(pos)
        self.play(Write(texto))
        self.wait()

class escena03_05(Scene):
    def construct(self):
        texto = Text('Onda mecánica',font="Consolas",font_size=70)
        pos = np.array([0,3.2,0])
        texto.move_to(pos)
        self.play(Write(texto))
        self.wait()

class escena04_02to04_03(Scene):
    def construct(self):
        texto = Text('Ondas longitudinales',font="Consolas",font_size=30)
        texto2 = Text('Paralelo',font="Consolas",font_size=30)
        pos = np.array([0,-3.6,0])
        pos2 = np.array([0,3.6,0])
        texto.move_to(pos)
        texto2.move_to(pos2)
        self.play(Write(texto),Write(texto2))
        #arrow2= Arrow((-2,3.6,0),(-1,3.6,0))
        #self.play(Write(arrow2))
        #self.wait()
        #arrow= Arrow((0.9,3.6,0),(1.9,3.6,0))
        #self.play(Write(arrow))
        #self.wait()
        self.play(FadeOut(texto),FadeOut(texto2))
        texto3 = Text('Perpendiculares',font="Consolas",font_size=30)
        texto4 = Text('Ondas Transversales',font="Consolas",font_size=30)
        texto3.move_to(pos2)
        texto4.move_to(pos)
        self.play(FadeIn(texto3),FadeIn(texto4))
        self.wait()

class escena04_11(Scene):
    def construct(self):
        titulo = Text("ONDAS LONGITUDINALES\n\n\t\t + \n\n ONDAS TRANSVERSALES",font="Consolas",font_size=60)
        self.play(FadeIn(titulo))
        self.wait(3)
        self.play(FadeOut(titulo))
        self.wait()

class escenas05_07to05_08(Scene):
    def construct(self):
        titulo = Text("Amplitud",font="Consolas",font_size=90)
        letra = Text("A",font="Consolas",font_size=90)
        aa = Text("A",font="Consolas",font_size=90)
        titulo.to_edge(UP)
        aa.to_edge(LEFT)
        self.play(Write(titulo),FadeIn(letra))
        self.wait(3)
        self.play(Transform(letra,aa))
        self.play(FadeOut(titulo))
        self.wait(2)
        valles = (
            Text('valles',font="Consolas",font_size=17),
            Text('valles',font="Consolas",font_size=17),
            Text('valles',font="Consolas",font_size=17),
            Text('valles',font="Consolas",font_size=17)
        )
        posicion1 = np.array([-1,1,0])
        posicion2 = np.array([4,1,0])
        posicion3 = np.array([-1,-3.6,0])
        posicion4 = np.array([4,-3.6,0])
        valles[0].move_to(posicion1)
        valles[1].move_to(posicion2)
        valles[2].move_to(posicion3)
        valles[3].move_to(posicion4)
        crestas = (
            Text('crestas',font="Consolas",font_size=17),
            Text('crestas',font="Consolas",font_size=17),
            Text('crestas',font="Consolas",font_size=17),
            Text('crestas',font="Consolas",font_size=17)
        )
        pos1 = np.array([1,3.6,0])
        pos3 = np.array([1,-1,0])
        pos4 = np.array([5,-1,0])
        crestas[0].move_to(pos1)
        crestas[1].to_edge(RIGHT+UP)
        crestas[2].move_to(pos3)
        crestas[3].move_to(pos4)
        self.play(FadeIn(valles[0]),FadeIn(valles[1]),FadeIn(valles[2]),FadeIn(valles[3]))
        self.play(FadeIn(crestas[0]),FadeIn(crestas[1]),FadeIn(crestas[2]),FadeIn(crestas[3]))
        self.wait()






class test(Scene):
    def construct(self):
        text = Text("some text.")
        text1 = Text("another text.")
        text2 = Text("its some text.")
        rect = Rectangle()
        circle = Circle()
        text.to_edge(UP)
        text1.move_to(text.get_corner(LEFT+DOWN)-np.array([text1.get_corner(LEFT+UP)]))
        text2.move_to(text1.get_corner(LEFT+DOWN)-np.array([text2.get_corner(LEFT+UP)]))
        rect.next_to(text1,DOWN)
        circle.next_to(rect,RIGHT)
        self.add(text)
        self.play(Transform(text,text1))
        self.play(Transform(text, text2))
        self.play(Transform(text, VGroup(rect,circle)))
        self.wait()
       


class escenas05_10to05_11(Scene):
    def construct(self):
        titulo = Text("Longitud de onda",font="Consolas",font_size=90)
        lam = Tex("\\lambda",font_size=110)
        aa = Tex("\\lambda",font_size=110)
        titulo.to_edge(UP)
        aa.to_edge(LEFT)
        self.play(Write(titulo),FadeIn(lam))
        self.wait(3)
        self.play(Transform(lam,aa))
        self.play(FadeOut(titulo))
        self.wait(2)


class escenas05_11to05_14(Scene):
    def construct(self):
        titulo = Text("Frecuencia",font="Consolas",font_size=90)
        lam = Tex("f",font_size=110)
        aa = Tex("f",font_size=110)
        asd = Tex("f=4",font_size=110)
        titulo.to_edge(UP)
        aa.to_edge(LEFT)
        self.play(Write(titulo),FadeIn(lam))
        self.wait(3)
        self.play(FadeOut(titulo))
        self.play(Transform(lam,aa))
        self.wait()
        self.clear()
        self.play(Transform(aa,asd.to_edge(LEFT)))
        self.wait(2)
        second = Tex("f\\longleftrightarrow\\lambda",font_size=110)
        self.clear()
        self.play(Transform(asd,second))
        self.wait()
        self.clear()
        vel1 = VGroup(
            Tex("v=", font_size=110
            ,t2w={"v": BOLD}),
            Tex("\\lambda", font_size=100),
            Tex("f",font_size=110),
            )

        vel2 = VGroup(
            Tex("\\lambda", font_size=20),
            Tex("f",font_size=190),
            Tex("\\lambda", font_size=190),
            Tex("f",font_size=20),
        )
        a1 = np.array([-1,0,0])
        a2 = np.array([0.35,0,0])
        a3 = np.array([1.1,0,0])
        vel1[0].move_to(a1)
        vel1[1].move_to(a2)
        vel1[2].move_to(a3)
        
        vel2[0].move_to(a2)
        vel2[1].move_to(a3)
        vel2[2].move_to(a2)
        vel2[3].move_to(a3)
        self.play(Transform(second,vel1))
        self.wait()
        self.clear()
        self.add(vel1[0],vel1[1],vel1[2])
        self.wait()
        self.play(Transform(vel1[1],vel2[0]),Transform(vel1[2],vel2[1]))
        self.wait(2)
        self.clear()
        self.add(vel1[0],vel2[0],vel2[1])
        self.play(Transform(vel2[0],vel2[2]),Transform(vel2[1],vel2[3]))
        self.wait()


class escena06_02to07_02(Scene):
    def construct(self):
        eq = Tex("\\frac{\\partial^2 u}{\\partial t^2}=v^2\\nabla^2u",font_size=90)
        eq2 = Tex("\\frac{\\partial^2 u}{\\partial t^2}=v^2\\nabla^2u",font_size=90)
        titulo = Text('Ecuación de onda',font='Consolas',font_size=90)
        titulo.to_edge(UP)
        VGroup(titulo, eq).arrange(DOWN, buff=1)
        self.play(FadeIn(eq,UP),Write(titulo))
        self.wait()
        self.play(FadeOut(titulo,UP))
        eq2.to_edge(LEFT)
        self.play(Transform(eq,eq2))
        nombre = Text("Jean D'Alembert",font_size=35)
        nombre.to_edge(RIGHT+DOWN)
        self.play(Write(nombre))
        self.wait()
        arrow1 = Arrow((-5,2.1,0),(-6,1,0))
        eq1 = Text("Variación del medio\nen el tiempo",font_size=20)
        eq1.move_to((-5,2.3,0))
        arrow2 = Arrow((-3.5,-0.3,0),(-3.5,-2,0))
        eq2 = Text("Velocidad de\nla perturbación",font_size=20)
        eq2.move_to((-3.5,-2,0))
        arrow3 = Arrow((-2,0.5,0),(-1,2,0))
        eq3 = Text('Variación del medio \nen el espacio',font_size=20)
        eq3.move_to((-1,2.2,0))
        self.play(ShowCreation(arrow1),Write(eq1),ShowCreation(arrow2),Write(eq2),ShowCreation(arrow3),Write(eq3))
        self.wait(3)
        self.clear()
        tit = Text('Ondas senoidales',font='Consolas',font_size=70)
        tit.to_edge(UP)
        VGroup(tit).arrange(LEFT, buff=1)
        self.play(Write(tit.to_edge(UP)))
        self.wait()
        self.play(FadeOut(tit))
        titulo2 = Text('Ondas planas',font_size=70)
        titulo2.to_edge(UP)
        self.play(FadeIn(titulo2,UP))


class escena08_02(Scene):
    def construct(self):
        titulo = Text(" Principio de\n\n superposición",font_size=110)
        self.play(FadeIn(titulo,DOWN))

class escena10_07(Scene):
    def construct(self):
        nombre = Text('Joseph Fourier',font_size=40)
        nombre.to_edge(RIGHT+DOWN)
        self.play(Write(nombre))
        self.wait()
        self.clear()
        eq = Tex('\\int_{-\infty}^{\\infty}f_{(x)}e^{-iwt}dt',font_size=70)
        eq.to_edge(DOWN+RIGHT)
        nombre2 = Text('Transformada\n     de\n   Fourier',font_size=50)
        self.play(TransformMatchingShapes(nombre,nombre2.to_edge(RIGHT+UP)),Write(eq))
    
