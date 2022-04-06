# Ahmet Ramekaj Grafik ne forme disku (pie plot)
import matplotlib.pyplot as plt
import json

f = open("koha.json")# hapim filen qe ka te dhenat e kohe
# inicializojme variblin koha me te dhenat e files koha.json
koha = json.load(f)
f.close()# mbyllim filen

lista_shpejtesi =  []# liste boshe qe do mbaje shpejtesine e eres qe kemi ne json
for items in koha :# cikel for qe te mbushim listen me te dhenat e shpejtesise
     # te dhenat e shpejtesise nga file i json i kalojme te var.shpejtesia 1 nga 1
    shpejtesia = items["Shpejtesia e eres"]
    lista_shpejtesi.append(shpejtesia)
    
mylabels = ["E Hene", "E Marte", "E Merkure", "E Enjte","E Premte","E Shtune","E Diel"]# Percaktojme ditet
plt.title("Shpejtesia e eres gjate gjithe javes", fontsize = 14)# Percaktojme titullin

# afishojme shpejtesite e eres dhe ditet
plt.pie(
    lista_shpejtesi,
    labels = mylabels,
    autopct = "%1.1f%%"
)
plt.legend(lista_shpejtesi)# shfaqim legjenden ne grafik
plt.show()# shfaqim grafikun
