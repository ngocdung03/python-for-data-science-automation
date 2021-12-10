# IMPORTS ----

import sqlalchemy as sql
import pandas as pd
from sqlalchemy.sql.expression import table


# COLLECT DATA ----
def collect_data(conn_string = "sqlite:///00_database/bike_orders_database.sqlite"):
    """[summary]
    Collects and combines the bike orders data.
    Args:
        conn_string (str, optional): A SQLAlchemy connection string to find the database. Defaults to "sqlite:///00_database/bike_orders_database.sqlite".

    Returns:
        DataFrame: A pandas data frame that combines data from tables:
            - orderlines: Transaction data
            - bikes: Products data
            - bikeshops: Customer data
     """
    # Body

    # 1.0 Connect to database
    engine = sql.create_engine(conn_string)
    conn = engine.connect()
    table_names = ['bikes', 'bikeshops', 'orderlines']       # Hardcoding table names is a good idea because our database will grow in the future, but our raw data will always reside in 3 tables: bikes, bikeshops, orderlines
    data_dict = {}
    for table in table_names:
        data_dict[table] = pd.read_sql(f"SELECT * FROM {table}", con=conn) \
            .drop("index", axis =1)
    conn.close()

    # 2.0 COmbining and cleaning data
    #data_dict['bikes']  #checking, similar to the other 2 dataframes
    joined_df = pd.DataFrame(data_dict['orderlines']) \
        .merge(
            right   = data_dict['bikes'],
            how     = 'left',
            left_on = 'product.id',
            right_on = 'bike.id',
        ) \
        .merge(
            right   = data_dict['bikeshops'],
            how     = 'left',
            left_on = 'customer.id',
            right_on = 'bikeshop.id',
        )

    # 3.0 Cleaning data
    #joined_df.info()

    df = joined_df

    df['order.date'] = pd.to_datetime(df['order.date'])

    temp_df = df['description'].str.split(" - ", expand=True)
    df['category.1'] = temp_df[0]
    df['category.2'] = temp_df[1]
    df['frame.material'] = temp_df[2]
    
    temp_df = df['location'].str.split(", ", expand = True)
    df['city'] = temp_df[0]
    df['state'] = temp_df[1]

    df['total.price'] = df['quantity'] * df['price']

    #df.columns 
    cols_to_keep_list = [
        'order.id', 
    'order.line', 
    'order.date', 
    'quantity',
    'price', 
    'total.price',
    'bikeshop.name', 
    'model', 
    'category.1', 
    'category.2',
    'frame.material', 
    'city', 
    'state'
    ]

    df = df[cols_to_keep_list]

    df.columns = df.columns.str.replace(".", "_", regex = False)  #ensure the literal "." is repaced and not treated as the regex command "find all"

    #df.info()
    return df