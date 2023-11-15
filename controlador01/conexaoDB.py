import redis

cliente_redis = redis.StrictRedis(host='localhost', port=6379, db=0)
cliente_redis.slaveof('no', 'one')

def salvar_dados(mensagem):
    
    cliente_redis.set('mensagem', mensagem)
    print("Dados salvos com sucesso.")
