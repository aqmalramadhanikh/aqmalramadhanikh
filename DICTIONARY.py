#TIPE DATA DICTIONARY
#CONTOH DICTIONARY
data={
    "nama":"aqmal",
    "umur":19,
    "alamat":"majene"
    }
#DICTIONARY DENGAN PERULANGAN
for i in data.items():
    print(i)

for i in data:
    print(i)

for i in data.values():
    print(i)
#UPDATE DICTIONARY
data={
    "nama":"aqmal",
    "umur":19,
    "alamat":"majene"
    }
data["alamat"]="tinambung"
print(data)
#MENGHAPUS DICTIONARY
data={
    "nama":"aqmal",
    "umur":19,
    "alamat":"majene"
    }
data.pop("alamat")
print(data)

print(data.popitem())

data.clear()
print(data)
#MENAMBAHKAN DICTIONARY
data={
    "nama":"aqmal",
    "umur":19,
    "alamat":"majene"
    }
data["status"]="mahasiswa"
print(data)
