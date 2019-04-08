# import xmlrpc bagian client
import xmlrpc.client

# buat proxy untuk mengakses server. Gunakan parameter URL server yang akan diakses berupa IP dan port. Bentuk http://IP:port
s = xmlrpc.client.ServerProxy('http://192.168.43.122:45678')

# buat/buka file baru dengan nama "hasil_download.txt" sebagai hasil download dari server
with open("hasil_didownload.txt", "wb") as handle:
    xmldata = s.file_download()

    # tulis/isi file hasil_download.jpg dengan hasil dari memanggil fungsi "download" yang berada server
    handle.write(xmldata.data)

# ubah file menjadi binary dengan menambahkan .data
