x = int(input("Masukkan Nomor:"))
def fungsi(x):
  if x % 2 == 0 or x>1 and x<=5:
    print("Tidak Aneh")
  elif x % 2 == 0 and x>=6 and x<=20:
    print("Aneh")
  elif x % 2 == 0 and x>20:
    print("Tidak Aneh")
  elif x % 2 != 0:
    print("Aneh")
  else:
    print("Tidak ada")
  return x
print(fungsi(x))