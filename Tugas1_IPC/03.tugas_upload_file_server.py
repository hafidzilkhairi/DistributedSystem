# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
IP='127.0.0.1'

# definisikan port untuk binding
PORT=12345

# definisikan ukuran buffer untuk menerima pesan
buf=1024

# buat socket (bertipe UDP atau TCP?)
s=socket.socket()

# lakukan binding ke IP dan port
s.bind((IP,PORT))

# lakukan listen
s.listen(1)

#  siap menerima koneksi
print("socket dalam state mendengarkan")
# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte


# loop forever
while 1:
    # terima pesan dari client
	conn, addr =s.accept()
	file=open("filebaru.txt",'w')
	data = conn.recv(buf).decode()
	while data:
    	# receive data and write it to file
		file.write(data)
		data = conn.recv(buf).decode()
    # tulis pesan yang diterima dari client ke file kita (result.txt)
	file.close()
	conn.close()
    # berhenti jika sudah tidak ada pesan yang dikirim
	if not 1:
		break

    
# tutup file result.txt    
s.close()

#tutup socket
s.close()