# import library SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
# import xmlrpc bagian client
import xmlrpc.client


# buatlah fungsi bernama download()
def file_download():
    # buka file bernama "phs.jpg"
    with open("file_didownload.txt", 'rb') as handle:
        # kirimkan file tersebut dalam bentuk xml dengan cara memanggil xmlrpc.client.Binary()
        binary_data = xmlrpc.client.Binary(handle.read())
        return binary_data


# buat server pada IP dan port yang telah ditentukan
with SimpleXMLRPCServer(("localhost", 45678)) as a:
    a.register_introspection_functions()

    # register fungsi download pada server
    a.register_function(file_download, 'file_download')

    # jalankan server
    a.serve_forever()
