# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
s = socket.socket

# definisikan target port number server yang akan dituju
UDP_IP = "10.20.1.92"
UDP_PORT = 12344
PESAN = "HHHAAALLLOOOOOOOO"

print ("target IP:", UDP_IP) 
print ("target port:", UDP_PORT)
print ("pesan:", PESAN)

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan loop 10 kali
for x in range (10):
    # definisikan pesan yang akan dikirim
    PESAN = "HHHAAALLLOOOOOOOO"
    
    # kirim pesan
    sock.sendto(PESAN.encode(), (UDP_IP,UDP_PORT))    
sock.close()
