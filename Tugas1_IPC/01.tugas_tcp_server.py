# import library socket karena akan menggunakan IPC socket
import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# definisikan alamat IP binding  yang akan digunakan 
ip = '0.0.0.0'

# definisikan port number binding  yang akan digunakan 
port = 65533

# definisikan ukuran buffer untuk mengirimkan pesan


# buat socket bertipe TCP

# lakukan bind
s.bind((ip,port))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(1)

# lakukan loop forever
while 1:
	# menerima koneksi
	conn, addr = s.accept()

	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
	print('connected by: ',addr[0],':',addr[1])

	# menerima data berdasarkan ukuran buffer
	data = str(conn.recv(1024).decode("utf-8"))

	# menampilkan pesan yang diterima oleh server menggunakan print
	print(data)

	# mengirim kembali data yang diterima dari client kepada client
	conn.send(data.encode())

# tutup koneksi	
s.close()
