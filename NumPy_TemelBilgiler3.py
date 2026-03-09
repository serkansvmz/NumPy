import numpy as np
import math

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a) # dizideki uniq değerleri tanımlar
print(unique_values)

unique_values, indices_list = np.unique(a, return_index=True) # dizideki uniq değerlerin indeksini tanımlar
print(indices_list)

unique_values, occurrence_count = np.unique(a, return_counts=True) # uniq değerlerin kaç tane olduğunu tanımlar
print(occurrence_count) 

arr = np.arange(6).reshape((2, 3))
print(arr)

print(arr.transpose())
print(arr.T)

#----------Bir dizi nasıl tersine çevrilir---------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.flip(arr)) # tersten yazar

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

reversed_arr = np.flip(arr_2d) #tüm satır ve sütunu tersine çevirir
print(reversed_arr)

reversed_arr_rows = np.flip(arr_2d, axis=0) # satırı tersine çevirir
print(reversed_arr_rows) 

reversed_arr_rows = np.flip(arr_2d, axis=1) # sütunu tersine çevirir
print(reversed_arr_rows)  

arr_2d[1] = np.flip(arr_2d[1]) # sadece tek bir satırı tersine çevirir
print(arr_2d) 

arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)

