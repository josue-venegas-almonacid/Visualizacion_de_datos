import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Datos
df = pd.DataFrame({
'group': ['Facebook','Instagram','Tiktok'],
'18-24':    [21.5, 30.8, 38.9],
'25-34':    [29.9, 30.3, 32.4],
'35-44':    [19.4, 15.7, 15.6],
'45-54':    [11.6, 8.4, 7.9],
'55+':      [12.9, 6.9, 5.1]
})
 
# Crear radar
 
# Cantidad de variables
categories=list(df)[1:]
N = len(categories)
 
# Cantidad de ángulos del radar
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Configurar eje X
ax = plt.subplot(111, polar=True)
 
# Configurar ubicación para que la primera variable aparezca arriba
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Configurar etiquetas en cada ángulo por cada variable
plt.xticks(angles[:-1], categories)
 
# Mostrar etiquetas de graduación
ax.set_rlabel_position(0)
plt.yticks([10,20,30, 40, 50], ["10%","20%","30%", "40%", "50%"], color="grey", size=10)
plt.ylim(0,50)
 

# Mostrar datos
 
# Facebook
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Facebook", color='#3b5998')
ax.fill(angles, values, '#3b5998', alpha=0.1)
 
# Instagram
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Instagram", color='#f77737')
ax.fill(angles, values, '#f77737', alpha=0.1)

# Tik Tok
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Tiktok", color='#EE1D52')
ax.fill(angles, values, '#EE1D52', alpha=0.1)
 
# Mostrar leyenda
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Mostrar el gráfico
plt.show()