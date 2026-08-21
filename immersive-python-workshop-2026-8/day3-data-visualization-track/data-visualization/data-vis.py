
try:
    import pandas as pd
    from matplotlib import pyplot as plt
    import plotly.express as px
    import io
    import requests
    import numpy as np
    import os

    print('success loading packages')

except Exception as e:
    print(str(e))
    print("ERROR: required packages could not be imported - use the command below to make sure required all packages are installed")
    print("pip install -r requirements.txt")



# download CSV of Weddel seal dive data from the Texas Data Repository at https://dataverse.tdl.org/file.xhtml?fileId=62725&version=1.1
# once the CSV is downloaded, copy the file into the ./data subdirectory in this repo
# source publication for this data is: Fuiman, L.A., T.M. Williams, and R.W. Davis. 2020. Homing tactics of Weddell seals in the Antarctic fast-ice environment. Marine Biology. (doi: 10.1007/s00227-020-03730-w)


if not os.path.isdir("./data"):
    os.mkdir("./data")

try:
    sealdivedf = pd.read_csv("./data/sealdivedata.csv")
    print("seal data loaded as df")


except Exception as e:
    print(str(e))
    print("ERROR: there was an issue reading the Weddel seal dive data - make sure you have downloaded the data and saved it as a CSV in the data directory in this local repo")

fig, axs = plt.subplots()

plt.savefig("./figures/blank_fig.png")

x_diveduration = sealdivedf["Duration"]
y_divedepth = sealdivedf["Avg.Depth"]

plt.scatter(x_diveduration,y_divedepth, color="#ff0000", alpha=.1, s=88)
plt.title("Weddell Seal Dive Duration vs Depth")
plt.xlabel("Dive Duration")
plt.ylabel("Dive Depth")


plt.savefig("./figures/sealdive_duration_vs_depth.png")
