import paho.mqtt.client as mqtt
from cliente import Controlador2Client
from conexaoDB import salvar_dados

mqtt_broker = "localhost"
mqtt_topic_sub = "sensor"
mqtt_topic_sub_atuador = "atuadorPub"
mqtt_topic_pub = "atuador"

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)
x = Controlador2Client()

def acionar_alarme():
    acao = "Ligar"
    
    pergunta = x.realizar_comunicacao()
    
    if pergunta == False:
        
        resultado = mqtt_client.publish(mqtt_topic_pub, acao)
        confirmacao = mqtt_client.subscribe(mqtt_topic_sub_atuador)
        print("Alarme acionado.")
        mqtt_client.on_message = on_message_atuador
    
def desativar_alarme():
    acao = "Desligar"

    pergunta = x.realizar_comunicacao()
    
    if pergunta == False:
        
        resultado = mqtt_client.publish(mqtt_topic_pub, acao)
        confirmacao = mqtt_client.subscribe(mqtt_topic_sub_atuador)
        print("Alarme desliga.")
        mqtt_client.on_message = on_message_atuador
    
def aproximacao():
    mqtt_client.on_message = on_message
    print("Aproximação detectada.")

def on_publish(client, userdata, result):
    print("Dados Publicados02.")
    
def on_message(client, userdata, msg):
    
    intensidade = msg.payload.decode()
        
    if intensidade > "50":
        status = "Ligar"
        resultado = mqtt_client.publish(mqtt_topic_pub, status)
        mqtt_client.on_publish = on_publish
    
    elif intensidade <= "50":
        status = "Desligar"
        resultado = mqtt_client.publish(mqtt_topic_pub, status)
        mqtt_client.on_publish = on_publish

def on_message_atuador(client, userdata, msg):
    mensagem = msg.payload.decode()
    salvar_dados(mensagem)

def executar():    
    mqtt_client.subscribe(mqtt_topic_sub)
    mqtt_client.on_message = on_message
    mqtt_client.loop_forever()