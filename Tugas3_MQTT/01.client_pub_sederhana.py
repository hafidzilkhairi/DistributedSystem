# import paho mqtt
import paho.mqtt.client as paho

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

def on_publish(client, userdata, message):
    # print pesan
    print("terpublish")

# definisikan nama broker yang akan digunakan
broker="localhost"

# buat client baru bernama P2
print("creating new instance")
client=paho.Client("P2")
client.on_publish=on_publish

# koneksi ke broker
print("connecting to broker")
client.connect(broker)

# mulai loop client
client.loop_start()

# lakukan 20x publish waktu dengan topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time .sleep(1)
    # publish waktu sekarang
    client.publish("waktu",datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))

#stop loop
client.loop_stop()