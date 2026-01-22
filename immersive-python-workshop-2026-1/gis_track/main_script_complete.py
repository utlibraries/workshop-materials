#install Python and Jupyter extensions on VS Code

#%%
print("hello")


#%%
import sys
!{sys.executable} -m pip install geopandas pandas matplotlib mapclassify folium shapely

import geopandas as gpd
import pandas as pd
import folium
import matplotlib.pyplot as plt
import mapclassify
import shapely 
from shapely.geometry import Point

print("Packages installed successfully!")

#Import a geojson file
#%%
buildings = gpd.read_file("buildings.geojson")
buildings_url = gpd.read_file("https://curio.lib.utexas.edu/geodata/shapefiles/utlarch__bot__gm__point__v2__buildings_of_texas.zip")
#buildings_url.plot(markersize=0.5)
buildings.crs

#espg stands for European Petroleum Survey Group - they provide  standardized identifiers for coordinate reference systems (CRS)
#buildings = buildings.to_crs(epsg=32645) #Bangladesh
buildings = buildings.to_crs(epsg=32139)
buildings.plot(markersize=0.5)
buildings.crs
buildings.to_file("buildings_projected.geojson", driver="GeoJSON")

#Filter Data
#%%
buildings.head()
buildings_filtered = buildings[buildings['place_type'] == 'university building']
buildings_filtered.plot(markersize=0.5, color='red')

#Challenge: Bring in a new layer, "texas_county.geojson" and filter it to Travis county
# %%
texas_county = gpd.read_file("texas_county.geojson")
texas_county = texas_county.to_crs(epsg=32139)
texas_county.head()
travis_county = texas_county[texas_county['name'] == 'Travis']
travis_county.plot()

#now let's use both of our files to limit our buildings of texas file to only those in Travis county
#County information isn't in the buildings file, so this is where we utilize the geospatial component of our data 
# %%
travis_buildings = buildings.overlay(travis_county, how='intersection')
travis_buildings.plot(markersize=1)

#It seems like it worked, but to make it clear we need to plot both layers together
# %%
base = travis_county.plot(color='white', edgecolor='black')
ax = travis_buildings.plot(ax=base, markersize=1, color='red')
ax.set_axis_off()

#Now let's work with some qunatitative data - population by census tract in Travis county
# %%
pop = gpd.read_file("travis_pop_cleaned.geojson")
pop.head()
pop = pop.to_crs(epsg=32139)
pop.plot()
pop.plot(column='population', cmap='YlOrRd', legend=True, legend_kwds={"orientation": "horizontal", "pad": 0.1})

#Let's write a function to calculate population density - a more informative metric
# %%
#defining a new tool called calculate_population_density that takes in a geodataframe and returns a geodataframe
def calculate_population_density(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    gdf_copy = gdf.copy()
    # Calculate area in sq km for the entire column
    area_sq_km = gdf_copy.geometry.area / 1_000_000
    # Calculate population density using vectorized operations
    gdf_copy['pop_density'] = gdf_copy['population'] / area_sq_km
    return gdf_copy
# %%
# Calculate population density and plot the map
pop_with_density = calculate_population_density(pop)
pop_with_density['pop_density'] = pop_with_density['pop_density'].astype(float)
pop_with_density.plot(column='pop_density', cmap='YlOrRd', legend=True, legend_kwds={"orientation": "horizontal", "pad": 0.1})
pop_with_density.plot(column='pop_density', scheme='natural_breaks')
newgdf = pop_with_density.to_file("travis_pop_with_density.geojson", driver='GeoJSON')

# %%
# Create an interactive map visualizing population density
m = pop_with_density.explore(
    column='pop_density',  # The column you want to visualize
    cmap='YlOrRd',         # Color map (same as your static plot)
    legend=True,           # Show legend
    scheme='natural_breaks', # Classification scheme
    tiles='CartoDB positron'  # Base map style
)

# Display the map
m