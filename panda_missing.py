import pandas as pd
df = pd.read_csv("Businessman.csv",parse_dates=["day"])
#print (df)
#print(type(df.day[1]))
df.set_index('day',inplace = True)
#print(df)
#new_df = df.fillna({'temperature' : 0,
#                    'windspeed': 0,
#                   'event': 'No event'})
#new_df = df.fillna(method = "ffill/bfill")
#new_df =df.fillna(method = "bfill",axis = "columns")
#To copy data from the next column
#new_df = df.fillna(method = "ffill", limit=1)
#new_df = df.interpolate()
#new_df = df.interpolate(method="time")
#new_df = df.dropna()
#new_df = df.dropna(how = "all") when all values are empty
#new_df = df.dropna(thresh=2) #keep ones where atleast 2 values are present
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)