# Ahmet Ramekaj Grafik diskret, me pika (scatter plot)
import matplotlib.pyplot as plt
import json

f = open("koha.json")# hapim filen qe ka te dhenat e kohe
# inicializojme variblin koha me te dhenat e files koha.json
koha = json.load(f)
f.close()# mbyllim filen

lista_mot =  []# liste boshe qe do mbaje motin qe kemi ne json
for items in koha :# cikel for qe te mbushim listen me te dhenat e motit
     # te dhenat e motit nga file i json i kalojme te var.moti 1 nga 1
    moti = items["Moti"]
    lista_mot.append(moti)

lista_dita = []
for items in koha:
    ditet = items["Dita"]
    lista_dita.append(ditet)
    

plt.title("Moti gjate gjithe javes", fontsize = 14)# Percaktojme titullin
plt.xlabel("Ditet e javes", fontsize = 14)# Percaktojme x label
plt.ylabel("Gjendja motit", fontsize = 14)# Percaktojme y label

# afishojme motin dhe ditet
plt.scatter(
    lista_dita,
    lista_mot,
    linewidth = 5
)
plt.show()# shfaqim grafikun