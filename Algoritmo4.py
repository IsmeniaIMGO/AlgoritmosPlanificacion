class proceso(object):
    def __init__(self, id, prioridad):
        self.id = id
        self.prioridad = prioridad

print("Ingrese el numero de procesos")
nnumeros = int(input(">"))
if (nnumeros > 0):
    listadeprocesos = []
    for i in range(nnumeros):
        tmpllegada = -1
        print("-------------------- Proceso " + str(i + 1) + " ------------------------")

        prioridad = 0
        while (prioridad< 1):
            print("Ingrese la prioridad del proceso", i+1)
            prioridad = int(input(">"))
        # en el arreglo el primer item es el "id del proceso", prioridad
        listadeprocesos.append(proceso((i + 1), prioridad))
        print()
        print()

    print("Procesoss creados Con exito!!")
    print()

    listadeprocesos =  sorted(listadeprocesos, key=lambda proceso: proceso.prioridad, reverse=True)
    print("Orden de ejecucion de procesos: ")
    for proceso in listadeprocesos:

        print("Proceso " + str(proceso.id) + " Prioridad " +  str(proceso.prioridad))



