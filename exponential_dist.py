import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# параметры распределения
lmbd = 0.2  # интенсивность (событий в час)
data = expon.rvs(scale=1/lmbd, size=1000)
# гистограмма и теоретическая плотность
x = np.linspace(0, 20, 500)
pdf = lmbd * np.exp(-lmbd * x)
plt.figure(figsize=(8,5))
plt.hist(data, bins=40, density=True, alpha=0.6, color="skyblue", edgecolor="black")
plt.plot(x, pdf, "r-", lw=2, label="Теоретическая плотность")
plt.xlabel("Время до события (часы)")
plt.ylabel("Плотность вероятности")
plt.title("Экспоненциальное распределение")
plt.legend()
plt.show() 