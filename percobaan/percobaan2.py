import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5, 5))

plt.plot(xpoints, ypoints, color='red', marker='o', label='Data Points')

plt.xlim([0, 15])
plt.ylim([0, 15])

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.title('Contoh Plot Data')

plt.legend()
plt.show()
