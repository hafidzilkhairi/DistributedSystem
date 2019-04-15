import os
import requests
import threading
import urllib.request, urllib.error, urllib.parse
import time

url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg" #link file yang akan didownload


def buildRange(value, numsplits):
    lst = []
    for i in range(numsplits):
        if i == 0:
            lst.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
        else:
            lst.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
    return lst

class SplitBufferThreads(threading.Thread):
    """ Splits the buffer to ny number of threads
        thereby, concurrently downloading through
        ny number of threads.
    """
    def __init__(self, url, byteRange):
        super(SplitBufferThreads, self).__init__()
        self.__url = url
        self.__byteRange = byteRange
        self.req = None

    def run(self):
        self.req = urllib.request.Request(self.__url,  headers={'Range': 'bytes=%s' % self.__byteRange})

    def getFileData(self):
        return urllib.request.urlopen(self.req).read()


def main(url=None, splitBy=3):
    start_time = time.time()#memulai perhitungan waktu untuk mengukur lamanya program berjalan
    if not url:#jika url belum terisi maka program terminate
        print("Please Enter some url to begin download.")
        return

    fileName = url.split('/')[-1]#mengambil nama file dari path url posisi paling akhir
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)#mengukur besar file yang akan didownload
    print("%s bytes to download." % sizeInBytes)#output besar file
    if not sizeInBytes:#jika sizeinbytes kosong maka program akan selesai
        print("Size cannot be determined.")
        return

    dataLst = []#deklarasi list
    for idx in range(splitBy):#mempartisi file kedalam beberapa bagian berdasarkan jumlah splitby (dalam kasus ini dibagi 3)
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]#membagi byte data sesuai dengan splitby yang ditentukan
        bufTh = SplitBufferThreads(url, byteRange)#mengassign threads dengan job sesuai dari pembagian yang dilakukan pada byterange
        bufTh.start()#mulai perkejaan mainthread (mengunggah)
        bufTh.join()#mainthread menunggu pekerjaan childthread selesai untuk dapat mengeksekusi perkejaan lainnya
        dataLst.append(bufTh.getFileData())#memasukkan data yang sudah diunggah kedalam list

    content = b''.join(dataLst)#menggabungkan isi datalst yang berupa byte 

    if dataLst:#jika datalst berhasil terisi maka akan mengoutputkan info waktu pengerjaan dan file serta menulis file yang sudah diunggah
        if os.path.exists(fileName):
            os.remove(fileName)
        print("--- %s seconds ---" % str(time.time() - start_time))
        with open(fileName, 'wb') as fh:
            fh.write(content)
        print("Finished Writing file %s" % fileName)

if __name__ == '__main__':
    main(url)#menjalankan program