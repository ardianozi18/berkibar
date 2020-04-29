#dengan fungsi
def normalized_nilai(x):
    return (x - x.min()) / (x.max() - x.min())

print(df[['nilai']].apply(normalized_nilai))



#tanpa fungsi
df['normalized_nilai'] = (df['nilai'] - df['nilai'].min()) / (df['nilai'].max() - df['nilai'].min())

print(df)


#dengan import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

df['normalized_nilai'] = MinMaxScaler().fit_transform(df[['nilai]])