import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

sample = np.random.normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(5, 4))
plt.hist(sample, bins=10, density=True)
plt.show()

sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

dist = norm(sample_mean, sample_std)

values = [value for value in range(30, 70)]

probabilities = [dist.pdf(value) for value in values]

plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilities)
plt.legend()
plt.show()
