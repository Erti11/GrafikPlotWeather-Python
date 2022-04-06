# Ahmet Ramekaj Grafik linear (line plot)
import matplotlib.pyplot as plt
import json

f = open("koha.json")# hapim filen qe ka te dhenat e kohe
# inicializojme variblin koha me te dhenat e files koha.json
koha = json.load(f)
f.close()# mbyllim filen
 
lista_temp = []# liste boshe qe do mbaje ditet qe kemi ne json
for items in koha:# cikel for qe te mbushim listen me te dhenat e temperaturave
     # te dhenat e temperaturave nga file i json i kalojme te var.temperatura 1 nga 1
    temperatura = items["Temperatura"]
    lista_temp.append(temperatura)

lista_dita = []
for items in koha:
    ditet =items ["Dita"]
    lista_dita.append(ditet)


plt.title("Temperaturat gjate gjithe javes", fontsize = 14)# Percaktojme titullin
plt.xlabel("Ditet e javes ",fontsize=14)# Percaktojme x label
plt.ylabel("Temperatura ne °C",fontsize=14)# Percaktojme y label

# afishojme temperaturat dhe ditet
plt.plot(
    lista_dita,
    lista_temp,
    linewidth = 3,
    color = "red"
)
plt.show()# shfaqim grafikun