import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
# параметры распределения
a, b = 10, 40
size = 10000
# генерация выборки
data = uniform.rvs(loc=a, scale=b-a, size=size)

# построение гистограммы и теоретической плотности
x = np.linspace(a, b, 1000)
pdf = uniform.pdf(x, loc=a, scale=b-a)
plt.figure(figsize=(8,5))
plt.hist(data, bins=40, density=True, alpha=0.6, color="skyblue", label="Смоделированные данные")
plt.plot(x, pdf, "r-", lw=2, label="Теоретическая плотность")
plt.xlabel("Значения X")
plt.ylabel("Плотность вероятности")
plt.title("Равномерное распределение")
plt.legend()
plt.show() 