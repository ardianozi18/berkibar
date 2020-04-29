ekonomi = df.pelajaran == 'Ekonomi'
fisika = df.pelajaran == 'Fisika'

print(df[(ekonomi)|(fisika)])