import rpyc

class Controlador2Client:

    def realizar_comunicacao(self):
    
            try:
                self.conn = rpyc.connect("localhost", 18862)
                result = self.conn.root.comunicacao()
                return result
            except EOFError or ConnectionRefusedError:
                return False
        

if __name__ == "__main__":
    controlador2 = Controlador2Client()
    controlador2.realizar_comunicacao()