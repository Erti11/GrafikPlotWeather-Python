# Ahmet Ramekaj Grafik me kolona (histogram)
import matplotlib.pyplot as plt
import json

f = open("koha.json")  # hapim filen me te dhenat e kohes
# inicializojme variablin koha me te dhenat e files koha.json
koha = json.load(f)
f.close()  # mbyllim filen

lista_mot = []  # liste boshe qe do mbaje motin qe kemi ne json
for items in koha:  # cikel for qe te mbushim listen me te dhenat e motit
    # te dhenat e motit nga file i json i kalojme te var.moti 1 nga 1
    moti = items["Moti"]
    lista_mot.append(moti)

plt.xlabel("moti", fontsize="15")  # Percaktojme x label
plt.ylabel("Numri i Ditve", fontsize="15")  # Percaktojme y label
plt.title("Sa dite ne jave kane te njejtin mot") # Percaktojme titullin

# afishojme motin dhe ditet
plt.hist(lista_mot, edgecolor="blue", color="red",bins=10,)
plt.show()  # shfaqim grafikun
