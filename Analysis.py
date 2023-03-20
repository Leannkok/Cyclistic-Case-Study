# Load libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pandas.api.types import CategoricalDtype

# Load datasets from February 2021 to January 2022 
feb_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202102.csv')
mar_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202103.csv')
apr_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202104.csv')
may_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202105.csv')
jun_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202106.csv')
jul_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202107.csv')
aug_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202108.csv')
sep_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202109.csv')
octo_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202110.csv')
nov_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202111.csv')
dec_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202112.csv')
jan_21 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202201.csv')

# To ensure datasets have been loaded (previewing the top 5 columns from June 2021)
jun_21.head(5)

# Combining the datasets into one dataframe
c_data = pd.concat([feb_21, mar_21, apr_21, may_21, june_21, july_21, aug_21, sep_21, octo_21, nov_21, dec_21, jan_22 ])

# To check data type of the dataframe
c_data.dtypes

# To change data type to datetime64
c_data['started_at'] = c_data['started_at'].astype('datetime64')
c_data['ended_at'] = c_data['ended_at'].astype('datetime64')

# To check whether changes have been reflected
c_data.dtypes

# Adding two new columns, "ride_length" and "day_of_week"
c_data['ride_length'] = (c_data['ended_at']- c_data['started_at'])/pd.Timedelta(minutes = 1)
c_data['ride_length'] = c_data['ride_length'].astype('int32')

c_data['day_of_week'] = c_data['started_at'].dt.day_name()

# Sort "ride length" column in ascending order
c_data = c_data.sort_values(by = 'ride_length')

# To determine the number of rows contatining negative value for ride length
c_data[c_data['ride_length'] < 0].count()


