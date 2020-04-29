import pandas as pd
import random

pelajaran = ['Matematika', 'Fisika', 'Biologi', 'Kimia', 'Geologi', 'Ekonomi']
kelas = ['12A', '12B', '12C', '12D']

hasil_nilai = {
    'siswa_id' : range(1, 21),
    'pelajaran' : [random.choice(pelajaran) for i in range(20)],
    'nilai' : [random.choice(range(0, 100)) for i in range(20)],
    'jenis-kelamin' : [random.choice(['laki-laki', 'perempuan']) for i in range(20)],
    'kelas' : [random.choice(kelas) for i in range(20)]
}

df = pd.DataFrame(hasil_nilai)
print(df)