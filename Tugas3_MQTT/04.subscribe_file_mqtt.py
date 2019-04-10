# gunakan library paho


# gunakan library time


# buat callback pada saat ada pesan masuk
###########################################
def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
    
##########################################
        
# definisikan broker yang akan digunakan


# buat client P2 
print("creating new instance")


# koneksi P2 ke broker
print("connecting to broker")


# P2 subcribe ke topik "photo"
print("Subscribing to topic","photo")


# callback diaktifkan


#client.loop_forever()
while True:
    client.loop(15)
    time.sleep(2)