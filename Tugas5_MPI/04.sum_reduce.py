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

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
sum = comm.reduce(random_val, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank==0:
    print("Hasil Penjumlahan ",sum)
