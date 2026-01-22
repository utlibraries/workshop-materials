import rasterio
import matplotlib 
from matplotlib import pyplot
from rasterio.plot import show
from rasterio.plot import show_hist

# Import a raster file
#%%
sm = rasterio.open("C:/Users/awm878/immersive_scripts/august_25_median_soil_moisture_texas.tif")
show(sm, cmap='pink')


#%%
# Show histogram
show_hist(sm, bins=50)
show(sm, cmap='pink', vmin=0, vmax=0.3, title="Raster Data Visualization")