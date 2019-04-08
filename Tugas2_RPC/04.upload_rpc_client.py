# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
proxy = xmlrpc.client.ServerProxy("http://localhost:9999/")

# buka file yang akan diupload
with open("file_diupload.txt",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    data = xmlrpc.client.Binary(handle.read())

# panggil fungsi untuk upload yang ada di server
proxy.file_upload(data)
