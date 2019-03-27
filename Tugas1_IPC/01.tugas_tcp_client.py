# import library socket karena akan menggunakan IPC socket
import socket
s = socket.socket()
# definisikan tujuan IP server
ip = '127.0.0.1'

# definisikan port dari server yang akan terhubung
port = 65533

# definisikan ukuran buffer untuk mengirimkan pesan


# definisikan pesan yang akan disampaikan
pesan = "Haiii"

# buat socket TCP
# socket.c(ip,port)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((ip,port))

# kirim pesan ke server
s.sendall('TCP packet from client'.encode())

# terima pesan dari server
data = s.recv(1024)

# tampilkan pesan/reply dari server
print("Pesan dari server: ",str(data.decode("utf-8")))

# tutup koneksi
s.close()

