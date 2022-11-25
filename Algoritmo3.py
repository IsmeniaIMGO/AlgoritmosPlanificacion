# Función para buscar el tiempo de espera
# para cada proceso
def buscarTiempoEspera(procesos, n, te):
	tr = [0] * n

	# Se copia el tiempo de ráfaga en tr[]
	for i in range(n):
		tr[i] = procesos[i][1]
	completados = 0
	t = 0
	min = 999999999
	corto = 0
	revisado = False

	# Procesar hasta que todos los procesos se completen
	while (completados != n):
		
		# Encuentrar el proceso con el tiempo restante 
        # mínimo entre los procesos que llegan hasta la 
        # hora actual
		for j in range(n):
			if ((procesos[j][2] <= t) and
				(tr[j] < min) and tr[j] > 0):
				min = tr[j]
				corto = j
				revisado = True
		if (revisado == False):
			t += 1
			continue
			
		# Reducir el tiempo restante en uno
		tr[corto] -= 1

		# Se actualiza el mínimo
		min = tr[corto]
		if (min == 0):
			min = 999999999

		# Si un proceso se ejecuta completamente
		if (tr[corto] == 0):

			# Incremento completo
			completados += 1
			revisado = False

			# Encuentra la hora de finalización 
            # del proceso actual
			tiempoTerminacion = t + 1

			# Calcular tiempo de espera
			te[corto] = (tiempoTerminacion - proc[corto][1] -	
								proc[corto][2])

			if (te[corto] < 0):
				te[corto] = 0
		
		# Incrementa el tiempo
		t += 1

# Función para calcular el tiempo de respuesta
def encontrarTiempoRespuesta(procesos, n, te, tdr):
	
	# Calcular tiempo de respuesta
	for i in range(n):
		tdr[i] = procesos[i][1] + te[i]

# Función para calcular tiempos medios de espera 
# y respuesta.
def encontrarTiempoPromedio(procesos, n):
	te = [0] * n
	tdr = [0] * n

	# Función para encontrar el tiempo de espera 
    # para todos los procesos
	buscarTiempoEspera(procesos, n, te)

	# Función para encontrar el tiempo de respuesta 
    # para todos los procesos
	encontrarTiempoRespuesta(procesos, n, te, tdr)

	# Mostrar procesos junto con todos los detalles
	print("Procesos 	Tiempo		 ráfaga		 en espera")
	total_te = 0
	total_tdr = 0
	for i in range(n):

		total_te = total_te + te[i]
		total_tdr = total_tdr + tdr[i]
		print(" ", procesos[i][0], "\t\t\t",
				procesos[i][1], "\t\t\t",
				te[i], "\t\t\t", tdr[i])

	print("\nTiempo medio de espera = %.5f "%(total_te /n) )
	print("Tiempo medio de respuesta = ", total_tdr / n)
	
# Controlador del coódigo

	# id's de procesos
proc = [[1, 5, 1], [2, 9, 2],
			[3, 7, 4], [4, 4, 3],
            [5, 8, 5]]
n = 5

def lanzar():
	encontrarTiempoPromedio(proc, n)

lanzar()
