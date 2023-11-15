from controlador01 import controlador as controlador1
from controlador02 import controlador as controlador2

def acionar_alarme():

    controlador1.acionar_alarme()
    controlador2.acionar_alarme()
    
def desativar_alarme():

    controlador1.desativar_alarme()
    controlador2.desativar_alarme()
    
def aproximacao():

    controlador1.aproximacao()
    controlador2.aproximacao()
    
while True:
    
    entrada = input("Digite 1 para acionar o alarme, 2 para desativar o alarme ou 3 para detectar aproximação: ")
    
    if entrada == "1":
        acionar_alarme()
    elif entrada == "2":
        desativar_alarme()
    elif entrada == "3":
        aproximacao()
    else:
        print("Entrada inválida.")
        break
    