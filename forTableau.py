# Load libraries 
import pandas as pd
import numpy as np
import datetime

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

# Combining the datasets into one dataframe
c_data = pd.concat([feb_21, mar_21, apr_21, may_21, june_21, july_21, aug_21, sep_21, octo_21, nov_21, dec_21, jan_22 ])

# To change data type to datetime64
c_data['started_at'] = c_data['started_at'].astype('datetime64')
c_data['ended_at'] = c_data['ended_at'].astype('datetime64')

# Adding four new columns, "ride_length", "day_of_week", "month" and "hour"
c_data['ride_length'] = (c_data['ended_at']- c_data['started_at'])/pd.Timedelta(minutes = 1)
c_data['ride_length'] = c_data['ride_length'].astype('int32')

c_data['day_of_week'] = c_data['started_at'].dt.day_name()
c_data['month'] = c_data['started_at'].dt.month_name()
c_data['hour'] = c_data['started_at'].dt.hour

# To remove rows containing negative values and with "ride length" less than 1 minute
c_data = c_data[c_data['ride_length'] >= 1]
c_data = c_data.reset_index()
c_data = c_data.drop(columns = ['index'])

# To remove columns that won't be used 
c_data = c_data.drop(columns = ['start_station_name', 'start_station_id', 'end_station_name', 'end_station_id', 'start_lat', 'start_lng', 'end_lat', 'end_lng'])

# To split the dataframe based on month
# The reason being the dataframe containing all the months is too big and cannot be uploaded to Tableau
# Therefore, the data will be added one by one based on the months and it will all be combined using the union function in Tableau
df1 = df[df['month'] == 'January']
df2 = df[df['month'] == 'February']
df3 = df[df['month'] == 'March']
df4 = df[df['month'] == 'April']
df5 = df[df['month'] == 'May']
df6 = df[df['month'] == 'June']
df7 = df[df['month'] == 'July']
df8 = df[df['month'] == 'August']
df9 = df[df['month'] == 'September']
df10 = df[df['month'] == 'October']
df11 = df[df['month'] == 'November']
df12 = df[df['month'] == 'December']

# Saving the data in csv format
df1.to_csv("output1.csv")
df2.to_csv("output2.csv")
df3.to_csv("output3.csv")
df4.to_csv("output4.csv")
df5.to_csv("output5.csv")
df6.to_csv("output6.csv")
df7.to_csv("output7.csv")
df8.to_csv("output8.csv")
df9.to_csv("output9.csv")
df10.to_csv("output10.csv")
df11.to_csv("output11.csv")
df12.to_csv("output12.csv")
