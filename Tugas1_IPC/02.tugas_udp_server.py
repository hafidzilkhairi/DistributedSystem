# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP bind dari server
UDP_IP = "0.0.0.0"

# definisikan port number untuk bind dari server
UDP_PORT = 12344

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan bind
sock.bind((UDP_IP, UDP_PORT))

# loop forever
while True:
    # terima pesan dari client
    data, addr = sock.recvfrom(1024)    
    
    # menampilkan hasil pesan dari client
    print (data)
    
sock.close()    
