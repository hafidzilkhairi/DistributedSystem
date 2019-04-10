####yang dirunning harus file subscribe terlebih dahulu

# import paho
import paho.mqtt.client as paho

# definsi broker yang digunakan
broker="192.168.100.5"
filename="surf.jpg"

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

# buat client bernama P1
print("creating new instance")
P1= paho.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
P1.connect(broker, 12345,60)
P1.loop_start()
    
# print "baca file"
print ("read file")

# buka file surf.jpg
f = open(filename, "rb")

# baca semua isi file
imagestring = f.read()

# ubah file dalam bentuk byte gunakan fungsi byte()
byteArray = bytes(imagestring)

# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
P1.on_publish=on_publish
P1.publish("photo",byteArray,0)

# client loop mulai
P1.loop_forever()

# tutup file
f.close