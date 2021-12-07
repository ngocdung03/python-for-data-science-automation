# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# SQL DATABASES (Module 2): Working with SQLAlchemy ----

# IMPORTS ----
import pandas as pd
import sqlalchemy as sql

import os

os.mkdir("./00_database")
# CREATING A DATABASE ----

# Instatiate a database
engine = sql.create_engine("sqlite:///00_database/bike_orders_database.sqlite")  #first 2 slashes are required to connect to sqlite://. The 3rd slash is bcs the location "/00_database..."
conn = engine.connect()  #connect your sql alchemy engine object to your database

# Read Excel Files
bikes_df = pd.read_excel("./00_data_raw/bikes.xlsx")
bikeshops_df = pd.read_excel("./00_data_raw/bikeshops.xlsx")
orderlines_df = pd.read_excel("./00_data_raw/orderlines.xlsx")

# Create Tables
bikes_df.to_sql("bikes", con=conn)
pd.read_sql("SELECT * FROM bikes", con = conn)

bikeshops_df.to_sql("bikeshops", con=conn)
pd.read_sql("SELECT * FROM bikeshops", con = conn)

orderlines_df \
    .iloc[:,1:] \
        .to_sql("orderlines", con=conn, if_exists="replace")  #drop Unnamed column
pd.read_sql("SELECT * FROM orderlines", con = conn)

# Close Connection
conn.close()

# RECONNECTING TO THE DATABASE 

# Connecting is the same as creating
engine = sql.create_engine("sqlite://00_database/bikes_oerders_database.sqlite")
conn = engine.connect()

# GETTING DATA FROM THE DATABASE

# Get the table names
engine.table_names()  #deprecated

inspector = sql.inspect(conn)

inspector.get_schema_names()  #Database schema: this is the architechture of your database. It has a name. In our case it is "main"

inspector.get_table_names()  #Return the table names from an inspector object that is connected to your database.
#=inspector.get_table_names('main')

# Read the data
table = inspector.get_table_names()
pd.read_sql(f"SELECT * FROM {table[0]}", con=conn)  #Text manipulation with f-string: format text using glue-style syntax where we can add variables to the text

# Close connection
conn.close()