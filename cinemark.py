# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe
group = ['Cinépolis', 'Cinemark', 'AMC']
values = [11, 15, 0]
df = pd.DataFrame({'group': group, 'values': values})

# Reorder it based on values:
ordered_df = df.sort_values(by='values')
my_range = range(1, len(df.index) + 1)

# Create a color if the group is "B"
my_color = np.where(ordered_df['group'] == 'Cinemark', 'blue', np.where(ordered_df['group'] == 'Cinépolis', 'cornflowerblue', 'lightsteelblue'))
my_size = np.where(ordered_df['group'] == 'Cinemark', 70, 30)

# The horizontal plot is made using the hline() function
plt.hlines(y=my_range, xmin=0, xmax=ordered_df['values'], color=my_color, alpha=1)
plt.scatter(ordered_df['values'], my_range, color=my_color, s=my_size, alpha=1)

# Add title and axis names
plt.yticks(my_range, ordered_df['group'])
plt.title("Presencia en América Latina", loc='left')
plt.xlabel('Cantidad de Países')
plt.ylabel('Group')

# show the graph
plt.show()
