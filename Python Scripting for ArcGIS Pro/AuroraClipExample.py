# Description: Clip soils areas that fall within the railroad buffer zone
import pandas as pd
import pandasql as psql

df = pd.read_csv(r"C:\Users\brett\OneDrive\Documents\ArcGIS\Projects\2024_NE_NationalParkLands_MostVisitedSince2000\data sources\NPSLandsRecreationVisitsSince2000_NortheastRegion.csv")
df.head()