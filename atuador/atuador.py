import paho.mqtt.client as mqtt

mqtt_broker = "localhost"  
mqtt_topic = "atuador"  


mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "Ligar":
        print("Ligado")
    elif msg.payload.decode() == "Desligar":
        print("Desligado")
    
mqtt_client.subscribe(mqtt_topic)
mqtt_client.on_message = on_message
mqtt_client.loop_forever()