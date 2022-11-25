
procesos = []
n = int (input ("Ingrese el número de procesos: "))

# Función de entrada
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

# Primer algoritmo de proceso más corto
def SJF():
    temp_procesos = procesos.copy()
    sjf_procesos = []
    queue_procesos = []

    # # Ordenar la lista en orden ascendente por hora de llegada x: x [1] se ordena por hora de llegada
    temp_procesos.sort(key = lambda x: x[1], reverse = False)


    while(len(sjf_procesos) < len(procesos)):

        for p in temp_procesos[::-1]:
            if(len(sjf_procesos) != 0):
                if (sjf_procesos[-1][1] < p[1] < sjf_procesos[-1][4]):
                    queue_procesos.append(temp_procesos.pop(temp_procesos.index(p)))

        queue_procesos.sort(key=lambda x: x[2], reverse = False)

        if(len(queue_procesos) == 0):
            queue_procesos.append(temp_procesos.pop(0))
            queue_procesos[0][3] = queue_procesos[0][1]
            queue_procesos[0][4] = queue_procesos[0][3] + queue_procesos[0][2]

        elif (queue_procesos[0][1] < sjf_procesos[-1][4]):
            queue_procesos[0][3] = sjf_procesos[-1][4]
            queue_procesos[0][4] = queue_procesos[0][3] + queue_procesos[0][2]
        
        sjf_procesos.append(queue_procesos.pop(0))

    mostrarResultado(sjf_procesos)

def lanzar():
    inProcesos()
    SJF()

lanzar()