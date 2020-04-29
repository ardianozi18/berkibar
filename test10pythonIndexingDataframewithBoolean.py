#Tampilkan semua data siswa pada mata pelajaran Ekonomi dan Fisika
ekonomi = df.pelajaran == 'Ekonomi'
fisika = df.pelajaran == 'Fisika'

print(df[(ekonomi)|(fisika)])


#Tampilkan semua data siswa yang mempunyai nilai lebih dari 50 di mata pelajaran Kimia
kimia = df.pelajaran == 'Kimia'
upper_50 = df.nilai > 50

print(df[(kimia)&(upper_50)])


#Tampilkan semua data yang mempunyai nilai lebih dari 70, berjnis kelamin perempuan dan di kelas 12C
perempuan = df.jenis_kelamin == 'perempuan'
upper_70 = df.nilai > 70
kelas_12c = df.kelas == '12C'

print(df[(perempuan)&(upper_70)&(kelas_12c)])