from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import polars as pl
import rasterio
from rasterio.plot import show
import requests
import os
import statsmodels

print("all packages imported successfully")

sealdivesdf = pd.read_csv("https://dataverse.tdl.org/api/access/datafile/62725?gbrecs=true")
print("sealdivesdf created successfully!")

treesdf = pd.read_csv("https://hub.arcgis.com/api/v3/datasets/15ae00ece1bf486a868c0f635d3acbfa_220/downloads/data?format=csv&spatialRefId=3857&where=1%3D1")
print("treesdf created successfully!")

customerchurndf = pd.read_csv("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/refs/heads/master/data/Telco-Customer-Churn.csv")
print("customerchurndf created successfully!")

singleimageband2 = {"bandname":"green",  "cmap":"Greens",  "url":"https://ut-austin.maps.arcgis.com/sharing/rest/content/items/21bfc72d87a844c8834db572bda24e58/data"}


#create a blank figure and save it using Matplotlib and then clear the figure with plt.clf()
plt.savefig("figures/blank_figure.jpg")
plt.clf()

#create a figure with two empty subplots and then clear the figure with plt.clf()
fig, axs = plt.subplots(1,2)
plt.savefig("figures/two-empty-subplots.jpg")
plt.clf()

#check names of columns containing data in the sealdivesdf data frame
print(sealdivesdf.columns.to_list())


#create and save a figure that shows a scatter plot of Weddell Seal Avg. Dive Depth vs Dive Duration and then clear the figure with plt.clf()
fig, axs = plt.subplots()
plt.scatter(x=sealdivesdf['Avg.Depth'], y=sealdivesdf['Duration'])
fig.suptitle('Weddell Seal Avg. Dive Depth vs Dive Duration', fontsize=16)
axs.set_xlabel('Avg. Depth')
axs.set_ylabel('Duration')

plt.savefig("figures/sealdives-avgdepth-vs-duration-scatterplot.jpg")
plt.clf()



#check names of columns containing data in the treedf data frame
print(treesdf.columns.to_list())



#process tree data to calculate average trunk diameter (DBH) for each tree family represented in the dataset and visualize the data as a bar chart using the pandas plot method
treefamilydbh=treesdf.groupby('Family')['DBH'].mean()
treefamilydbh.plot(kind="bar", xlabel="Family Name", ylabel="Avg. DBH", figsize=(12,14), color="#009900")
plt.suptitle('Avg. DBH of Portland, OR trees by Tree Family', fontsize=16)
plt.savefig("figures/tree-dbh-by-family.jpg")
plt.clf()

#process tree data to calculate counts for each tree family represented in the dataset and visualize the data as a bar chart using the pandas plot method
treefamilycounts = treesdf['Family'].value_counts()
treefamilycounts.plot(kind="bar")
plt.suptitle("Portaland, OR Parks Tree Inventory: Number of Trees in Each Family", fontsize=16)
plt.savefig("figures/tree-count-by-family.jpg")
plt.clf()



# #Create interactive Plotly scatter plot with ordinary least squares trendline
# fig = px.scatter(x=treesdf['TreeHeight'], y=treesdf['DBH'], trendline="ols")
# fig.show()



#check names of columns containing data in the customerchurn data frame

print("x lists")
print(customerchurndf['PaymentMethod'].unique())
print(customerchurndf['PaperlessBilling'].unique())
print(customerchurndf['Contract'].unique())
print(customerchurndf['PhoneService'].unique())
print()

valuecountspaymentmethod = customerchurndf['PaymentMethod'].value_counts().to_dict()
valuecountspaperlessbilling = customerchurndf['PaperlessBilling'].value_counts().to_dict()
valuecountscontract = customerchurndf['Contract'].value_counts().to_dict()
valuecountsphoneservice = customerchurndf['PhoneService'].value_counts().to_dict()

valuecountspaymentmethodk = list([k for k,v in valuecountspaymentmethod.items()])
valuecountspaymentmethodv = list([v for k,v in valuecountspaymentmethod.items()])
valuecountspaperlessbillingk = list([k for k,v in valuecountspaperlessbilling.items()])
valuecountspaperlessbillingv = list([v for k,v in valuecountspaperlessbilling.items()])
valuecountscontractk = list([k for k,v in valuecountscontract.items()])
valuecountscontractv = list([v for k,v in valuecountscontract.items()])
valuecountsphoneservicek = list([k for k,v in valuecountsphoneservice.items()])
valuecountsphoneservicev = list([v for k,v in valuecountsphoneservice.items()])



print(customerchurndf.columns.to_list())
fig, axs = plt.subplots(2,2,figsize=(16,16))
axs[0,0].bar(valuecountspaymentmethodk, valuecountspaymentmethodv)
axs[0,0].set_title("Payment Method")
axs[0,1].bar(valuecountspaperlessbillingk, valuecountspaperlessbillingv)
axs[0,1].set_title("Paperless Billing")
axs[1,0].bar(valuecountscontractk, valuecountscontractv)
axs[1,0].set_title("Contract Status")
axs[1,1].bar(valuecountsphoneservicek, valuecountsphoneservicev)
axs[1,1].set_title("Has Phone Service")
plt.suptitle("Potential Factors Affecting Customer Churn", fontsize=16)
fig.tight_layout(pad=2.0)
plt.savefig("figures/customerchurn-characteristics-bar-chart-subplots.jpg")
plt.clf()


