#import Algoritmo1 as a1

def mensajeBienvenida():
    print("                                             ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───")
    print("                                             ───█▒▒░░░░░░░░░▒▒█───")
    print("                                             ────█░░█░░░░░█░░█────")
    print("                                             ─▄▄──█░░░▀█▀░░░█──▄▄─")
    print("                                             █░░█─▀░░░░░░░░░▀─█░░█")
    print("                                             █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("                                             █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
    print("                                             █░░║║║╠─║─║─║║║║║╠─░░█")
    print("                                             █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
    print("                                             █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("\n")
    print("▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █▀▄▀█ █▀█ █▀   █▀▄ █▀▀   █▀█ █░░ ▄▀█ █▄░█ █ █▀▀ █ █▀▀ ▄▀█ █▀▀ █ █▀█ █▄░█")
    print("█▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █░▀░█ █▄█ ▄█   █▄▀ ██▄   █▀▀ █▄▄ █▀█ █░▀█ █ █▀░ █ █▄▄ █▀█ █▄▄ █ █▄█ █░▀█")
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print("Integrantes: Juan Esteban Quintero Rodriguez - David Santiago Martinez Lopez - Ismenia Marcela Guevara Ortiz")
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
def mensajeDespedida():
    print("     ──────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("     ─██████████████─████████████████───██████████████─██████████████─██████████─██████████████─██████████████─")
    print("     ─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("     ─██░░██████████─██░░████████░░██───██░░██████░░██─██░░██████████─████░░████─██░░██████░░██─██░░██████████─")
    print("     ─██░░██─────────██░░██────██░░██───██░░██──██░░██─██░░██───────────██░░██───██░░██──██░░██─██░░██─────────")
    print("     ─██░░██─────────██░░████████░░██───██░░██████░░██─██░░██───────────██░░██───██░░██████░░██─██░░██████████─")
    print("     ─██░░██──██████─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██───────────██░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("     ─██░░██──██░░██─██░░██████░░████───██░░██████░░██─██░░██───────────██░░██───██░░██████░░██─██████████░░██─")
    print("     ─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██───────────██░░██───██░░██──██░░██─────────██░░██─")
    print("     ─██░░██████░░██─██░░██──██░░██████─██░░██──██░░██─██░░██████████─████░░████─██░░██──██░░██─██████████░░██─")
    print("     ─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─")
    print("     ─██████████████─██████──██████████─██████──██████─██████████████─██████████─██████──██████─██████████████─")
    print("     ──────────────────────────────────────────────────────────────────────────────────────────────────────────")


def preguntar():
    print("Desea probar otro algoritmo?")
    print("1. si")
    print("2. no")
    respuesta = int(input())
    if respuesta == 1:
        return True
    elif respuesta == 2:
        return False


def funcion1():
    import Algoritmo1
    print("\n \n")


def funcion2():
    import Algoritmo2
    print("\n \n")


def funcion3():
    import Algoritmo3
    print("\n \n")


def funcion4():
    import Algoritmo4
    print("\n \n")


def funcion5():
    import Algoritmo5
    print("\n \n")


def funcion6():
    import Algoritmo6
    print("\n \n")


def funcion7():
    import Algoritmo7
    print("\n \n")


def lanzar_aplicacion():
    while True:
        print("Escriba la opcion del algoritmo que desea probar"+"\n")
        print("1. FCFS- (primero en llegar, primero en ser atendido)")
        print("2. SJF- (Trabajo más corto primero)")
        print("3. SRTF- (Tiempo restante más corto primero)")
        print("4. PRIORIDAD")
        print("5. HRN- (Respuesta Alta Siguiente)")
        print("6. RR- (Round Robin)")
        print("7. FMQ- (Colas múltiples de retroalimentación)")
        print("0. Salir"+"\n")
        opcion = input()
        if opcion == "0":
            mensajeDespedida()
            break
        elif opcion == "1":
            funcion1()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        elif opcion == "2":
            funcion2()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        elif opcion == "3":
            funcion3()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        elif opcion == "4":
            funcion4()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        elif opcion == "5":
            funcion5()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        elif opcion == "6":
            funcion6()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        elif opcion == "7":
            funcion7()
            if not preguntar():
                mensajeDespedida()
                break
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        else:
            print("Elija una opcion disponible"+"\n \n")
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

mensajeBienvenida()
lanzar_aplicacion()
