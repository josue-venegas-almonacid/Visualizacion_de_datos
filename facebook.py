import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Datos
x           = [2019, 2020, 2021, 2022, 2023]
facebook    = [2271, 2449, 2740, 2910, 2958]
instagram   = [1000, 1000, 1221, 1478, 2000]
tiktok      = [500, 800, 689, 1000, 1051]

# Crear gráfico de áreas superpuestas
plt.fill_between(x, facebook, color="#3b5998", alpha=0.5)
plt.fill_between(x, instagram, color="#f77737", alpha=0.5)
plt.fill_between(x, tiktok, color="#EE1D52", alpha=0.5)

# Agregar leyenda y título
plt.title('Cantidad de cuentas activas por año (en millones)')
plt.legend(['Facebook', 'Instagram', 'Tiktok'], loc='upper left')

# Agregar marcas de graduación en X cada 5 unidades
plt.xticks(np.arange(2019, 2024, 1))

# Agregar marcas de graduación en Y cada 500 unidades
plt.yticks(np.arange(0, 3500, 500))

# Agregar submarcas de graduación en Y cada 100 unidades
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(100))

# Agregar línea horizontal en máximos
plt.axhline(y=2900, color="#3b5998")
plt.axhline(y=2000, color="#f77737")
plt.axhline(y=1000, color="#EE1D52")

# Mostrar el gráfico
plt.show()
