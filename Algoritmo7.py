procesos = []
n = int(input("Ingrese el número de procesos: "))

def inProcesos():
    for i in range(n):
        print("-------------------------------------------------------------")
        pName = input (f"Ingrese el nombre del proceso {i + 1}: ")
        llegada = int (input ("Ingrese la hora de llegada: "))
        ejecucion = int (input ("Ingrese el tiempo de ejecucion: "))

        # Nombre del proceso, hora de llegada, tiempo de ejecucion, inicio, finalización, tiempo de servicio, indice de servicio, tiempo de espera
        procesos.append([pName, llegada, ejecucion, 0, 0, 0, 0, 0])

def mostrarResultado(resultado):
    # Calcular el tiempo de servicio, el indice de servicio y tiempo de espera
    for i in range(n):
        resultado[i][5] = resultado[i][4] - resultado[i][1]
        resultado[i][6] = round((resultado[i][2] / resultado[i][5]),2)
        resultado[i][7] = resultado[i][5] - resultado[i][2]

    # Calcular el tiempo de servicio, el indice de servicio y el tiempo de espera promedio
    tiempoServicioProm = 0
    tiempoIservicioProm = 0
    tiempoEsperaProm = 0

    for i in range(n):
        tiempoServicioProm = (tiempoServicioProm + resultado[i][5])
        tiempoIservicioProm = (tiempoIservicioProm + resultado[i][6])
        tiempoEsperaProm = (tiempoEsperaProm + resultado[i][7])

    tiempoServicioProm = round((tiempoServicioProm/n),2)
    tiempoIservicioProm = round((tiempoIservicioProm/n),2)
    tiempoEsperaProm = round((tiempoEsperaProm/n),2)

    # Resultados de salida, ordenados según la hora de inicio
    resultado.sort(key = lambda x:x[3], reverse = False)
    print ("Resultado de la ejecución:")

    print("Proceso | Llegada | Ejecucion | Salida | Servicio | Indice Servicio | Espera |")
    for i in range(n):
        print("   ",resultado[i][0],"   |   ",resultado[i][1]," |    ",resultado[i][2]," |    ",resultado[i][4],"  |    ",resultado[i][5],"  |   ",resultado[i][6],"   |   ",resultado[i][7]," |")
    print(f"Tiempo de Servicio promedio: {tiempoServicioProm}")
    print(f"Indice Servicio promedio: {tiempoIservicioProm}" )
    print(f"Tiempo de Espera promedio: {tiempoEsperaProm}")
def FMQ():
    temp_procesos = copy.deepcopy(procesos)
    queue_rr8 = []
    queue_rr16 = []
    queue_fcfs = []
    fmq_procesos = []
    quantum8 = 8
    quantum16 = 16
    time = 0

    # Ordenar la lista en orden ascendente por hora de llegada x: x [1] se ordena por hora de llegada
    temp_procesos.sort(key = lambda x: x[1], reverse = False)

    while(len(fmq_procesos) < len(procesos)):

        if(len(queue_rr8) == 0):
            queue_rr8.append([temp_procesos.pop(0),0])
            time = queue_rr8[0][0][1]
        
        for p in temp_procesos[::-1]:
            if (p[1] <= time):
                queue_rr8.append([temp_procesos.pop(temp_procesos.index(p))], 0)

        # Ordenar la lista en orden ascendente por hora de llegada x: x [1] se ordena por hora de llegada
        queue_rr8.sort(key = lambda x: x[0][1], reverse = True)

        for p in queue_rr8[::-1]:
            if(p[0][3] == 0):
                p[0][3] = time
            if(p[0][2] <= quantum8):
                time += p[0][2]
                p[0][2] -= p[0][2]
                p[0][4] = time
                fmq_procesos.append(queue_rr8.pop(queue_rr8.index(p)).pop(0))
            elif(p[0][2] > quantum8):
                p[0][2] -= quantum8
                time += quantum8
                p[1] += 1

            if(p[1] >= 8):
                queue_rr16.append([queue_rr8.pop(queue_rr8.index(p)).pop(0),0])

        if(len(queue_rr8) == 0):
            for p in queue_rr16[::-1]:
                if(p[0][2] <= quantum16):
                    time += p[0][2]
                    p[0][2] -= p[0][2]
                    p[0][4] = time
                    fmq_procesos.append(queue_rr16.pop(queue_rr16.index(p)).pop(0))
                elif(p[0][2] > quantum16):
                    p[0][2] -= quantum16
                    time += quantum16
                    p[1] += 1

                if(p[1] >= 8):
                    queue_fcfs.append(queue_rr16.pop(queue_rr16.index(p)).pop(0))

        if(len(queue_rr16) == 0):
            queue_fcfs.sort(key = lambda x: x[1], reverse = True)
            for p in queue_fcfs[::-1]:
                time += p[2]
                p[4] = time
                fmq_procesos.append(queue_fcfs.pop(queue_fcfs.index(p)))

    for proceso in fmq_procesos:
        for p in procesos:
            if(proceso[0] == p[0]):
                proceso[2] = p[2]

def lanzar():
    inProcesos()
    FMQ()

lanzar()