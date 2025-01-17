'''
pip install osmnx
pip install geopandas
pip install matplotlib
pip install shapely
'''
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon

'''
Load a Country or City as a geodataframe and project it onto a plot

Notice the _ =

Python automatically stores the value of the last expression in the interpreter to a particular variable called "_."
'''
import osmnx as ox
country = ox.geocode_to_gdf('India')
ax = ox.project_gdf(country).plot()
_ = ax.axis('off')

#Same thing here but with a list

places = ox.geocode_to_gdf(['Botswana', 'Angola', 'Zambia', 'South Africa', 'Zimbabwe', 'Namibia'])
places = ox.project_gdf(places)
places.to_file('s-africa')
ax = places.plot()
_ = ax.axis('off')

'''
Produce a street network from a bounding box  (north, south, east, west)

You can also simply type the name of a location like we did before. 

But for many cities (e.g., Austin, NYC) it takes a long time to load everything within the location bounds.
'''
G = ox.graph_from_bbox(30.29, 30.27, -97.72, -97.75, network_type='drive')
G_projected = ox.project_graph(G)
ox.plot_graph(G_projected)

'''
Filter to find restaurants in Austin using the geometries_from_place function

https://wiki.openstreetmap.org/wiki/Key:amenity
'''
# List key-value pairs for tags
tags = {'amenity': 'restaurant'}

# Retrieve restaurants
restaurants = ox.geometries_from_place('Austin, Texas', tags)

# How many restaurants do we have?
len(restaurants)

#Check to see what columns are associated with restaurants
restaurants.columns.values

# Select some useful cols and print
cols = ['name', 'opening_hours', 'addr:city', 'addr:country',
        'addr:housenumber', 'addr:postcode', 'addr:street']

# Print only selected cols
restaurants[cols].head(100)

#Now let's make a cool looking map
# define a bounding box
north, south, east, west = 30.29, 30.27, -97.72, -97.75

#convert the bounding box to a polygon
poly = ox.utils_geo.bbox_to_poly(north, south, east, west)

#convert the polygon to a geo data frame
region = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[poly])

#building: True means that every type of buildings will be downloaded
buildings = ox.features_from_bbox(north, south, east, west, tags = {'building': True})

#Using graph module we will recieve graph of roads in the city
roads = ox.graph.graph_from_bbox(north, south, east, west)

#Here we specify specific tags
rivers = ox.features_from_bbox(north, south, east, west, tags = {'waterway': True})
parks = ox.features_from_bbox(north, south, east, west, tags = {'leisure': 'park'})
univeristy = ox.features_from_bbox(north, south, east, west, tags = {'amenity': 'university'})

#city
ax = region.plot(facecolor = '#333f48', figsize=(85,85))
ax.set_facecolor('#d6d2c4')


univeristy.plot(facecolor = 'grey',
            edgecolor = 'grey',
            linewidth = 2,
            markersize = 1,
            ax = ax)

buildings['geometry'].plot(facecolor = '#bf5700',
                           edgecolor = '#bf5700',
                           linewidth = 1,
                           markersize = 1,
                           ax = ax)

parks.plot(facecolor = '#1b9e77',
            edgecolor = '#1b9e77',
            linewidth = 2,
            markersize = 1,
            ax = ax)

rivers.plot(edgecolor = '#2c7fb8',
            linewidth = 8,
            linestyle = '-',
            ax = ax)

ox.plot_graph(roads,
              edge_color = 'white',
              node_color = 'white',
              edge_linewidth=1,
              node_size = 1,
              ax=ax)

ax.grid('on', which='major', axis='x', color = '#99A2A2')
ax.grid('on', which='major', axis='y', color = '#99A2A2')
plt.show()