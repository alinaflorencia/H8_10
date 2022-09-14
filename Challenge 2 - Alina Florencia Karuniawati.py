#!/usr/bin/env python
# coding: utf-8

# In[14]:


def cek_angka(x):
    temp = 0
    for i in range(len(x)):
        if ord(x[i]) < 48 or ord(x[i]) > 57:
            temp +=1
    if temp == 0:
        return True
    elif temp > 0:
        return False

def conv_angka(x):
    dct = {0:'nol',1:'satu',2:'dua',3:'tiga',4:'empat',5:'lima',6:'enam',7:'tujuh',8:'delapan',9:'sembilan',10:'sepuluh',20:'dua puluh',
           30:'tiga puluh',40:'empat puluh',50:'lima puluh',60:'enam puluh',70:'tujuh puluh',80:'delapan puluh',90:'sembilan puluh'}
    if x <=10:
        return dct[x]
    if x <100 and x>10:
        if x % 10 == 0:
            return dct[x]
        else:
            return dct[x // 10 * 10] + ' '+dct[x%10]
    
angka = input('Masukkan angka:')
while cek_angka(angka) == False:
    print('Input harus dalam bentuk angka')
    angka = input('Masukkan angka:')
result = conv_angka(int(angka))
print(result)

