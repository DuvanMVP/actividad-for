total_distancia = 0 
numero_escalas = int(input("Ingrese el numero de escalas: "))

for escala in range(numero_escalas):
    distance = float(input("Ingreese la distancia de las escalas (escala + 1): "))
    total_distancia += distance
    
print("la distancia total es ", total_distancia ," y el numero de escalas es",numero_escalas)
