import numpy as np
import math 

#-------İndeksleme ve dilimleme---------

a = np.array([1, 2, 3])  # 3 elemanlı bu dizide; 1 -> 0. ve -3. indis, 2 -> 1. ve -2. indis, 3 -> 2. ve -1. indis oluyor
print(a[1]) # 1. indisi yazar yani 2
print(a[0:2]) # 0. indisten 2. indise kadar yazar 2. indisi yazmaz
print(a[1:])  # 1. indisten itibaren hepsini yazar
print(a[-3:])  # 3. indisten itibaren yazar


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[a<=7]) # 7 den küçük ve eşit olan elemanları yazar
print(a[a%2==0]) # 2 ile bölünebilen elemanları yazar
print(a[(a > 2) & (a < 11)]) 

b=[(a > 5) | (a == 5)]
print(b)

b = np.nonzero(a < 5)
print(b)


list_of_coordinates= list(zip(b[0], b[1])) 
for coord in list_of_coordinates:   
    print(coord)

#--------Mevcut verilerden bir dizi nasıl oluşturulur----------

a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

print(np.vstack((a1, a2))) # dikey olarak istifler
print(np.hstack((a1, a2))) # yatay olarak istifler

x = np.arange(1, 25).reshape(2, 12)
print(x)
print(np.hsplit(x,3)) # diziyi 3 eşit parçaya böler
print(np.hsplit(x,(3,4))) # diziyi 3. ve 4. sütundan sonra böler

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]
print(b1)
b1[0] = 99
print(b1)
print(a)  # b1 de yapılan değişiklik a da da değişir
b2=a.copy() # kopyasını oluşturur

#---------Temel dizi işlemleri-----------

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones) # toplama işlemi yapar
print(data - ones)
print(data * data)
print(data / data)

a = np.array([1, 2, 3, 4])
print(a.sum()) #elemanları toplar
print(a.max())
print(a.min())

b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0)) # sütunları toplar
print(b.sum(axis=1)) # satırları toplar

data = np.array([1.0, 2.0])
print(data * 1.6)