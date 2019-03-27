# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:48:54 2019

@author: madit
"""

# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
ip="127.0.0.1"

# definisikan port untuk binding
port=12344

# definisikan ukuran buffer untuk menerima pesan
buffer_size=1024

# buat socket (bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((ip, port))

# lakukan listen
s.listen(1)

#  siap menerima koneksi
conn, addr = s.accept()
print('Got connection from', addr)

# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python
filename='file_didownload.txt'
with open(filename,'rb') as f:
    try:
# baca file tersebut sebesar buffer 
        l = f.read(buffer_size)

# selama tidak END OF FILE; pada pyhton EOF adalah b''
        while l != b'':
    # kirim hasil pembacaan file dari server ke client
            while (l):
                conn.send(l)
                l = f.read(buffer_size)

    # baca sisa file hingga EOF
    finally:
        print ("end sending")

# tutup file jika semua file telah  dibaca
        f.close();

# tutup socket
s.close()

# tutup koneksi
conn.close()