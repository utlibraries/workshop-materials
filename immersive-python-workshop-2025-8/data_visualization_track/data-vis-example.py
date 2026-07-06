# print("hello")

import os
import json
import matplotlib.pyplot as plt
import pandas as pd
import polars as pl
import datetime

print("all packages imported successfully")


#use polars to create a dataframe from the air quality index data downloaded from https://aqs.epa.gov/aqsweb/airdata/daily_aqi_by_county_2023.zip
df = pl.read_csv("daily_aqi_by_county_2023.csv")


#create a modified copy of the data frame which converts the string information in the Date column to a date object and then converts the date object to the corresponding day of the year value that is saved in a new column "day_of_year"
df_day_of_year = df.with_columns(pl.col("Date").str.to_date().dt.ordinal_day().alias("day_of_year"))

#created a modified copy of the df_day_of_year data frame which filters out only the records for Travis County in Texas
travis_df_day_of_year = df_day_of_year.filter(pl.col("county Name") == "Travis")

#print the data frame to verify the ordinal day of the year values were calculated correctly and records have been filtered to just Travis County
print(travis_df_day_of_year)

#create a scatter plot of the air quality data for Travis County showing how it changed over the course of the year in 2023
chart = (travis_df_day_of_year.plot.point(x="day_of_year",y="AQI"))

#save the created chart out as a PNG file naes "example.png"
chart.save("example.png")


