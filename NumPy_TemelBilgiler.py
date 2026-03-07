import numpy as np
import math

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b=a[3:]
print(b)
b[0]=40
print(a)

a= np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a)
print(a[2,1]) # 3. satır 2. sütunu yazar, soldaki satır sağdaki sütun bilgisi index sıfırdan başladığı için 1 eksiği
print(a.ndim) # kaç boyutlu 
print(a.shape) # her boyutta kaç eleman var
print(len(a.shape)) # kaç boyutlu
print(a.size) # toplam öge sayısı
print(a.size==math.prod(a.shape)) # True döndürür
print(a.dtype)

#-------------------------------------------------------------

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

a=np.ones(5, dtype=np.float64)
print(a)
print(a.dtype)