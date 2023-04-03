import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

regiones = ['Arica-Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaíso', 'Metropolitana', "O'Higgins", 'Maule', 'Ñuble', 'Bíobío', 'Araucanía', 'Los Ríos', 'Los Lagos', 'Aysén', 'Magallanes']

# Datos de las empresas
valores_cinehoyts = [0, 0, 3, 0, 2, 1, 22, 1, 1, 1, 1, 2, 0, 2, 0, 0]
valores_cinemark = [1, 1, 0, 0, 2, 3, 7,  2, 0, 0, 3, 0, 0, 1, 0, 0]
valores_amc = [0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0]

# Crear una figura
fig, ax = plt.subplots()

# Configurar los límites del eje y
ax.set_ylim(0, len(regiones))

# Crear las barras
ax.barh(regiones, valores_cinehoyts, height=-0.4, align='center')
ax.barh(regiones, [-v for v in valores_cinemark], height=0.4, align='center')
ax.barh(regiones, valores_amc, height=0.4, align='edge')

# Configurar los límites del eje x
ax.set_xlim(-max(valores_cinehoyts + valores_cinemark + valores_amc) * 1.1, max(valores_cinehoyts + valores_cinemark + valores_amc) * 1.1)

# Agregar etiquetas
ax.set_xlabel('Cantidad de cines por región en Chile')
ax.legend(['Cinehoyts', 'Cinemark', 'AMC'])

# Agregar marcas de graduación cada 5 unidades
plt.xticks(np.arange(-30, 30, 5))

# Agregar submarcas de graduación cada 1 unidad
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1))

# Agregar línea vertical en (0,0)
plt.axvline(x=0, color="black")

# Mostrar el gráfico
plt.show()
