#TIPE DATA LIST
#CONTOH TIPE DATA LIST
nama = ["upin","ipin","mail","fizi","ikhsan"]
print(nama)
#MENAMPILKAN LIST DENGAN PERULANGAN
nama = ["upin","ipin","mail","fizi","ikhsan"]
for i in nama:
    print(i)
#MENAMPILKAN LIST DENGAN PERULANGAN WHILE
nama = ["upin","ipin","mail","fizi","ikhsan"]
i = 0
while i < len(nama):
    print(nama[i])
    i+=1
#MENGUPDATE LIST
nama = ["upin","ipin","mail","fizi","ikhsan"]
nama[2]="jarjit"
print(nama)
#MENGHAPUS LIST
nama = ["upin","ipin","mail","fizi","ikhsan"]
nama.pop(1)
print(nama)

nama = ["upin","ipin","mail","fizi","ikhsan"]
del nama[1:3]
print(nama)

#MENAMBAHKAN LIST
nama = ["upin","ipin","mail","fizi","ikhsan"]
nama.append("jarjit")
print(nama)

nama.extend(["mei-mei","susanti"])
print(nama)

nama.insert(0,"ijat")
print(nama)
