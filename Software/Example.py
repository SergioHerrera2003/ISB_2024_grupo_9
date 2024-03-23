# Laboratorio N°2.2
# Ejercicio 1
# Elaborado por Sergio Jesús Miguel Herrera del Carpio

# Parte a
lista = [('1','2','3','4'),('2','3','4','5'),('3','4','5','6'),('4','5','6','7')]
listanew=[ ]
for i in range(len(lista)):
    listai = list(lista [i])
    agregar = ((int(listai[0])*(10**3) +int(listai[1])*(10**2)+int(listai[2])*10+int(listai[3])))
    
    listai.append(str(agregar))
    listanew.append(tuple(listai))
print("La nueva lista es:\nlista =", listanew,"\n")

# Parte b
print("En forma de matriz lo ordenamos de la siguiente manera: ")
for i in range(len(listanew)):
    filai = listanew[i]
    listamat = list(filai)
    print(listamat)
