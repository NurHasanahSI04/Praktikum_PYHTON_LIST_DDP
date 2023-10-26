#1. Buat variabel list dengan value: [namakendaraan,jeniskendaraan,cckendaraan,warnakendaraan,rodakendaraan]
my_list=["Motor","Darat",155,"MagnificentRed",4]
print("variabel list =", my_list)

#tambahkan dari list tersebut dibelakang value:[hargakendaran,tipekendaraan]
my_list.append("32894000,CBS")
print("tambahkan dari list tersebut dibelakang value:[hargakendaran,tipekendaraan]")
print("hasil =", my_list)

#tambahkan setelah jenis kendaraan dengan value:[merkkendaraann]
my_list.insert(2,"hondaPCX")
print("tambahkan setelah jenis kendaraan dengan value:[merkkendaraann]")
print(my_list)


#2.Buat Program Pyhton dengan match case untuk menghitung luas bangun datar:
ket = '''menghitung luas bangun datar dengan program pyhton
Silahkan pilih opsi untuk menjalankan program
1. luas persegi
2. luas lingkaran
3. luas segitiga'''

pilihan = input(ket)
pilihan = input("masukan pilihan 1/2/3 :")
match pilihan:
    case"1":
        print("anda memilih nomor 1 untuk menghitung luas persegi")
        s = float(input("masukan sisi? "))
        luas = s*s
        print("Hasil Luas Persegi=", luas)
    case"2":
        print("anda memilih nomor 2 untuk menghitung luas lingkaran")
        j = float(input("masukan jari-jari: "))
        luas =3.14*j**2
        print("Hasil Luas Lingkaran =", int(luas))
    case"3":
        print("anda memilih nomor 3 untuk menghitung luas segitiga")
        alas = int(input("masukan alas : "))
        tinggi = int(input("masukan tinggi: "))
        luasS = alas*tinggi/2
        print("Hasil Luas Segitiga", int(luasS))
    case _:
        print("anda salah memilih")