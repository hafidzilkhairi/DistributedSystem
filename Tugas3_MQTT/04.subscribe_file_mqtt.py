####yang dirunning harus file subscribe terlebih dahulu

# gunakan library paho
import paho.mqtt.client as paho

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################
def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
    print('berhasil diterima')
    with open('iris.jpg', 'wb') as fd:
        fd.write(message.payload)
        
def on_connect(client, userdata, flags, rc):
    print("OK Connected with result code "+str(rc))
    client.subscribe(SUBTOPIC, qos=0)
    print("Subscribe: " + SUBTOPIC)


def on_subscribe(client, userdata, mid, gqos):
    print("subscribed: " + gqos)
    pass
##########################################

# definisikan broker yang akan digunakan
broker="192.168.100.5"
SUBTOPIC="photo"
# buat client P2 
print("creating new instance")
client= paho.Client("P2")

# koneksi P2 ke broker
print("connecting to broker")
client.connect(broker,12345,60)

# P2 subcribe ke topik "photo"
print("Subscribing to topic","photo")
client.subscribe("photo", 0)

# callback diaktifkan
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe
#client.loop_forever()
while True:
    client.loop(15)
    time.sleep(2)