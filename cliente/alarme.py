from ..controlador01 import controlador as controlador01
from ..controlador02 import controlador as controlador02

x = controlador01
y = controlador02

def acionar_alarme():

    x.acionar_alarme()
    y.acionar_alarme()
    
def desativar_alarme():

    x.desativar_alarme()
    y.desativar_alarme()
    
def aproximacao():

    x.aproximacao()
    y.aproximacao()
    
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
    