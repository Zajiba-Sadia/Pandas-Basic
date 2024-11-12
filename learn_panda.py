#import pandas as pd
#df = pd.read_csv("panda.csv")
#print(df)
#df.shape
#print(df.tail(2))
#print(type(df.day))
#print(df[['event','day']])
#print(df['temperature'].std())
#print(df.describe())
#print(df[df.temperature >= 31])
#print(df[['day','temperature']][df.temperature == df.temperature.max()])
#print(df.index)

#df['day'] = pd.to_datetime(df['day'])
#df.set_index('day', inplace=True)
#print(df.loc['1/3/2017'])
#df.reset_index(inplace=True)

#print(df)

#import pandas as pd
#df = pd.read_csv("businessman.csv", na_values = {
 #   'eps':["not available","n.a"],
  #  'revenue':["not available","n.a",-1],
   # 'people':["not available","n.a"]
#})
#print(df.columns)
#df.to_csv("newcsv.csv", header=False )

import pandas as pd
df = pd.read_excel("businessman.xlsx","Sheet1")
print(df)