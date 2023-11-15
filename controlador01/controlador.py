import paho.mqtt.client as mqtt
from .cliente import Controlador2Client

mqtt_broker = "localhost"
mqtt_topic_sub = "sensor"
mqtt_topic_pub = "atuador"

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)
x = Controlador2Client()


def acionar_alarme():
    acionar = "Ligar"

    pergunta = x.realizar_comunicacao()

    if pergunta == False:
        print("Alarme acionado.")
        resultado = mqtt_client.publish(mqtt_topic_pub, acionar)
    
def desativar_alarme():
    acionar = "Desligar"
    from controlador01 import cliente
    pergunta = cliente.realizar_comunicacao()
    
    if pergunta == False:
        print("Alarme desliga.")
        resultado = mqtt_client.publish(mqtt_topic_pub, acionar)
    
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
    
def executar():    
    mqtt_client.subscribe(mqtt_topic_sub)
    mqtt_client.on_message = on_message
    mqtt_client.loop_forever()
    