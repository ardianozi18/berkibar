country = {
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }

for key, val in country.items():
  for keys, vals in val.items():
    if keys == "capital":
      print('Ibukota '+key+" adalah " +vals)
