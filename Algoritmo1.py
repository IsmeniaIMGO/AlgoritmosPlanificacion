
procesos = []
n = int(input("Ingrese el número de procesos: "))

# Función de entrada
def inProcesos():

    for i in range(n):
        print("-------------------------------------------------------------------")
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
        print("   ",resultado[i][0],"   |   ",resultado[i][1],"  |    ",resultado[i][2],   "   |    ",resultado[i][4],  "   |    ",resultado[i][5],  "  |     ",resultado[i][6],   "      |   ",resultado[i][7], " |")
    print(f"Tiempo de Servicio promedio: {tiempoServicioProm}")
    print(f"Indice Servicio promedio: {tiempoIservicioProm}" )
    print(f"Tiempo de Espera promedio: {tiempoEsperaProm}")


# Primero algoritmo de primer servicio
def FCFS():

    fcfs_procesos = procesos.copy()

    # Ordenar la lista en orden ascendente por hora de llegada x: x [1] se ordena por hora de llegada
    fcfs_procesos.sort(key = lambda x:x[1], reverse = False )

    # Calcular tiempo de inicio y finalización
    for i in range(n):
        if(i == 0):
            startTime = fcfs_procesos[i][1]
            fcfs_procesos[i][3] = startTime
            fcfs_procesos[i][4] = startTime + fcfs_procesos[i][2]

        elif(i > 0 and  fcfs_procesos[i - 1][4] < fcfs_procesos[i][1]):
            startTime = fcfs_procesos[i][1]
            fcfs_procesos[i][3] = startTime
            fcfs_procesos[i][4] = startTime + fcfs_procesos[i][2]

        else:
            startTime = procesos[i - 1][4]
            fcfs_procesos[i][3] = startTime
            fcfs_procesos[i][4] = startTime + fcfs_procesos[i][2]

    mostrarResultado(fcfs_procesos)

def lanzar():
    inProcesos()
    FCFS()

lanzar()