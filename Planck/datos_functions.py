from ROOT import TProfile
from ROOT import *
import pandas as pd

def data(Doc, nombre, caso):				# Crea los data frame y hace la correción de datos necesaria
	escale_toma = []
	escale_offs = []

	col_n = ["Tiempo", "Voltaje", "Corriente"]
	Doc.pop(0)
	Doc = pd.DataFrame(Doc)
	Doc.columns = col_n
	Doc = Doc.astype("float")
	# Correción de tiempo en ms a segundos (el valor minimo en mili segundos es 4.883)
	Doc["Tiempo"][abs(Doc["Tiempo"])>2.5] = round(Doc["Tiempo"]/1000,3)
	if nombre == "rojo":
		escale_toma = [500, 100]			# Escala de voltaje IN1, IN2
		escale_offs = [500, 100]			# Escala de voltaje IN1, IN2
	elif nombre == "azul":
		escale_toma = [500, 500]
		escale_offs = [500, 100]
	elif nombre == "acqua":
		escale_toma = [500, 100]
		escale_offs = [500, 100]	
	elif nombre == "uv":
		escale_toma = [500, 200]
		escale_offs = [500, 100]	
	elif nombre == "naranja":
		escale_toma = [500, 200]
		escale_offs = [500, 100]	
	elif nombre == "verde":
		escale_toma = [500, 200]
		escale_offs = [500, 100]
	if caso == 2:
		print(escale_toma[1]/escale_offs[1])
		Doc["Corriente"] = Doc["Corriente"]/(escale_toma[1]/escale_offs[1])	
	return Doc

def style(Profile, Doc, texto1, texto2, color):			# Variables de estilo de Root
	for i in range(0, len(Doc[texto1]) ):
		Profile.Fill(Doc[texto1][i], Doc[texto2][i])	# Ingresa los puntos
	Profile.SetMarkerSize(0.75)							# Tamaño y forma de los puntos
	Profile.SetMarkerStyle(kFullCircle)		
	Profile.SetMarkerColorAlpha(color,0.25)				# Color alpha bajo para observar mejor el fit
	Profile.GetXaxis().SetTitle(texto1)					# Nombre eje X
	Profile.GetYaxis().SetTitle(texto2)					# Nombre eje Y

def grafs(Doc, color, r_min, r_max, bin):
	bin2 = 100
	Time_Volt = TProfile("T vs  V","Tiempo vs Voltaje", bin2, -2.5, 2.5)			# Gráfica 1
	style(Time_Volt, Doc, "Tiempo", "Voltaje", color)

	Time_Curr = TProfile("T vs C", "Tiempo vs Corriente", bin2, -2.5, 2.5)			# Gráfica 2
	style(Time_Curr, Doc, "Tiempo", "Corriente", color)

	Volt_Curr = TProfile("V vs C", "Voltaje vs Corriente", bin2, -3.1, 2.0)			# Gráfica 3
	style(Volt_Curr, Doc, "Voltaje", "Corriente", color)

	rango = [0.65, 0.94]
	Volt_Curr_fit = TProfile("V vs C", "Voltaje vs Corriente"+"  bines: "+str(bin)+" rmin: "+str(r_min)+" rmax: "+str(r_max), bin, -3.1, 1.5)	# Gráfica fit
	style(Volt_Curr_fit, Doc, "Voltaje", "Corriente", color)

	line = TF1("line", "[0]+[1]*x", r_min, r_max )					# Ecuación a ajustar con rango solicitado
	line.SetParNames("b","m")
	line.SetLineColor(kAzure-3)

	line2 = TF1("line2", "[0]+[1]*x", -3, -1.3 )					# Ecuación a ajustar con rango fijo para el color rojo
	line2.SetParNames("b1","m1")
	line2.SetLineColor(kAzure-3) 

	return Time_Volt, Time_Curr, Volt_Curr, Volt_Curr_fit, line, line2
	
def color_s(nombre):			# Selecciona el color de los puntos dependiendo el archivo leido
	if nombre == "rojo":
		color = kRed
	elif nombre == "azul":
		color = kBlue -3
	elif nombre == "acqua":
		color = kCyan +1
	elif nombre == "uv":
		color = kMagenta
	elif nombre == "naranja":
		color = kOrange +7
	elif nombre == "verde":
		color = kGreen +1
	else:
		color = kPink +9
		
	return color

#####################################################################################################