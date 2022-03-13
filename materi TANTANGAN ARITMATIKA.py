#contoh kasus sistem operasi aritmatika
pajak = 10/100
NIM=input("masukkkan NIM:")
gaji_pokok=int(input("masukkan gaji pokok:"))
lama_lembur=int(input("masukkan lamalembur:"))
gaji_lembur=int(input("masukkan gaji lembur:"))
gaji_utama=(gaji_lembur*lama_lembur-pajak+gaji_pokok)

print("NIM:",NIM)
print("gaji pokok:",gaji_pokok)
print("lama lembur:",lama_lembur)
print("gaji lembur:",gaji_lembur)
print("gaji utama:",gaji_lembur*lama_lembur-pajak+gaji_pokok)

