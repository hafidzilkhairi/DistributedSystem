# import paho mqtt


# import time for sleep()


# import re (regular expression) untuk filter


# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # filter pesan yang masuk 
    
    
    #jika ada pola AAA tulis ke result_a.txt
    if match:
    
    # lainnya tulis ke result_b.txt
    else:

    
########################################
    
# buat definisi nama broker yang akan digunakan


# buat client baru bernama P1
print("creating new instance")


# kaitkan callback on_message ke client


# buat koneksi ke broker
print("connecting to broker")


# jalankan loop client


# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic")


# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    

#stop loop
