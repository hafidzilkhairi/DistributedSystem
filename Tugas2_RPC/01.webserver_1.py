# import library socket karena akan digunakan request reply protocol sederhana


# definisikan IP dan port dari webserver yang akan kita gunakan. Port HTTP adalah 80


# buat socket bertipe TCP


# lakukan binding 


# socket mendengarkan


# tampilkan dengan print () "Server berjalan dan melayani HTTP pada port xx"


# loop forever
while True:
    # socket menerima koneksi
    
    
    # socket menerima data
    
    
    # print data hasil koneksi
    
    
    # buat response sesuai spesifikasi HTTP untuk diberikan kepada client
    http_response = """\HTTP/1.1 200 OK

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
"""
    # kirim response kepada client dengan sendall() jangan lupa diencode response dengan utf-8 
    
    
    # tutup koneksi
    

# Selamat! Kamu telah berhasil membuat web server sederhana. 