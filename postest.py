print("operasi menentukan bangun bidang")
username = input(" masukan nama anda :")
input("masukan NIM anda : ")
password = input("masukan pasword anda :")

if password == "12344321":
    print("selamat anda berhasil login")
else :
    print("anda gagal login, coba lagi")

print ("------------------------------")
print ("menetukan bangun bola")
r = float(input("masukan jari jari bangun bola :"))
operasi = input("bisa dibagi 7 atau tidak bisa dibagi 7 :")

if operasi == "bisa dibagi 7" :
    hasil = 4 * 22/7 * r * r
    print (hasil)
elif operasi =="tidak bisa dibagi 7" :
    hasil = 4/3 * 3.14 * r * r * r
    print (hasil)
else :
    print ("hasil tidak diketahui")

print ("------------------------------")
print ("menentukan bangun tabung")
l = float(input("masukan luas alas tabung :"))
t = float(input("masukan tinggi tabung :"))
hasil = l * t
print (hasil)

print ("------------------------------")
print ("menentukan bangun limas segitiga")
x =  float(input("masukan luas limas :"))
y =  float(input("masukan tinggi limas segitiga :"))
hasil = 1/3 * x * y
print(hasil)