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
jan_22 = pd.read_csv(r'C:\Users\JiaQian\Desktop\Data\202201.csv')

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

# To determine number of rows for "ride_length" that are less than 1 minute
c_data[c_data['ride_length'] < 1].count()

# To determine number of rows that are null
c_data[c_data['ride_length'].isna()].count()

# To remove rows containing negative values and with "ride length" less than 1 minute
c_data = c_data[c_data['ride_length'] >= 1]
c_data = c_data.reset_index()
c_data = c_data.drop(columns = ['index'])

# To remove columns that won't be used 
c_data = c_data.drop(columns = ['start_station_name', 'start_station_id', 'end_station_name', 'end_station_id', 'start_lat', 'start_lng', 'end_lat', 'end_lng'])

# Adding two new columns, "month" and "hour"
c_data['month'] = c_data['started_at'].dt.month_name()
c_data['hour'] = c_data['started_at'].dt.hour

# To determine the number of member riders and casual riders in these 12 months
type = c_data.groupby(['member_casual'])['member_casual'].count()
print(type)

# To determine the number of member riders and casual riders each month
monthly = c_data.groupby(['month', 'member_casual'])['month'].count()
print(monthly)

# To determine the number of member riders and casual riders based on weeks
weekly = c_data.groupby(['day_of_week', 'member_casual'])['day_of_week'].count()
print(weekly)

# To determine the total number of riders based on time
time = c_data.groupby(['hour'])['hour'].count()
print(time)

# To determine the number of member riders and casual riders based on time
time2 = c_data.groupby(['hour', 'member_casual'])['hour'].count()
print(time2)

# To determine the number of member riders and casual riders based on bike type
bike = c_data.groupby(['rideable_type', 'member_casual'])['rideable_type'].count() 
print(bike)

# To determine the average ride time for members and casual riders
avgbymember = c_data.groupby(['member_casual'])['ride_length'].mean()
print(avgbymember)

# To determine the average ride time for members and casual riders each month
avgbymonth = c_data.groupby(['month', 'member_casual'])['ride_length'].mean()
print(avgbymonth)
