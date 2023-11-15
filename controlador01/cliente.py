import rpyc

from controlador01 import controlador

class Controlador2Client:

    def realizar_comunicacao(self):
        try:
            conn = rpyc.connect("localhost", 18862)
            result = conn.root.exposed_comunicacao()
            return result
        except EOFError or ConnectionRefusedError:
            return False
        

if __name__ == "__main__":
    controlador2 = Controlador2Client()
    controlador2.realizar_comunicacao()
