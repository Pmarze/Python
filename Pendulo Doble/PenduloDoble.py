# Programa para el pendulo doble

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import time
inicio= time.time()

archivo=pd.ExcelFile("datos.xlsx")
Prec_Simple=archivo.parse("Normalizado_S")
Prec_Total=archivo.parse("Normalizado_T")
Radio_S=archivo.parse("radio_S")
Radio_T=archivo.parse("radio_T")

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

def comparar(archivo1,archivo2,archivo3,a,delta,porcentaje,caso):      # Archivo1=Simple, Archivo2=Total, Archivo3=Runge-Kutta
    total=1
    acierto=1
    for i in np.arange(0,a,5):
        total+=1
        if (xaz(i,caso,archivo1,archivo2)-xaz(i,caso,archivo3,archivo3))<delta:
            acierto+=1
    return (100*acierto)/total

def relativo(caso,archi1,archi2):
    return yro(0,caso,archi1,archi2)/xro(0,caso,archi1,archi2)
###############################################################################
# Encontrar theta1 y theta2 iniciales

theta_0=[]
theta1_0=[]
theta2_0=[]
for theta1 in np.arange(180,270.5,0.1):
    x1=54*np.sin(np.radians(theta1))
    xvaluar=xro(0,1,Prec_Simple,Prec_Total)*100
    porcent=xvaluar*0.01
    if  x1>xvaluar+porcent and x1<xvaluar-porcent:
        theta_0.append(theta1)
for theta11 in(theta_0):
    for theta2 in np.arange(0,90,0.1):
        x2=54*np.sin(np.radians(theta11))+45*np.sin(np.radians(theta2))
        x2valuar=xaz(0,1,Prec_Simple,Prec_Total)*100
        porcent2=xvaluar*0.01
        if  x2>x2valuar+porcent2 and x2<x2valuar-porcent2:
            theta2_0.append(theta2)
            theta1_0.append(theta11)
            
###############################################################################
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



c=0
ite=0

theta1_salida=[]
theta2_salida=[]
m1_salida=[]
r1_salida=[]
porcentaje_salida=[]


cant_p = 900                              # Cantidad de pasos
g = 9.81                                # gravedad
h = 0.008333333333                      # Tamaño de la iteración para el método RK4
relacion=relativo(1,Radio_S,Radio_T)    # Constante de proporcinalidad

for aa in range(0,len(theta1_0)):       # Variar para cada caso de ángulos iniciales
    for a in np.arange(0.3,2,0.3):      # Se varía el valor de ambas barillas
        for b in np.arange(0.3,5,0.1):    # y también la longitud de las masas
            
            # Condiciones iniciales
            m1 = b      # masa del péndulo rojo
            m2 = m1     # asumimos que es la misma masa
            r1 = a      # longitud pendulo rojo
            r2 = r1*relacion     # asumimos misma longitud
            runit = np.sqrt(r1**2+r2**2)        # Se normaliza para poder trabajar independiente de la distancia
            x = y = []
          
            # Condiciones iniciales de los ángulos [ángulo, velocidad angular]
            a1_arr = np.array([np.radians(theta1_0[aa]),0])
            a2_arr = np.array([np.radians(theta2_0[aa]),0])
            t = 0                           # Tiempo inicial
            
            steps_no = cant_p               # number of steps of the RK4 method
            time_arr = np.array([t])
            func_array1 = np.array([a1_arr])
            func_array2 = np.array([a2_arr])
            
            tiempo=[]
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
                ite+=1
            
            # You can plot the pendulum's position or angular speed/acceleration as a function of time
            [pendulum1_theta, pendulum1_angular_speed] = func_array1.transpose()
            [pendulum2_theta, pendulum2_angular_speed] = func_array2.transpose()
            
            pendulum1_x = np.divide(r1*np.sin(pendulum1_theta),runit)
            pendulum1_y = np.divide(- r1*np.cos(pendulum1_theta),runit)
            
            pendulum2_x = np.divide(r2*np.sin(pendulum2_theta),runit) + pendulum1_x
            pendulum2_y = pendulum1_y - np.divide(r2*np.cos(pendulum2_theta),runit)
            
            np.true_divide(pendulum1_x,runit)
            
            dataf = pd.DataFrame({"t":tiempo,
                                  "xr":pendulum1_x,
                                  "yr":pendulum1_y,
                                  "xa":pendulum2_x,
                                  "ya":pendulum2_y,})
    
            c+=1                        # Se aumenta en uno con cada éxito y se crea un archivo distinto
            
            
            porcentaje = comparar(Prec_Simple,Prec_Total,dataf,cant_p,0.01,10,1)
            if porcentaje > 50:
                #print("aciertos:",porcentaje,"caso",c)
                #print("theta1=",theta1_0[aa],"theta2=",theta2_0[aa],"m1=",m1,"r1=",r1)
                theta1_salida.append(theta1_0[aa])
                theta2_salida.append(theta2_0[aa])
                m1_salida.append(m1)
                r1_salida.append(r1)
                porcentaje_salida.append(porcentaje)
                
                
            '''
            # Graficar el cada frame del movimiento
            scatter_x = []
            scatter_y = []
            counter = 0
            save_every_n_frames = 5
            for j in range(int(len(pendulum1_y)/save_every_n_frames)):
                i = j*save_every_n_frames
                fig = plt.figure()
                ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2,2), ylim=(-2.1, 1.5))
                x = [0, pendulum1_x[i]]
                y = [0, pendulum1_y[i]]
                ax.plot(x,y,lw=3,color='red')
                x1 = [pendulum1_x[i], pendulum2_x[i]]
                y1 = [pendulum1_y[i], pendulum2_y[i]]
                scatter_x.append(pendulum2_x[i])
                scatter_y.append(pendulum2_y[i])
                ax.plot(x1,y1,'o-',lw=3,color='blue',markersize=5)
                ax.scatter(scatter_x,scatter_y,lw=0.0005,color='black')
                ax.set_xlabel('$x-Axis$',fontsize=12)
                ax.set_ylabel('$y-Axis$',fontsize=12)
                ax.set_title('Péndulo Doble Runge-Kutta ',fontsize=14)
                ax.grid()
                fig.savefig(str(j)+'.png',dpi=300)
                plt.show()
            '''
            ############################################################################################        
            # Guardar datos en excel
            '''
            k="salida"+str(c)+".xlsx"
            writer=pd.ExcelWriter(k)
            dataf.to_excel(writer,index=False)
            #dataf.to_excel(writer)
            writer.save()
            '''
cond_inic_salida=pd.DataFrame({"porcentaje":porcentaje_salida,
                               "theta1": theta1_salida,
                               "theta2": theta2_salida,
                               "m1": m1_salida,
                               "r1": r1_salida})            

cond_inic_salida=cond_inic_salida.sort_values(by=['porcentaje'])
cond_inic_salida=cond_inic_salida[::-1]
k2="condiciones.xlsx"
writer2=pd.ExcelWriter(k2)
cond_inic_salida.to_excel(writer2,index=False)
writer2.save()            
############################################################################################
'''
# Eliminar los archivos de excel
for i in range(1,c+1):
    k2="salida"+str(i)+".xlsx"
    os.remove(k2)
'''    
print("iteraciones=",ite)
fin = time.time()
print("tiempo=",fin-inicio,"s")
print("tiempo=",(fin-inicio)/60,"m")