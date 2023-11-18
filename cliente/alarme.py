import controlador01.controlador
import controlador02.controlador


def aciona_alarme():
    controlador01.controlador.acionar_alarme()
    controlador02.controlador.acionar_alarme()


def desativa_alarme():
    controlador01.controlador.desativar_alarme()
    controlador02.controlador.desativar_alarme()


def aproxima():
    controlador01.controlador.aproximacao()
    controlador02.controlador.aproximacao()


while True:

    entrada = input("Digite 1 para acionar o alarme, 2 para desativar o alarme ou 3 para detectar aproximação: ")

    if entrada == "1":
        aciona_alarme()
    elif entrada == "2":
        desativa_alarme()
    elif entrada == "3":
        aproxima()
    else:
        print("Entrada inválida.")
        break
