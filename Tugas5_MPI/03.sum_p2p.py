# import mpi4py
from mpi4py import MPI
import numpy as np
# import library random untuk generate angka integer secara random


# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank=comm.Get_rank()

# dapatkan total proses berjalan
size=comm.Get_size()

# generate angka integer secara random untuk setiap proses
random_val = np.random.randint(100)
# jika saya adalah proses dengan rank 0 maka:

# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank== 0:
    sum = random_val 
    for i in range(1,size):
        sum += comm.recv(source=i)
        print("Hasil Penjumlahan %d" %sum)
	
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
	comm.send(random_val, dest=0)


