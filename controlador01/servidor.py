import rpyc

class Controlador1Service(rpyc.Service):
    
    def on_connect(self, conn):
        print("Conexão estabelecida com Controlador 1.")

    def on_disconnect(self, conn):
        print("Conexão perdida com Controlador 1.")

    def exposed_comunicacao(self):
        return True

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(Controlador1Service, port=18862)
    t.start()
    
    