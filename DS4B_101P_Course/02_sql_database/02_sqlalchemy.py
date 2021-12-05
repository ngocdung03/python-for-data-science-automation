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


# Create Tables


# Close Connection

# RECONNECTING TO THE DATABASE 

# Connecting is the same as creating


# GETTING DATA FROM THE DATABASE

# Get the table names


# Read the data

