print("nama : Aqmal Ramadhani KH")
print("***************************")
pilih = int(input('''1. mean
2. modus
3. medium
pilih menu diatas  : '''))
if pilih == 1:
        angka1 = int(input("masukkan data1 :"))
        angka2 = int(input("masukkan data2 :"))
        angka3 = int(input("masukkan data3 :"))
        angka4 = int(input("masukkan data4 :"))
        angka5 = int(input("masukkan data5 :"))
        angka6 = int(input("masukkan data6 :"))
        angka7 = int(input("masukkan data7 :"))
        data = angka1 + angka2 + angka3 + angka4 + angka5 + angka6 + angka7
        n = int(input("masukkan nilai n : "))
        hasil = data / n
        print("hasil = ",hasil)
if pilih == 2:
        angka1 = int(input("masukkan data1 :"))
        angka2 = int(input("masukkan data2 :"))
        angka3 = int(input("masukkan data3 :"))
        angka4 = int(input("masukkan data4 :"))
        angka5 = int(input("masukkan data5 :"))
        angka6 = int(input("masukkan data6 :"))
        angka7 = int(input("masukkan data7 :"))
        data = angka1,angka2,angka3,angka4,angka5,angka6,angka7
        frekuensi = dict.fromkeys(data, 0)
        for key,value in frekuensi.items():
            for i in data : 
                if i == key : 
                    frekuensi[key] += 1
        Modus = []
        frekuensi_terbanyak = 0
        print("jumlah frekuensi dari setiap data = ",frekuensi)
        for key,value in frekuensi.items():
            if value >= frekuensi_terbanyak : 
                frekuensi_terbanyak = key
            else : 
                pass
        for key,value in frekuensi.items():
            if value == frekuensi_terbanyak : 
                Modus.append(key)
        print("modus dari data tersebut adalah : ",Modus)
if pilih == 3:
        angka1 = int(input("masukkan data1 :"))
        angka2 = int(input("masukkan data2 :"))
        angka3 = int(input("masukkan data3 :"))
        angka4 = int(input("masukkan data4 :"))
        angka5 = int(input("masukkan data5 :"))
        angka6 = int(input("masukkan data6 :"))
        angka7 = int(input("masukkan data7 :"))
        data = [angka1,angka2,angka3,angka4,angka5,angka6,angka7]
        n = len(data)
        for i in range(n):
            for j in range(n-i-1):
                if data[j] > data[j + 1] :
                    data[j], data[j+1] = data[j+1] , data[j]
        print("data setelah diurutkan = ",data)
        if n % 2 != 0 :
            index_median = int((n+1)/2)
            print("median = ",data[index_median])
        else : 
            index_median = int((data[1+n/2] + data[1+1+n/2]) / 2)
            print("median = ",median[index_median])

else : 
    print("masukkan pilihan dengan benar!")
       

    

    
