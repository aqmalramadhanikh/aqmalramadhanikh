#TIPE DATA SET
#CONTOH SET
nama = {"upin","ipin","fizi","ikhsan","mail"}
print(nama)
#SET DENGAN PERULANGAN
nama = {"upin","ipin","fizi","ikhsan","mail"}
for i in nama:
    print(i)
#SET DENGAN PERULANGAN WHILE
nama = {"upin","ipin","fizi","ikhsan","mail"}
nama=list(nama)
i = 0
while i < len(nama):
    print(nama[i])
    i+=1
#UPDATE SET
nama = {"upin","ipin","fizi","ikhsan","mail"}
nama=list(nama)
nama[2]="jarjit"
print(nama)
#MENGHAPUS SET
nama = {"upin","ipin","fizi","ikhsan","mail"}
nama=list(nama)
nama.pop(2)
print(nama)

del nama[0:3]
print(nama)
#MENAMBAHKAN SET
nama = {"upin","ipin","fizi","ikhsan","mail"}
nama=list(nama)
nama.append("jarjit")
print(nama)

nama.extend(["mei-mei","susanti"])
print(nama)

nama.insert(0,"ijat")
print(nama)

