import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# параметры распределения
mu, sigma = 22, 2
x = np.linspace(15, 30, 500)
y = norm.cdf(x, mu, sigma)
# интервал
x_fill = np.linspace(20, 25, 200)
y_fill = norm.cdf(x_fill, mu, sigma)
plt.plot(x, y, label="Плотность вероятности f(x)")
plt.fill_between(x_fill, y_fill, alpha=0.4, color="red", label="P(20 ≤ X ≤ 25)")
plt.xlabel("Температура (°C)")
plt.ylabel("Плотность вероятности")
plt.legend()
plt.show() 