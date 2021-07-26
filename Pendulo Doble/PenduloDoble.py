'''
2021-07-26
PenduloDoble.py
Pablo Martínez (pabloversion1.0@gmail.com)

Programa que calcula candidatos a condiciones iniciales que provean una trayectoria
cercana a la observada en un video del péndulo doble.

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
<http://www.gnu.org/licenses/>.
'''
##############################################################################################
import pandas as pd
import numpy as np
import time
inicio= time.time()

archivo=pd.ExcelFile("datos.xlsx")          # Archivo donde se leen los datos obtenidos
Prec_Simple=archivo.parse("Normalizado_S")  # Debe existir una hoja con datos normalizados de 
Prec_Total=archivo.parse("Normalizado_T")   # precisión simple y otra con precisión total
Radio_S=archivo.parse("radio_S")            # Relaciones de proporcionalidad de la longitud relativa
Radio_T=archivo.parse("radio_T")            # entre ambas varillas, con precisión simple y total

##############################################################################################
# Funciones para poder comparar las filas de los datos del video vs los datos de la simulación

def xro(fila,caso,archi1,archi2):     # Caso 1 precisión simple, Caso 2 precisión total
        if caso==1:
            return archi1.loc[fila][1]
        elif caso==2:
            return archi2.loc[fila][1]

def yro(fila,caso,archi1,archi2):
        if caso==1:
            return archi1.loc[fila][2]
        elif caso==2:
            return archi2.loc[fila][2]
            
def xaz(fila,caso,archi1,archi2):
        if caso==1:
            return archi1.loc[fila][3]
        elif caso==2:
            return archi2.loc[fila][3]

def yaz(fila,caso,archi1,archi2):
        if caso==1:
            return archi1.loc[fila][4]
        elif caso==2:
            return archi2.loc[fila][4]

# Función para comparar arreglos de datos
# Archivo1=Simple, Archivo2=Total, Archivo3=Runge-Kutta
def comparar(archivo1,archivo2,archivo3,a,delta,porcentaje,caso):
    total=1
    acierto=1
    for i in np.arange(0,a,2):
        total+=1
        if abs((xaz(i,caso,archivo1,archivo2)-xaz(i,caso,archivo3,archivo3)))<delta:
            if abs((xro(i,caso,archivo1,archivo2)-xro(i,caso,archivo3,archivo3)))<delta:
                acierto+=1
    return (100*acierto)/total

# cálculo de la constante de proporcionalidad entre ambas varillas
def relativo(caso,archi1,archi2):
    return yro(0,caso,archi1,archi2)/xro(0,caso,archi1,archi2)

##############################################################################################
# Encontrar theta1 y theta2 iniciales en un rango determinado

theta_0=[]
theta1_0=[]
theta2_0=[]

for theta1 in np.arange(200,210,0.2):
    x1=54*np.sin(np.radians(theta1))
    xvaluar=xro(0,1,Prec_Simple,Prec_Total)*100
    porcent=xvaluar*0.01
    if  x1>xvaluar+porcent and x1<xvaluar-porcent:
        theta_0.append(theta1)
for theta11 in(theta_0):
    for theta2 in np.arange(15,25,0.2):
        x2=54*np.sin(np.radians(theta11))+45*np.sin(np.radians(theta2))
        x2valuar=xaz(0,1,Prec_Simple,Prec_Total)*100
        porcent2=xvaluar*0.01
        if  x2>x2valuar+porcent2 and x2<x2valuar-porcent2:
            theta2_0.append(theta2)
            theta1_0.append(theta11)
            
##############################################################################################
# Inicia código modificado de Ahmed Alkharusi, estas modificaciones fueron para
# adecuar el código según las necesidades del problema
"""
# =============================================================================
# Simulating the double pendulum using Runge–Kutta method (RK4)
# =============================================================================
Created on Fri Jul 17 2020
@author: Ahmed Alkharusi
"""
# =============================================================================
# Functions defn.
# =============================================================================
        
def angular_acc1(a1_arr,a2_arr):
    """Calculate the angular acceleration for the 1st pendulum
    Inputs-> a1_arr: np.array([Initial angle, Initial angular velocity]);
    a2_arr: np.array([Initial angle, Initial angular velocity]);"""
    num = -g *(2*m1+m2)*np.sin(a1_arr[0]) - m2*g*np.sin(a1_arr[0]-2*a2_arr[0])- 2* m2*np.sin(a1_arr[0]-a2_arr[0]) * (r2*pow(a2_arr[1],2)+r1*pow(a1_arr[1],2)*np.cos(a1_arr[0]-a2_arr[0]))
    den = r1*(2*m1+m2-m2 * np.cos(2*a1_arr[0]-2*a2_arr[0]))
    return num/den
        
def angular_acc2(a1_arr,a2_arr):
    """Calculate the angular acceleration for the 2nd pendulum
    Inputs-> a1_arr: np.array([Initial angle, Initial angular velocity]);
    a2_arr: np.array([Initial angle, Initial angular velocity]);"""
    temp = (2*np.sin(a1_arr[0]-a2_arr[0])) 
    num = temp * (r1*pow(a1_arr[1],2)*(m1+m2)+g*(m1+m2)*np.cos(a1_arr[0])+r2*pow(a2_arr[1],2)*m2*np.cos(a1_arr[0]-a2_arr[0]))
    den = r2*(2*m1+m2-m2 * np.cos(2*a1_arr[0]-2*a2_arr[0]))
    return num/den

def deriv_a1(a1_arr,a2_arr,t):
    """
    Returns an array np.array([first derivative, 2nd derivative])
    Inputs-> a1_arr: np.array([Initial angle, Initial angular velocity]);
    a2_arr: np.array([Initial angle, Initial angular velocity]);
    t: the dependent variable;
    """
    return np.array([a1_arr[1],angular_acc1(a1_arr,a2_arr)])

def deriv_a2(a2_arr,a1_arr,t):
    return np.array([a2_arr[1],angular_acc2(a1_arr,a2_arr)])

def rk4(deriv,func_i,func_i2, x_i,h):
    """
    Implements the RK4 method
    Inputs-> deriv: a function that takes two arguments;
    func_i: the function to be calculated;
    func_i2: this is just passed as an argument for func_i (see above deriv_a1 and deriv_a2);
    x_i: the dependent variable of func_i;
    h: the step size;
    
    """
    k1 = deriv(func_i,func_i2,x_i)
    k2 = deriv(func_i+h/2,func_i2,h*k1/2)
    k3 = deriv(func_i+h/2,func_i2,h*k2/2)
    k4 = deriv(func_i+h,func_i2,h*k3)
    func = func_i + (1/6) * h * (k1 +2*k2+2*k3+k4)
    x = x_i + h
    return (x,func)

##############################################################################################

ite=0                       # Variable de conteo sobre las iteraciones realizadas
theta1_salida=[]            # Arreglos para almacenar variables necesarias
theta2_salida=[]
m1_salida=[]
r1_salida=[]
porcentaje_salida=[]

cant_p = 300                            # Cantidad de pasos a realizar
g = 981                                 # cm/s^2 gravedad
h = 0.008333333333                      # Tamaño de la iteración para el método RK4
relacion=relativo(1,Radio_S,Radio_T)    # Constante de proporcinalidad
for aa in range(0,len(theta1_0)):       # Variar para cada pareja de candidatos de los de ángulos iniciales
    for a in np.arange(5,15,0.5):       # Se varía el valor de ambas barillas
        for b in np.arange(0.1,6,0.2):  # y también la longitud de las masas
            
            # Condiciones iniciales
            m1 = b                      # masa del péndulo rojo
            m2 = m1                     # asumimos que es la misma masa
            r1 = a                      # longitud péndulo rojo
            r2 = r1*relacion            # longitud péndulo azul
            runit = np.sqrt(r1**2+r2**2)  # Se normaliza para poder trabajar independiente de la distancia
            x = y = []
          
            # Condiciones iniciales de los ángulos [ángulo, velocidad angular]
            a1_arr = np.array([np.radians(theta1_0[aa]),0])
            a2_arr = np.array([np.radians(theta2_0[aa]),0])
            t = 0                           # Tiempo inicial
            steps_no = cant_p
            time_arr = np.array([t])
            func_array1 = np.array([a1_arr])
            func_array2 = np.array([a2_arr])
            
            tiempo=[]                   # Arreglo para añadir tiempo al data frame
            tiempo.clear()
            tiempo.append(0)
            for i in range(steps_no):
                temp =a1_arr
                (t,a1_arr) = rk4(deriv_a1,a1_arr,a2_arr,t,h)
                t -=h 
                (t,a2_arr) = rk4(deriv_a2,a2_arr,temp,t,h)
                time_arr2 = np.append(time_arr, t)
                func_array1 = np.vstack((func_array1,np.array([a1_arr])))
                func_array2 = np.vstack((func_array2,np.array([a2_arr])))
                tiempo.append(t)
                ite+=1                  # Aumenta la cantidad de iteraciones
            
            # You can plot the pendulum's position or angular speed/acceleration as a function of time
            [pendulum1_theta, pendulum1_angular_speed] = func_array1.transpose()
            [pendulum2_theta, pendulum2_angular_speed] = func_array2.transpose()
            
            pendulum1_x = np.divide(r1*np.sin(pendulum1_theta),runit)
            pendulum1_y = np.divide(- r1*np.cos(pendulum1_theta),runit)
            
            pendulum2_x = np.divide(r2*np.sin(pendulum2_theta),runit) + pendulum1_x
            pendulum2_y = pendulum1_y - np.divide(r2*np.cos(pendulum2_theta),runit)
            
            np.true_divide(pendulum1_x,runit)
            
            # Se crea un dataframe con los datos obtenidos en este caso
            dataf = pd.DataFrame({"t":tiempo,
                                  "xr":pendulum1_x,
                                  "yr":pendulum1_y,
                                  "xa":pendulum2_x,
                                  "ya":pendulum2_y,})
            
            # Se compara el resultado de la simulación contra los datos obtenidos            
            porcentaje = comparar(Prec_Simple,Prec_Total,dataf,cant_p,0.05,10,1)
            if porcentaje > 50:         # Si se desea solamente resultados sobre cierto porcentaje
                theta1_salida.append(theta1_0[aa])  # Se almacenan las cond. iniciales que cumplan
                theta2_salida.append(theta2_0[aa])
                m1_salida.append(m1)
                r1_salida.append(r1)
                porcentaje_salida.append(porcentaje)
        
##############################################################################################
# Se crea un dataframe con los casos que superaron el límite anterior
cond_inic_salida=pd.DataFrame({"porcentaje":porcentaje_salida,
                               "theta1": theta1_salida,
                               "theta2": theta2_salida,
                               "m1": m1_salida,
                               "r1": r1_salida})            

# Para evitar realizar operaciones en excel, se ordenan los resultados de mayor a menor
cond_inic_salida=cond_inic_salida.sort_values(by=['porcentaje'])
cond_inic_salida=cond_inic_salida[::-1]
k2="condiciones.xlsx"   # El archivo de excel con los resultados se llama "condiciones"
writer2=pd.ExcelWriter(k2)
cond_inic_salida.to_excel(writer2,index=False)
writer2.save()            
##############################################################################################
# Se muestran el tiempo de ejecución y la cantidad de iteraciones
print("iteraciones=",ite)
fin = time.time()
print("tiempo=",fin-inicio,"s")