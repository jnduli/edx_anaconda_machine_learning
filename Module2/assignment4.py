import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
df.columns = ['RK','PLAYER', 'TEAM','GP','G', 'A','PTS','+/-','PIM', 'PTS/G','SOG', 'PCT','GWG','PPG','PPA','SMG','SMA']
#print df
# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(axis=0, thresh=4)
#df.reset_index(drop =True)
#print df
# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df[df.PLAYER != 'PLAYER']
#df.reset_index(drop=True)
#print df

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=['RK'], axis=1)
#print df


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)
#print df

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#print df.dtypes
#print df.dtypes
df.GP = pd.to_numeric(df.GP, errors='coerce')
df.G = pd.to_numeric(df.G, errors='coerce')
df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')
df['+/-'] =pd.to_numeric(df['+/-'], errors='coerce')
df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df['PTS/G']= pd.to_numeric(df['PTS/G'], errors='coerce')
df.SOG = pd.to_numeric(df.SOG, errors='coerce')
df.PCT= pd.to_numeric(df.PCT, errors='coerce')
df.GWG = pd.to_numeric(df.GWG, errors='coerce')
df.PPG = pd.to_numeric(df.PPG, errors='coerce')
df.PPA =pd.to_numeric(df.PPA, errors='coerce')
df.SMG =pd.to_numeric(df.SMG, errors='coerce')
df.SMA =pd.to_numeric(df.SMA, errors='coerce')

print df.dtypes
print df
print 'details descibe'
print df.describe()
print 'shape'
print df.shape
print 'unique PCT'
print df.PCT.unique().size
print '14:15 GP'
print df.loc[15:16 , 'GP']
# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

