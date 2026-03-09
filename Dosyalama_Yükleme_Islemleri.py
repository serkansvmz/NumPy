import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
np.save('filename',a) #   filename.npy olarak kaydeder

b = np.load('filename.npy') # tekrardan kullanmak için
print(b)

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', csv_arr) # .csv dosyası
np.savetxt('new_file.txt', csv_arr) # .txt dosyası
print(np.loadtxt('new_file.csv'))   # dosyayı geri yükleme

import pandas as pd

a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

df = pd.DataFrame(a)
print(df)
df.to_csv('pd.csv') 
data = pd.read_csv('pd.csv')
np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')

