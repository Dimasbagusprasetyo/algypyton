ulang="y"
while ulang=="y" or ulang =="Y":
    print("===========================")
    print(" CEK Nilai Mahasiswa")
    print("===========================")
    n= 0
    while n>=0 and n<=100:
        u = input("Masukan Nilai = ")
        n = int(u)
        if n>0 and n<=100:
            if n>=91:
                    sts= "A"
            elif n>=81:
                    sts= "B"
            elif n>=71:
                    sts="C"
            else: sts="D"
            print(sts)
            ulang=input("Ingin Mengecek Kembali? y/t = ")
            if ulang=="t" or ulang =="T":
                break
        else:
            pesan="Masukan Kembali Nilai Angka Antara 0-100"
            print(pesan)
            print()
