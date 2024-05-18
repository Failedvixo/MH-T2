from collections import deque
from collections import defaultdict
import random

with open('C1.txt', 'r') as file:
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



def hillClimb():
    solucion = [0]*n_lugares
   # print(solucion)

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
                    solucion[lugar]=1
    
    #print(solucion)
    print(matrix_demanda_por_sector)
    vecino = neighbor(solucion, total_cost)
    checkSolution(vecino)

def neighbor(solucion, total_cost):
    aux = solucion
    cambio_posicion= random.randint(0, n_lugares-1)
    if(solucion[cambio_posicion]==0):
        aux[cambio_posicion] = 1
    else:
        aux[cambio_posicion] = 0
    return aux


#def checkSolution(aux):


hillClimb()


