# DS4B 101-P: PYTHON FOR BUSINESS ANALYSIS ----
# Module 2 (Pandas Import): Importing Files ----

# IMPORTS ----
#%%
import pandas as pd

# 1.0 FILES ----

# - Pickle ----
pickle_df = pd.read_pickle("/00_data_wrangled/bike_orderlines_wrangled_df.pkl")
pickle_df.info()
# - CSV ----
# Be aware of data conversion: datetime, category
pd.read_csv("/00_data_wrangled/bike_orderlines_wrangled_df.csv", parse_dates = ['order_date'])  #parse_dates = True only applies for one column

# - Excel ----
pd.read_excel("/00_data_wrangled/bike_orderlines_wrangled_df.csv")
