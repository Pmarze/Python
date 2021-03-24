# Comando para ejecutar el programa y exportar video de muestra 
# en baja resolución, este además, muestra la lista de objetos
# a exportar, se elije ingresando el número correspondiente.
# python -m manim SoloTexto.py -pl
# Comando para ejecutar el programa y exportar todos los objetos
# en alta calidad.
# python -m manim SoloTexto.py -pa
from big_ol_pile_of_manim_imports import *

class AbajoArriba(Scene):
    def construct(self):
        title = TextMobject(
        "Texto centrado \\\\"           # Salto de línea con \\\\
        " fade de arriba \\\\"
        "hacia abajo")
        self.play(
            FadeInFrom(title, UP),      # de arriba hacia abajo el parámetro es DOWN
            run_time=3                  # La duración de la animación es 3s
        )
        self.wait()

class DerechaIzquierda(Scene):
    def construct(self):
        title = TextMobject(
        "Texto centrado \\\\"
        " fade de derecha \\\\"
        "a izquierda")
        self.play(
            FadeInFrom(title, RIGHT),   # de izquierda a derecha el parámetro es LEFT
            run_time=2                  # La duración de la animación es 2s
        )
        self.wait(3)                    # Se mantiene en la escena durante 3s

class Distribucion(Scene):
    def construct(self):
        title = TextMobject("Titulo en texto")
        p1 = TexMobject("Texto 1 fade desde arriba")
        p2 = TexMobject("Texto \\phantom{5} 2 \\phantom{10} corregido\\\\"
        "fade \\phantom{0} desde \\phantom{0} abajo")   # Phanthom{a} crea un espacio de tamaño "a"
        p3 = TextMobject("Texto tres")
        VGroup(title, p1, p2, p3).arrange_submobjects(DOWN) # Orden del texto
        self.play(                      # Animación de escritura
            Write(title),
            Write(p3),
            run_time=2
        )
        self.play(                      # Una vez aplicado FadeInFrom, cambia todos los 
            FadeInFrom(p1, UP),         # textos a tipo fórmula
            FadeInFrom(p2, DOWN),        
            run_time=3
        )
        self.wait()