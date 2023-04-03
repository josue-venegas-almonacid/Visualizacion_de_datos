import numpy as np
import pandas as pd
import circlify
import matplotlib.pyplot as plt

arr = np.array([0, 20000, 27000, 40000])
normalized_arr = (arr - arr.min()) / (arr.max() - arr.min())

df = pd.DataFrame({
    'Name': ['Cinemark', 'Cinépolis', 'AMC'],
    'Value': [20000, 27000, 40000]
})

# compute circle positions:
circles = circlify.circlify(
    df['Value'].tolist(),
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(10, 10))

# Title
ax.set_title('Cantidad de Empleados', fontsize = 20)

# Remove axes
ax.axis('off')

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# list of labels
labels = df['Name']

# print circles
for circle, label in zip(circles, labels):
    x, y, r = circle
    if label == 'AMC':
        ax.add_patch(plt.Circle((x, y), r, alpha=normalized_arr[3], linewidth=2, color='teal'))
    elif label == 'Cinemark':
        ax.add_patch(plt.Circle((x, y), r, alpha=normalized_arr[1], linewidth=2, color='teal'))
    else:
        ax.add_patch(plt.Circle((x, y), r, alpha=normalized_arr[2], linewidth=2, color='teal'))
    plt.annotate(
          label,
          (x,y ) ,
          va='center',
          ha='center',
        fontsize = 16
     )
print(normalized_arr)
plt.show()
