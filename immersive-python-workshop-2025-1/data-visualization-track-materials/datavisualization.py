import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

print("all packages imported successfully")

cities = ["austin","dallas","houston", "san antonio", "el paso", "abilene"]
developercounts = [20000,10000,15000,8000,6000,1000]

fig, axs = plt.subplots()
# axs.set_title("Count of Developers in Major Texas Cities")
# axs.bar(cities, developercounts, color="#00aa00", edgecolor="#005500")
# plt.savefig(r"C:\Users\mgs2896\OneDrive - The University of Texas at Austin\Desktop\pythonworkshop\barchart.png")


treedata = pd.read_csv("https://hub.arcgis.com/api/v3/datasets/15ae00ece1bf486a868c0f635d3acbfa_220/downloads/data?format=csv&spatialRefId=3857&where=1%3D1")

# print(treedata['DBH'])
# print(treedata['TreeHeight'])

axs.scatter(treedata['DBH'], treedata['TreeHeight'])
plt.savefig(r"C:\Users\mgs2896\OneDrive - The University of Texas at Austin\Desktop\pythonworkshop\treedbhvsheightscatterplot.png")




