daftar = []

def menu_pilihan():
    print("1.menambahkan barang")
    print("2.mengurangi barang")
    print("3.cek barang")
    print("4.mengedit barang")
    print("5.ketersediaan barang")
    print("6.index barang")
    print("7.out")
    menu_pilihan = input("pilih menu:")
    if menu_pilihan == "1" :
        menambah_barang()
    if menu_pilihan == "2" :
        menghapus_barang()
    if menu_pilihan == "3" :
        cek_barang()
    if menu_pilihan == "4" :
        mengedit_barang()
    if menu_pilihan == "5" :
        sedia_barang()
    if menu_pilihan == "6" :
        index_barang()
    if menu_pilihan == "7" :
        out()

def menambah_barang():
    print("MENAMBAHKAN LIST BARANG")
    while True :
        masukkan_barang = input("masukkan nama barang yang ingin ditambahkan:")
        daftar.append(masukkan_barang)

        print("barang yang ditambahkan")
        for i in daftar :
            print(i)

        lanjut = input("lanjut menambahkan barang (y/n):")
        if lanjut == "y" :
            pass
        else :
            menu_pilihan()


def menghapus_barang():
    print("MENGURANGI LIST BARANG")
    while True :
        hapus_barang = input("masukkan nama barang yang ingin dikurangi:")
        daftar.remove(hapus_barang)

        print("barang yang dikurangi")
        for i in daftar :
            print(i)

        lanjut = input("lanjut mengurangi barang (y/n):")
        if lanjut == "y" :
            pass
        else :
            menu_pilihan()


def cek_barang() :
    print("barang anda")
    print("+","nomor barang".center(15,' '),"nama barang".center(20,' '),"+")
    for i in daftar :

        print("+     ",daftar.index(i)+1,"         |",  (i).center(18,' '),"+")
        pass
    menu_pilihan()


def mengedit_barang():
    print("ini adalah tempat mengedit barang anda")
    while True :
        edit_barang = input("masukkan nama barang anda:")
        ganti = input("ganti ke :")
        daftar[daftar.index(edit_barang)] = ganti
        print("+","nomor barang".center(15,' '),"nama barang".center(20,' '),"+")
        for i in daftar :
            print("+     ",daftar.index(i)+1,"         |",  (i).center(18,' '),"+")
        lanjut = input("Lanjut edit (y/n) : ")
        if lanjut == 'y':
            pass
        else :
            menu_pilihan()
        
def sedia_barang() :
    print("barang anda yang tersedia")
    while True :
        cari = input("cari barang anda:")
        if cari in daftar :
            print("barang teersedia!")
            lanjut = input("lanjut cek barang (y/n):")
            if lanjut == "y" :
                pass
        
            else :
                menu_pilihan()

        else :
            print("barang tidak tersedia!")
            break


def index_barang():
    print("ini adalah index barang anda")
    while True :
        cari = input("cari index barang:")
        if cari in daftar :
            print("barang pada index :",daftar.index(cari))
            lanjut = input("lanjut cek barang (y/n):")
            if lanjut == "y" :
                pass
            else :
               menu_pilihan()
   
        else :
            print("barang tidak tersedia!")
            break


def out():
    print([daftar])
        
        
            


            
menu_pilihan()
        
    
    
