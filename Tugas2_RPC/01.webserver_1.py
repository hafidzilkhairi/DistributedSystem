# import library socket karena akan digunakan request reply protocol sederhana
import socket

# definisikan IP dan port dari webserver yang akan kita gunakan. Port HTTP adalah 80
SERVER_IP = "192.168.0.100"
SERVER_PORT = 80

# buat socket bertipe TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding 
sock.bind((SERVER_IP, SERVER_PORT))

# socket mendengarkan
sock.listen()

# tampilkan dengan print () "Server berjalan dan melayani HTTP pada port xx"
print("Server berjalan dan melayani HTTP pada port ", SERVER_PORT)

# loop forever
while True:
   
    # socket menerima koneksi
    connectionSocket, addr = sock.accept()
    
    # socket menerima data
    try:
        message = connectionSocket.recv(1024)
    
    # print data hasil koneksi
        print("Received :   ", message.decode())
    
    # buat response sesuai spesifikasi HTTP untuk diberikan kepada client
        http_response = ("""\HTTP/1.1 200 OK

<html>
<head>
<title>Web Server Sederhana</title>
</head>
<body>

<h1>Heading 1</h1>
<p>Ini adalah contoh paragraf.</p>
<img src="https://www.surfertoday.com/images/stories/surfetiquette.jpg">

</body>
</html>
""")
    # kirim response kepada client dengan sendall() jangan lupa diencode response dengan utf-8 
    
        connectionSocket.sendall(http_response.encode('utf-8'))
    except IOError:
        connectionSocket.send("404 Not Found")
    # tutup koneksi
        connectionSocket.close()

# Selamat! Kamu telah berhasil membuat web server sederhana. 