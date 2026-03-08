import numpy as np
import math

#----------Dizi temelleri-----------------------------------

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b=a[3:]
print(b)
b[0]=40
print(a)

#-------Dizi öznitelikleri---------------------------------

a= np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a)
print(a[2,1]) # 3. satır 2. sütunu yazar, soldaki satır sağdaki sütun bilgisi index sıfırdan başladığı için 1 eksiği
print(a.ndim) # kaç boyutlu 
print(a.shape) # her boyutta kaç eleman var
print(len(a.shape)) # kaç boyutlu
print(a.size) # toplam öge sayısı
print(a.size==math.prod(a.shape)) # True döndürür
print(a.dtype)

#--------Temel bir dizi nasıl oluşturulur------------------

a=np.zeros(4) # Sıfırlardan oluşan 4 elemanlı
print(a)

a=np.ones(6) # Birlerden oluşan 6 elemanlı
print(a)

a=np.empty(3) # Rastgele elemenlı 
print(a)

a=np.arange(5) # 0 dan 5 e kadar giden dizi oluşturur
print(a)

a=np.arange(2,9,2) # 2 den 9 a kadar 2 şerli artan dizi oluşturur
print(a)

a=np.linspace(0, 10, num=5) # 0 dan 10 a kadar doğrusal artan 5 elemanlı dizi oluşturur 
print(a)

a=np.ones(5, dtype=np.float64) # veri türünü değiştirme
print(a)
print(a.dtype)

#------------Öğeleri ekleme, çıkarma ve sıralama-------------

a=np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(a)) # dizinin elemanlarını sıralı bir şekilde yazar

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a,b))) #İki diziyi birleştirir

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x,y), axis=0)) # dikey eksende birleştirir
print(np.concatenate((x, y.T), axis=1)) # yatay eksende birleştirir ama öncesinde y nin transpozunu almamız gerek
print(np.concatenate((x, y), axis=None)) # herhangi eksende birleştirmez ögeleri direk sırayla yazar

#-----------Bir dizinin şeklini ve boyutunu nasıl bilirsiniz-----------

a = np.array([[[0, 1, 2, 3], 
               [4, 5, 6, 7]], 
               
              [[0, 1, 2, 3], 
               [4, 5, 6, 7]], 
                
              [[0 ,1 ,2, 3], 
               [4, 5, 6, 7]]])

print(a)
print(a.ndim) # dizinin boyutu
print(a.size) # dizinin öge sayısı
print(a.shape) # dizinin şekli

a = np.arange(6)
print(a)
b = a.reshape(3, 2) # a dizisini (3,2) lik matrise çevirir
print(b)

#---------1D dizi 2D diziye nasıl dönüştürülür --------

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape) #tek boyutlu bir dizi

a2 = a[np.newaxis, :] # (1,6) lık bir matrise dönüştürür
print(a2)
print(a2.shape)
a2 = a[:, np.newaxis] #  (6,1) lık bir matrise dönüştürür
print(a2)
print(a2.shape)

a = np.array([1, 2, 3, 4, 5, 6])
print(a,"->", a.shape)
b = np.expand_dims(a, axis=1) # a dizisini sütun vektörüne dönüştürür
print(b,"->", b.shape )
c = np.expand_dims(a, axis=0) # a dizisini satır vektörüne dönüştürür
print(c,"->", c.shape)
