
# Función para ordenar el proceso por hora de llegada
def ordenarLlegada(time_llegada_proceso, numero_procesos):
    # Clasificación de selección aplicada
    for i in range(0, numero_procesos - 1):
        for j in range(i + 1, numero_procesos):

            # Consultar por menor tiempo de llegada
            if time_llegada_proceso[i] > time_llegada_proceso[j]:
                # Cambiar el proceso anterior al frente
                time_llegada_proceso[i], time_llegada_proceso[j] = time_llegada_proceso[j], time_llegada_proceso[i]

# código de conductor
def lanzar():

    suma_tiempo = 0
    tiempo_medio_espera = 0
    tiempo_prom_respuesta = 0
    numero_procesos = 5
    completado = [0] * numero_procesos
    tiempo_espera = [0] * numero_procesos
    tiempo_respuesta = [0] * numero_procesos
    normalizado_TT = [0] * numero_procesos

    # Horas de llegada predefinidas
    hora_llegada = [0, 2, 4, 6, 8]

    # Tiempos de ráfaga predefinidos
    tiempo_quemado = [3, 6, 4, 5, 2]
    proceso = []

    # Inicializar las variables de estructura
    for i in range(0, numero_procesos):
        proceso.append(chr(65 + i)) #Adjunta los valores
        suma_tiempo += tiempo_quemado[i]

    # Ordenar la estructura por horas de llegada
    ordenarLlegada(hora_llegada, numero_procesos)
    print("Nombre   " , "Hora de llegada",
          "Tiempo en ejecución", "Tiempo en espera",
          "Retorno", "Normalizado TT")
    tiempo = hora_llegada[0]

    while (tiempo < suma_tiempo):

        # Establecer el límite inferior para la relación de respuesta
        aux = -9999
        temp, local = 0, 0

        for i in range(0, numero_procesos):

            # Comprobar si el proceso ha llegado y esta completo
            if hora_llegada[i] <= tiempo and completado[i] != 1:

                # Cálculo de la relación de respuesta
                temp = ((tiempo_quemado[i] + (tiempo - hora_llegada[i])) / tiempo_quemado[i])

                # Comprobación de la tasa de respuesta más alta
                if aux < temp:
                    # Relación de respuesta de almacenamiento
                    aux = temp
                    # Ubicación de almacenamiento
                    local = i

        # Actualizando el valor del tiempo
        tiempo += tiempo_quemado[local]

        # Cálculo del tiempo de espera
        tiempo_espera[local] = (tiempo - hora_llegada[local] - tiempo_quemado[local])

        # Cálculo del tiempo de respuesta
        tiempo_respuesta[local] = tiempo - hora_llegada[local]

        # Suma del tiempo de respuesta para el promedio
        tiempo_prom_respuesta += tiempo_respuesta[local]

        # Cálculo del tiempo de respuesta normalizado
        normalizado_TT = float(tiempo_respuesta[local] / tiempo_quemado[local])

        # Actualización del estado de finalización
        completado[local] = 1

        # Tiempo de espera total para el promedio
        tiempo_medio_espera += tiempo_espera[local]

        print(proceso[local], "\t\t\t\t", hora_llegada[local],
              "\t\t\t\t", tiempo_quemado[local], "\t\t\t\t\t",
              tiempo_espera[local], "\t\t\t",
              tiempo_respuesta[local], "\t\t",
              "{0:.6f}".format(normalizado_TT))

    print("Tiempo medio de espera: {0:.6f}".format(tiempo_medio_espera / numero_procesos))
    print("Tiempo promedio de respuesta:  {0:.6f}".format(tiempo_prom_respuesta / numero_procesos))

lanzar()