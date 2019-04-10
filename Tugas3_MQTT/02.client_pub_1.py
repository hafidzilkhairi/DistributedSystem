# import paho mqtt
import paho.mqtt.client as paho

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

# definisikan nama broker yang akan digunakan
broker = "localhost"
def published(c, u, m):
    print("Published")
# buat client baru bernama P2
print("creating new instance")
client = paho.Client('p2')
client.on_publish = published

# koneksi ke broker
print("connecting to broker")
client.connect(broker, 1234)

# mulai loop client
client.loop_start()

# lakukan 20x publish topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(0.1)
    # publish waktu sekarang topik 1
    client.publish('topik_1', "AAA: "+datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))

#stop loop
client.loop_stop()
