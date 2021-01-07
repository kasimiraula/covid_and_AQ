import sys
import pandas as pd
from datetime import datetime

# Smear stock is UTC+2. This Converts it to UTC
def to_unix(timestring):
    dt = pd.to_datetime(timestring)
    return dt.timestamp()-7200

args=sys.argv[1:]

all_data = pd.read_csv(args[0], sep=",", error_bad_lines=False)
index = all_data.apply(lambda row: datetime(
                              int(row['Year']), int(row['Month']), int(row['Day']),
                              int(row['Hour']), int(row['Minute']), int(row['Second'])), axis=1)
unixtime = index.apply(lambda row : to_unix(row))

all_data = all_data.iloc[:,6:]

all_data = all_data.set_index(unixtime)
all_data.index.name = 'timestamp'
all_data = all_data.rename(columns={'KUM_META.t':'t', 'KUM_META.rh':'rh', 'KUM_META.p':'p', 'KUM_META.ws':'ws', 'KUM_META.wdir':'wdir', 'KUM_META.rmm':'rmm', 'KUM_META.PM10_TEOM':'PM10',
                    'KUM_META.PM25_TEOM':'PM2.5', 'KUM_META.NO_x' : 'NO_x', 'KUM_META.NO':'NO', 'KUM_META.O_3':'O_3', 'KUM_META.SO_2':'SO_2', 'KUM_META.CO':'CO'})

all_data.to_csv("smear-tsfixed.csv",index=True)
print('merging done')
