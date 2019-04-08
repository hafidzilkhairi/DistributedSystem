# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
server = xmlrpc.client.ServerProxy('http://127.0.0.1:1234')

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
server.vote("satu")

# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
server.query()

# lakukan pemanggilan fungsi lain terserah Anda