# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('', 1234), RequestHandler = RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()
    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    cancidates = {
        'satu': 0,
        'dua': 0,
        'tiga': 0
    }
    
    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
    def vote_candidate(x):
        
        # critical section dimulai harus dilock
        lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan  nilai votenya
        
        
        # critical section berakhir, harus diunlock
        lock.release()
        
    
    # register fungsi vote_candidate() sebagai vote
    

    # buat fungsi bernama querry_result
    def querry_result():
        # critical section dimulai
        lock.acquire()
        
        # hitung total vote yang ada
        
        
        # hitung hasil persentase masing-masing kandidat
        
        
        # critical section berakhir
        lock.release()    
        
    # register querry_result sebagai querry
    


    print ("Server voting berjalan...")
    # Jalankan server
    
