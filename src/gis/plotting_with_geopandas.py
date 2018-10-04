"""
Inspired from https://gist.github.com/jorisvandenbossche/7b30ed43366a85af8626#file-geopandas_lightning_talk-ipynb


How to run:
1. Download data https://land.copernicus.eu/local/urban-atlas/urban-atlas-2012?tab=download
(You need to register for free). Select Rotterdam and download the zip file. Extract the file.
2. Set the datafile variable to the path to NL003L3_ROTTERDAM_UA2012.shp file 

Note: This script will take around a minute (or more?) to run. Be paitent when running. 

"""
import os
import matplotlib # we need matplotlib for plotting later
matplotlib.use('Qt5Agg') # Not esential. But QtAgg backend seems to work better for plotting
from matplotlib import pyplot as plt
import geopandas

path='./data/rotterdam/Shapefiles/NL003L3_ROTTERDAM_UA2012.shp'
print("reading file ...")
data = geopandas.read_file(path) # read the shapfiles
print("Data boundaries: ", data.total_bounds) # what are the boundaries of the total dataset
# now set a window to extract data (subset)
minx,maxx,miny,maxy=(3924650.4677, 3934650.4677,3195659.78655, 3205659.78655) 
# extract that window
datasub = data[((data.bounds['minx'] < maxx) & (data.bounds['maxx'] > minx)
             & (data.bounds['miny'] < maxy) & (data.bounds['maxy'] > miny))]


# start a plot
fig, ax = plt.subplots(figsize=(12,10), subplot_kw={'aspect':'equal'})
# plot the subset of data
datasub.plot(column='ITEM2012', legend=True, ax=ax)
# set the boundaries of the plot
ax.set_xlim(minx, maxx)
ax.set_ylim(miny,maxy)
# We would like to move the legend outside the plot - so as not to block the view
leg = ax.get_legend() # get the legend
leg.set_bbox_to_anchor((1.7, .9)) # move it to this location
plt.show() # show the plot