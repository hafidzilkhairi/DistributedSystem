# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
ip='127.0.0.1'
# definisikan port number proses di server
port=12345

# definisikan ukuran buffer untuk mengirim

# buat socket (apakah bertipe UDP atau TCP?)
s=socket.socket()
# lakukan koneksi ke server
s.connect(('127.0.0.1',port))

# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
byte = open ("aku.txt","r")
try:
    # baca file tersebut sebesar buffer 
    l=byte.read(1024)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while l:
        # kirim hasil pembacaan file
        s.send(l.encode())
        
        # baca sisa file hingga EOF
        l = byte.read(1024)
        #print(byte)
        #print (byte)
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    byte.close()

# tutup koneksi setelah file terkirim
s.close()