"""
This program is perfom a basic visualisation process, using pandas, numpy & matplotlib.
This graph represents the location of big cities, which has over 5000 citizens in France, 1999.
"""

# Preparing libraries that help with visualisation.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read the csv file that contains the information of cities in France.
file = pd.read_csv('france.csv', delimiter=';')


# Extract the needed data (population >= 5000)
file = file[file['population'] >= 5000]
city, lat, lng, population, area = file['place'], file['x'], file['y'], file['population'], file['surface']


# Visualisation process.
plt.style.use('Solarize_Light2')  # Choose the style of the graph
plt.figure(figsize = (12, 7))  # Choose the figure size
plt.scatter(lat, lng,
            c=np.divide(population, 100.0), cmap='cividis',
            s=area*2, alpha=0.8, linewidths=0)


# Set the labels of axis
plt.ylabel("Longitude")
plt.xlabel("Latitude")
plt.axis('equal')
plt.colorbar(label="Population / 100")
plt.clim(0, 400)
plt.title("Cities with populations over 5000 in France, in 1999")


# Create a legend of areas of cities for the graph.
areas = [10, 100, 200, 300, 400]
for i in areas:
    plt.scatter([], [], s=i, c='k', alpha=0.5,
                label = str(i) + 'km$^2$')

plt.legend(title = "Area of city", labelspacing = 1)


plt.show()