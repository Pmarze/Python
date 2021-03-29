''' 2021-03-28
    SEMF.py
    Pablo Martínez (pabloversion1.0@gmail.com)

    Programa para calcular la masa atómica. Para utilizarlo se definen dos 
    vectores con las constantes a utilizar, 'ctej' es el vector con las constantes
    de la SEMF y 'masj' es el vector con las masas de los nucleones y el electrón,
    además de incluir el valor en eV del dalton.

    Codificación del texto: UTF8
    Compiladores probados: Python 3.8.5
    Instrucciones de compilación: python3 /SEMF.py

    Copyright (C) 2021
    P. D. Martínez Zeceña
    pabloversion1.0@gmail.com

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see
    <http://www.gnu.org/licenses/>
'''

#######################################################################################################

def f0(Z,A,MAS):                                    # Función para calcular f0
    return Z*(MAS[0]+MAS[2])+(A-Z)*MAS[1]           # resultado en MeV

def f1(Z,A,CTE):                                    # Función para calcular f1
    return -CTE[0]*A                                # resultado en MeV

def f2(Z,A,CTE):                                    # Función para calcular f2
    return CTE[1]*pow(A,2/3)                        # resultado en MeV

def f3(Z,A,CTE):                                    # Función para calcular f3
    return CTE[2]*(Z*(Z-1))/pow(A,1/3)              # resultado en MeV

def f4(Z,A,CTE):                                    # Función para calcular f4
    return CTE[3]*pow(Z-A/2,2)/A                    # resultado en MeV

def f5(Z,A,C,CTE):                                  # Función para calcular f5
    '''Función para calcular f5
    :param Z: Número atómico
    :param A: Número másico
    :param C: caso a analizar dado por δ (-1,0,1)
    -1 Si Z,N=par
     0 Si Z=par(impar), N=impar(par)
     1 Si Z,N=impar
    :param CTE: vector de constantes a_i
    '''
    if C==-1:   # Z,N par
        return -CTE[4]/pow(A,1/2)
    if C==0:    # Z=par(impar), N=impar(par)
        return 0
    if C==1:    # Z,N impar
        return CTE[4]/pow(A,1/2)                    # resultado en MeV

def M(Z,A,CTE,MAS,SEL):                                 # Función para calcular M(Z,A)
    '''Función para calcular masa atómica
    :param Z: Número atómico
    :param A: Número másico
    :param CTE: vector de constantes a_i
    :param MAS: vector de constantes de masa
    :param SEL: seleccionar resultados como 'TEX'=texto, 'TER'=terminal, 'VEC'=vector
    '''
    for i in range(-1,2):
        resultado=(f0(Z,A,MAS)+f1(Z,A,CTE)+f2(Z,A,CTE)+f3(Z,A,CTE)+f4(Z,A,CTE)+f5(Z,A,i,CTE))/MAS[3]
        if SEL=='TEX':
            print(resultado)                            # resultado en dalton
        elif SEL=='TER':  
            print('M(',Z,',',A,')=',resultado)    # resultado en dalton
        elif SEL=='VEC':
            DATOS.append(resultado)

#######################################################################################################

# Datos extraidos de Nuclear and Particle physics(2009), Brian Martin
cte1=(15.56,17.23,0.697,93.14,12.00) # MeV/c² (a1,a2,a3,a4,a5)=(av,as,ac,aa,ap) 
mas1=(0.9383*10**3,0.9396*10**3,0.511,931.494) # MeV/c² (Mp,Mn,Me,u)

# Datos extraidos de Wikipedia 28/03/21
cte2=(15.80,18.30,0.714,23.20,12.00) # MeV/c² (a1,a2,a3,a4,a5)=(av,as,ac,aa,ap)
mas2=(0.938282013*10**3,0.939565560*10**3,0.510998928,931.49410242) # Mev/c² (Mp,Mn,Me,u)

DATOS=[]

Z=int(input('Z='))
A=int(input('A='))

# Ejemplo de sintáxis
# TEXto
print('Modelo B.Martin')
M(Z,A,cte1,mas1,'TEX')
print()

# TERminal
print('Modelo Wikipedia')
M(Z,A,cte2,mas2,'TER')
print()

# VECtor
M(Z,A,cte1,mas1,'VEC')
M(Z,A,cte2,mas2,'VEC')
print('Modelo B.Martin y Wikipedia')
print(DATOS)

#######################################################################################################