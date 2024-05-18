#sectores -> cada una se compone de  lugares.
#Se instala en lugares
#Un sector cumple la demanda si alguno de sus lugares tiene una clínica.
#Se busca la minima cantidad de instalaciones tal que todos los sectores tengan cubierta su demanda


#guardar para cada lugar ( de los 1000 ), en un mapa con llave = id lugar.
# los sectores que satisface si se instala

#Luego el greedy es iterar por costos menores en este caso ya estan ordenados,
#y ver si satisface algun lugar si es asi


from collections import deque
from collections import defaultdict
import random

with open('/home/collapse/Escritorio/T2_meta/C2.txt', 'r') as file:
    content = file.read()
    numbers = deque(int(numero) for numero in content.split())
    #print(numbers)
    m_sectores = numbers.popleft() 
    n_lugares = numbers.popleft()
    #print(m_sectores)
    #costo instalacion por lugar
    n_lugares_costo = []
    for i in range(n_lugares):
        n_lugares_costo.append(numbers.popleft())
        
    matrix_demanda_por_sector = []
    sectores_satisfechos = defaultdict(list)


    for i in range(m_sectores):
        aux = []
        for j in range(numbers.popleft()):
            curr =numbers.popleft()
            aux.append(curr)

            if curr not in sectores_satisfechos:
                sectores_satisfechos[curr- 1] = [i]
            else:
                sectores_satisfechos[curr - 1].append(i)

        matrix_demanda_por_sector.append(aux)

    #print(matrix_demanda_por_sector[0])
    #print(sectores_satisfechos[0])
    #print(sectores_satisfechos[999])


def deterministic_greedy():
    visited_sector= [ -1 for _ in range(m_sectores)]
    left = m_sectores
    total_cost = 0

    #recorremos en orden el vector de lugares, dado que estan ordenados de costo menor a mayor
    for i in range(0, 1000):
        check = 0
        #caso ya visitamos todos los elementos
        if(left == 0):
            break
        #print(sectores_satisfechos)
        for sector in sectores_satisfechos[i]:    
            #si satisface alguno de los sectores aún no visitamos, lo consideramos para instalar
            if visited_sector[sector] == -1:
                check = 1
                left -=1 #queda 1 menos por visitar
                #print(f"not visited{sector}")
                #se elige de forma greedy los lugares con menos costo, añadimos el costo y actualizamos visited_sector
                visited_sector[sector] = 1

        if check == 1:
            total_cost += n_lugares_costo[i]
                    
    return total_cost


def stocastic_greedy():
    visited_sector= [ -1 for _ in range(m_sectores)]
    left = m_sectores
    total_cost = 0
    
    candidatos_por_costo = defaultdict(list) #1-index

    #obtener candidatos mismo costo
    for i in range(0, 1000):
        curr_cost = n_lugares_costo[i]

        if curr_cost not in candidatos_por_costo:
            candidatos_por_costo[n_lugares_costo[i]] = [i]
        else:
            candidatos_por_costo[n_lugares_costo[i]].append(i)

    #sorting para poder evaluar
    costos_ordenados = sorted(candidatos_por_costo.keys())    

    total_cost = 0
    for curr_costo in costos_ordenados:
            lugares = candidatos_por_costo[curr_costo]
            # Mezclar aleatoriamente los elementos asociados al costo
            random.shuffle(lugares)
            # Evaluamos siguiendo las mismas condiciones que el greedy determinista
            for lugar in lugares:
                check = 0
                for sector in sectores_satisfechos[lugar]:    

                    if visited_sector[sector] == -1:
                        check = 1
                        visited_sector[sector] = 1

                if check == 1:
                    total_cost += n_lugares_costo[lugar]

    return total_cost


print(f"Deterministic ans: {deterministic_greedy()}")

ans = 1000000

for i in range(1000):
    ans = min(stocastic_greedy(), ans)
    print(f" itt: {i} : {stocastic_greedy()}")

print(f"Best stochastic greedy: {ans}")
