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
