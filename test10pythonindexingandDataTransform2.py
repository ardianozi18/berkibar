#indexing data


df.loc['0':'21',['nilai','kelas']]

df.loc['0':,['nilai','kelas']]

df.iloc[5:11].loc[:,['pelajaran','nilai']]