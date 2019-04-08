# import SimpleXMLRPCServer bagian server


# buat fungsi bernama file_upload()
def file_upload(filedata):
    
    # buka file 
    with open("hasil_upload.txt",'wb') as handle:
        #convert from byte to binary IMPORTANT!
        data1=filedata.data
        
        # tulis file tersebut
        
        return True  #IMPORTANT
        
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"

# buat server


# tulis pesan server telah berjalan
print ("Listening on port 9999")

# register fungsi 


# jalankan server
