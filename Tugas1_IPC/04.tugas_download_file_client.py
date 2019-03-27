# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:48:52 2019

@author: madit
"""

# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload

            
host = "127.0.0.1"  
                    


# definisikan port number proses di server
port = 12344 

# definisikan ukuran buffer untuk mengirim
buffer_size=1024

# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket() 

# lakukan koneksi ke server
s.connect((host,port))
print('berhasil terkoneksi')
# buka file bernama "hasil_download.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
with open('result.txt','wb') as res:
    print('menulis file')
# loop forever
    while 1:
        # terima pesan dari client
        data=s.recv(buffer_size)
        # tulis pesan yang diterima dari client ke file kita (result.txt)
        # berhenti jika sudah tidak ada pesan yang dikirim
        if not data: break
        res.write(data)
# tutup file_hasil_download.txt    
    res.close()
print('filereceived')
#tutup socket
s.close()