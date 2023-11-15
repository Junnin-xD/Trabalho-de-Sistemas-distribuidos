import redis

cliente_redis = redis.StrictRedis(host='localhost', port=6380, db=0)
cliente_redis.slaveof('master', 6379)

def salvar_dados(mensagem):
    
    cliente_redis.set('mensagem', mensagem)
    print("Dados salvos com sucesso.")
