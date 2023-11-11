import random
import time
import paho.mqtt.client as mqtt

mqtt_broker = "localhost"  
mqtt_topic = "sensor"  
#mqtt_topic2 = "sensor2"


mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883, 60)

#mqtt_client.subscribe(mqtt_topic2, acionaSensor)

#if acionaSensor == True:
        #print("Sensor Ligado")
def on_publish(client, userdata, result):
    print("Dados Publicados.")
   
while True:
    time.sleep(1)
    intensidade = random.randint(0, 100)
    print(intensidade)
    resultado = mqtt_client.publish(mqtt_topic, intensidade)
    mqtt_client.on_publish = on_publish
    
    #mqtt_client.subscribe(mqtt_topic2, acionaSensor)
    
    #if acionaSensor == False:
    #    print("Sensor Desligado")
    #    break
