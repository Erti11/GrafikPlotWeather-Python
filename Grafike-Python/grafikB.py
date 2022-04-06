# Ahmet Ramekaj Grafik me flluska (bubble plot)
import matplotlib.pyplot as plt
import json

f = open("koha.json")# hapim filen qe ka te dhenat e kohes
# inicializojme variblin koha me te dhenat e files koha.json
koha = json.load(f)
f.close()# mbyllim filen

lista_lag = []# liste boshe qe do mbaje lageshtiren qe kemi ne json
for items in koha:# cikel for qe te mbushim listen me te dhenat e lageshtires
    # te dhenat e lageshtires nga file i json i kalojme te var.lage 1 nga 1
    lage = items["Lageshti"]
    lista_lag.append(lage)

lista_dit = []
for items in koha:
    ditet = items["Dita"]
    lista_dit.append(ditet)

lista_shpejt = []
for items in koha:
    sh = items["Shpejtesia e eres"]
    lista_shpejt.append(sh)

plt.xlabel("Ditet e javes",fontsize="15")# Percaktojme x label
plt.ylabel("Lageshtia dhe shpejtesia", fontsize="15")# Percaktojme y label
plt.title("Lageshtia (zi) dhe Shpejtesia e eres (kuq) gjate javes")# Percaktojme titullin

# afishojme shoejtesine e eres dhe ditet
plt.scatter(
    lista_dit, lista_shpejt, s=20,  c="red"
)
# afishojme lageshtine dhe ditet
plt.scatter(
    lista_dit, lista_lag, s=20, c="black"
)
plt.show()# shfaqim grafikun