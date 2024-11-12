import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')
#print(df.columns)
#print(df[['Name', 'Type 1', 'HP']][0:5])
#print(df.head(5))
#print(df.iloc[0:4])
#print(df.iloc[2,1])
#for index, row in df.iterrows():
#    print(index, row['Name'])
#print(df.loc[df['Type 1']=="Grass"])
#print(df.describe())
#print(df.sort_values(['Name', 'HP'], ascending = [1,0]))
#df['Total']=df['HP']+df['Attack']+df['Defense']+ df['Sp. Atk']+df['Sp. Def'] + df['Speed']
#print(df['Total'][0:5])
#df = df.drop(columns=['Total'])
#print(df.columns)
#df['Total'] = df.iloc[:, 4:10].sum(axis = 1) #axis = 0 for vertical
#cols = list(df.columns)
#df = df[cols[0:4] +[cols[-1]] + cols[4:12]]
#print(df.head(5))
#df.to_csv('modified.csv')
#FILTERING DATA
#new_df = (df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]) # for or, |
#new_df = new_df.reset_index() to reset index from 0
#new_df. reset_index(drop = True, inplace = True)
#print(new_df)
#mega = df.loc[~df['Name'].str.contains('Mega')] #for negating, ~
#reg = df.loc[df['Type 1'].str.contains('fire|Grass', flags = re.I, regex = True)] #to ignore case sensitivity
#pi = df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I, regex = True)]
#CONDITIONAL CHANGE
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
#print(df)
#df.loc[df['Type 1']=='Fire', 'Legendary'] = True
#df.loc[df['HP'] > 50, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
#print(df)

#df = pd.read_csv('pokemon_data.csv')
#print(df)
#baal = df.groupby(['Type 1']).mean(numeric_only= True)
#print(baal.apply(print))
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('pokemon_data.csv', chunksize= 20):
   results = df.groupby(['Type 1']).count()
   new_df = pd.concat([new_df, results])
print(new_df.apply(print))