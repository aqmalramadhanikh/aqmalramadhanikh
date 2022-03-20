#TIPE DATA TUPLE
#CONTOH TUPLE
nama = ("upin","ipin","ijat","mail","jarjit")
print(nama)
#TUPLE DENGAN PERULANGAN
nama = ("upin","ipin","ijat","mail","jarjit")
for i in nama:
    print(i)
#TUPLE DENGAN PERULANGAN WHILE
nama = ("upin","ipin","ijat","mail","jarjit")
i = 0
while i < len(nama):
    print(nama[i])
    i+=1
#UPDATE TUPLE
nama = ("upin","ipin","ijat","mail","jarjit")
nama=list(nama)
nama[2]="fizi"
print(nama)
#MENGHAPUS TUPLE
nama = ("upin","ipin","ijat","mail","jarjit")
nama=list(nama)
nama.pop(1)
print(nama)

nama = ("upin","ipin","ijat","mail","jarjit")
nama=list(nama)
del nama[0:3]
print(nama)
#MENAMBAHKAN TUPLE
nama = ("upin","ipin","ijat","mail","jarjit")
nama=list(nama)
nama.append("fizi")
print(nama)

nama.extend(["mei-mei","susanti"])
print(nama)

nama.insert(0,"ikhsan")
print(nama)
