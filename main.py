#program menghitung luas dan keliling dari lingkaran, persegi, dan persegi panjang

def hitungLingkaran(r):
    pi = 22/7

    luas = pi*r*r
    keliling = pi*2*r

    print("Luas dari lingkaran dengan panjang jari-jari "+str(r)+" cm adalah "+str(luas)+" cm")
    print("Keliling dari lingkaran dengan panjang jari-jari "+str(r)+" cm adalah "+str(keliling)+" cm")

def hitungPersegi(s):
    luas = s*s
    keliling = 4*s

    print("Luas dari persegi dengan panjang sisi "+str(s)+" cm adalah "+str(luas) + " cm")
    print("Keliling dari persegi dengan panjang sisi "+str(s)+" cm adalah "+str(keliling) + " cm")

def hitungPersegiPanjang(p, l):
    luas = p*l
    keliling = (2*p) + (2*l)

    print("Luas dari persegi panjang dengan panjang "+str(p)+" cm dan lebar "+str(l)+" cm adalah " + str(luas) + " cm")
    print("Keliling dari persegi panjang dengan panjang "+str(p)+" cm dan lebar "+str(l)+" cm adalah " + str(keliling) + " cm")

def hitungSegitiga (s1, s2, s3):
    k = (s1+s2+s3)/2 #keliling segitiga
    l =  (k*(k-s1)*(k-s2)*(k-s3)) ** 0.5

    print("Keliling Segitiga dengan sisi "+str(s1)+" cm, "+str(s2)+", dan " + str(s3) + " cm, adalah " + str(k))
    print("Keliling Segitiga dengan sisi "+str(s1)+" cm, "+str(s2)+", dan " + str(s3) + " cm, adalah " + str(l))


print("Program untuk menghitung luas dan keliling dari lingkaran, persegi, dan persegi panjang")
print("Pilihan kode jenis bangun datar: 1. Lingkaran   2. Persegi   3. Persegi Panjang 4. Segitiga")
jenis = input("Masukkan kode jenis bangun datar yang diinginkan (angka 1-4): ")

if jenis=="1":
    r = int(input("Masukkan ukuran panjang jari-jari lingkaran (dalam cm): "))
    hitungLingkaran(r)
elif jenis=="2":
    s = int(input("Masukkan ukuran panjang sisi persegi (dalam cm): "))
    hitungPersegi(s)
elif jenis=="3":
    p = int(input("Masukkan ukuran panjang dari persegi panjang (dalam cm): "))
    l = int(input("Masukkan ukuran lebar dari persegi panjang (dalam cm): "))
    hitungPersegiPanjang(p, l)
elif jenis=="4":
    s1 = int(input("Masukkan ukuran sisi pertama segitiga (dalam cm): "))
    s2 = int(input("Masukkan ukuran sisi pertama segitiga (dalam cm): "))
    s3 = int(input("Masukkan ukuran sisi pertama segitiga (dalam cm): "))
    hitungSegitiga(s1, s2, s3)
else:
    print("Kode yang Anda masukkan salah. Selamat tinggal.")