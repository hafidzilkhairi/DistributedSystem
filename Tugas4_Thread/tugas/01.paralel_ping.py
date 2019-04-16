# import os, re dan threading
import os, re, threading

# import time
import time

# buat kelas ip_check
class ip_check(threading.Thread):
    
    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__ (self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.status = -1
    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        pingAction = os.popen('ping -c 2 '+str(self.ip))
        
        # loop forever
        while True:
            # baca hasil respon setiap baris
            resultPerLine = pingAction.readline()
            
            # break jika tidak ada line lagi
            if not resultPerLine:
                break
            
            # baca hasil per line dan temukan pola Received = x
            pola = re.findall(r"(\d) received", resultPerLine)
            
            # tampilkan hasilnya
            if pola:
                self.status = int(pola[0])
                
    # fungsi untuk mengetahui status; 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def statusM(self):
        # 0 = tidak ada respon
        #print('status: ',self.status)
        if self.status == 0:
            return "Tidak ada respon"
        # 1 = ada loss
        if self.status == 1:
            return "Hidup tapi ada yang loss"
        # 2 = hidup
        if self.status == 2:
            return "Hidup"
        # -1 = seharusnya tidak terjadi
        return "Seharusnya tidak terjadi"
# buat regex untuk mengetahui isi dari r"Received = (\d)"


# catat waktu awal
waktuAwal = time.time()

# buat list untuk menampung hasil pengecekan
check_results = []

# lakukan ping untuk 20 host
for suffix in range(1,244):
    # tentukan IP host apa saja yang akan di ping
    ip = "10.100.77."+str(suffix)
    # panggil thread untuk setiap IP
    t = ip_check(ip)
    
    # masukkan setiap IP dalam list
    check_results.append(t)
    
    # jalankan thread
    t.start()

# untuk setiap IP yang ada di list
for el in check_results:
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya
    print(el.ip,' ',el.statusM())

# catat waktu berakhir
waktuAkhir = time.time()

# tampilkan selisih waktu akhir dan awal
print(waktuAkhir-waktuAwal)
