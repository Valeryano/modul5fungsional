import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

warna = ['red', 'green', 'blue', 'orange', 'purple']
ukuran = [50, 100, 150, 200, 250]
penanda = 'o' 

plt.scatter(x, y, c=warna, s=ukuran, marker=penanda, alpha=0.7, label='Titik Data')

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.title('Scatter Plot dengan Variasi')

plt.legend()
plt.show()
