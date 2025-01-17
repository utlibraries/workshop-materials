'''
run the following pip commands in the terminal:
pip install geodatasets
pip install rasterio
pip install geopandas
pip install matplotlib
pip install certifi
pip install urllib3
pip install certifi
pip install zipfile
'''
import geopandas
import geodatasets
from geodatasets import get_path
from urllib.request import urlretrieve
import rasterio
import os
import matplotlib.pyplot as plt
import zipfile
import ssl
import certifi
ssl._create_default_https_context = ssl._create_unverified_context


#Establish an object that is the URL for the data we want to access. 
# If you're working locally you may want to provide a specific path (e.g.,"C:/Users/awm878/Downloads"). 
# The default path will likely be where you have the script file saved

url = ("https://curio.lib.utexas.edu/geodata/raster/utlmaps__ams__asia__1000k__6622985__rangoon_ne_47.zip")
filename = "ams_map.zip"

urlretrieve(url, filename)

# Path to the zip file
zip_file_path = 'ams_map.zip'

# Open the zip file in read mode
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all the contents to the current directory
    zip_ref.extractall('map-example')

from rasterio.plot import show
show(rasterio.open("map-example/utlmaps__ams__asia__1000k__6622985__rangoon_ne_47.jpg"))

#Now let's download a batch of files
import urllib

def get_filename(url):
    """
    Parses filename from given url
    """
    if url.find('/'):
        return url.rsplit('/', 1)[1]

# Filepaths
outdir = r"Example GeoData"

# File locations
url_list = ["https://curio.lib.utexas.edu/geodata/raster/utlmaps__sfi__austin_tx_1885__1k__x__6.zip",
            "https://curio.lib.utexas.edu/geodata/raster/utlmaps__sfi__austin_tx_1885__1k__x__7.zip",
            "https://curio.lib.utexas.edu/geodata/raster/utlmaps__sfi__austin_tx_1885__1k__x__8.zip"]

# Create folder if it does no exist
if not os.path.exists(outdir):
    os.makedirs(outdir)

# Download files
for url in url_list:
    # Parse filename
    fname = get_filename(url)
    outfp = os.path.join(outdir, fname)
    # Download the file if it does not exist already
    if not os.path.exists(outfp):
        print("Downloading", fname)
        r = urllib.request.urlretrieve(url, outfp)

for url in url_list:
    # Parse filename
    fname = get_filename(url)
    outfp = os.path.join(outdir, fname)

    # Unzip the file
    with zipfile.ZipFile(outfp, 'r') as zip_ref:
        zip_ref.extractall(outdir)

#******On your own: use urlretrieve to access the Austin Watershed Geojson from 
# the following site: https://data.austintexas.gov/Locations-and-Maps/Watershed-Boundaries/2829-xbvw/about_data


#Load a spatial dataset and assign it as a geodataframe
filename = "austin_was_map.geojson"
file = open(filename)
df = geopandas.read_file(file)

#if we simply write the name of file we can view the attribute table 
df

# to check the coordinate reference system us .crs
df.crs

#Now we'll project the dataset
gdf = df.to_crs("ESRI:102003")

#To produce a map use Plot with the attribute you want to display
gdf.plot("display_name", legend=True)

#Calculate the area of receiving basins

# Dissolve the geodataframe by receiving basin
dissolved = gdf.dissolve(by='receiving_basin')

# Calculate the area of each dissolved polygon
dissolved['area'] = dissolved.area

# Reset the index to make 'receiving_basin' a column again
dissolved = dissolved.reset_index()

# Print the resulting geodataframe
print(dissolved[['receiving_basin', 'area']])

#We can now plot our receiving basin map
dissolved.plot('receiving_basin', legend=True)

#For a proper legend we have to do a bit more work
ax = dissolved.plot(
    column="receiving_basin",
    categorical=True,
    legend=True,
    legend_kwds={"loc": "center left", "bbox_to_anchor": (1, 0.5), "fmt": "{:.0f}"},
)

#Now let's set receiving basin as our index to do a calculation

indexed = dissolved.set_index("receiving_basin")

lake_austin = indexed.loc["Lake Austin", "geometry"]
lake_austin

# buffering the active geometry by 1000 meters (geometry is already in meters)
indexed["buffered"] = indexed.buffer(1000)

indexed["buffered"].plot(alpha=0.5)

#Now we can calculate which watersheds are within 1000 meters of Lake Austin

indexed["buffered"].intersects(lake_austin)
