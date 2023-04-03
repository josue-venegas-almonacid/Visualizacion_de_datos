# libraries
import matplotlib
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
import pandas as pd

# Create a data frame with fake data
groups = ['Instagram', 'Facebook', 'TikTok']
values = [33, 25, 12]
# values.sort(reverse=True)
df = pd.DataFrame({'value': values, 'group': groups})

# create a color palette, mapped to these values
cmap = matplotlib.cm.Blues
mini=0
maxi=max(values)
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in values]


sizes = squarify.normalize_sizes(values,100,0)[::-1]
# plot it
squarify.plot(sizes=df['value'], label=df['group'], alpha=.8, color=colors)
plt.axis('off')
plt.title('Retorno de la inversión al vender directamente en la app')
plt.show()



