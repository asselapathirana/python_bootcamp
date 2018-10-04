import matplotlib # we need matplotlib for plotting later
matplotlib.use('Qt5Agg') # Not esential. But QtAgg backend seems to work better for plotting

from matplotlib import pyplot as plt
import pandas as pd
import geopandas
from shapely.geometry import Point

#data downloaded from http://techslides.com/list-of-countries-and-capitals
#Note: there are lines with N/A as coordinates (where there is no capital city)
# Need to remove the comma in Washington, D.C. to avoid error in those lines!
df=pd.read_csv("country-capitals.csv", sep=',', error_bad_lines=False)
# create a new field coordinates
df['Coordinates'] = list(zip(df.CapitalLongitude, df.CapitalLatitude))

# now convert coordinates to points
df['Coordinates'] = df['Coordinates'].apply(Point)
# now create a geopandas object - a geodataframe
gdf = geopandas.GeoDataFrame(df, geometry='Coordinates')
print(gdf.columns)

# plot them 
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# We restrict to South America.
ax = world.plot(
    color='white', edgecolor='black')

# We can now plot our GeoDataFrame.
gdf.plot(ax=ax, color='red')
for idx, row in gdf.iterrows():
    v=row['Coordinates']
    plt.annotate(s=row['CapitalName'], xy=(v.x,v.y))
# show only part of the map (feel free to remove to get the whole world)
ax.set_xlim(60,100)
ax.set_ylim(0,40)
plt.show()