import pandas as pd
from glob import glob
import os

listing_files = sorted(glob(os.path.join("idx_files", "CRMLSListing*.csv")))
sold_files = sorted(glob(os.path.join("idx_files", "CRMLSSold*.csv")))
print(listing_files)
print(sold_files)

true_listing_rows_before = sum(len(pd.read_csv(f)) for f in listing_files)
true_sold_rows_before = sum(len(pd.read_csv(f)) for f in sold_files)

print(f"True row count before concatenation for Listing: {true_listing_rows_before:,}")
print(f"True row count before concatenation for Sold: {true_sold_rows_before:,}")

print(f"Listing files loaded: {len(listing_files)}")
print(f"Sold files loaded: {len(sold_files)}")


listings = pd.concat((pd.read_csv(f) for f in listing_files), ignore_index=True)
sold = pd.concat((pd.read_csv(f) for f in sold_files), ignore_index=True)


#Listings rows before concatenation: 762,171
#Sold rows before concatenation: 678,512

print(f"Listings rows after concatenation: {len(listings):,}")
print(f"Sold rows after concatenation: {len(sold):,}")

#Listings rows after concatenation: 762,171
#Sold rows after concatenation: 678,512

listings = listings[listings["PropertyType"] == "Residential"]
sold = sold[sold["PropertyType"] == "Residential"]




print(f"Residential listings rows: {len(listings):,}")
print(f"Residential sold rows: {len(sold):,}")
#Residential listings rows: 501,639
#Residential sold rows: 453,907

listings.to_csv("Combined_Residential_Listings.csv", index=False)
sold.to_csv("Combined_Residential_Sold.csv", index=False)

print("Combined Residential CSV files saved successfully.")