# load libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pandas.api.types import CategoricalDtype

# load datasets from February 2021 to January 2022 
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
