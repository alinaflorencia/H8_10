import random

def cek_angka(x):
    temp = 0
    for i in range(len(x)):
        if ord(x[i]) < 48 or ord(x[i]) > 57:
            temp +=1
    if temp == 0:
        return True
    elif temp > 0:
        return False

print("="*50)
print("Permainan Tebak Angka")
print("="*50)
print("Saya memikirkan sebuah angka dari 0-9")
print("Input HARUS dalam bentuk ANGKA")

initial_point = 100
angka = random.randint(0,9)

def cek_tebakan(x, angka):
    if int(x) == angka:
        return True
    elif int(x) > angka or int(x) < angka :
        return False

menang = False
chance = 0
while True:
    angka_tebakan = input('Masukkan angka:')
    while cek_angka(angka_tebakan) == False:
        print("Penalty, point dikurangi 20")
        initial_point -= 20
        print("Score anda saat ini:", initial_point)
        chance+=1
        if chance >= 3:
            break
        angka_tebakan = input('Masukkan angka:')

        
    while cek_angka(angka_tebakan) == True or cek_angka(angka_tebakan) == False:
        if cek_angka(angka_tebakan) == False:
            chance+=1
            initial_point -= 20
            print("Penalty, point dikurangi 20")
            print("Score anda saat ini:", initial_point)
            break
        elif cek_tebakan(angka_tebakan,angka) == True:
            print("Selamat Anda Menang dengan score", initial_point)
            menang = True
            break
        else:
            chance+=1
            initial_point -=10
            if int(angka_tebakan) < angka:
                print("tebakan terlalu kecil")
                print("Score Anda saat ini", initial_point)
            else:
                print("tebakan terlalu besar")
                print("Score Anda saat ini", initial_point)
            if chance >= 3:
                break
            angka_tebakan = input('Masukkan angka:')
    
            
    if chance >= 3:
        print("Anda Kalah")
        break
    if menang == True:
        break