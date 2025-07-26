import json
import csv
i = 0
while i < 86:
  i += 1v
  print(i)
  with open(f'{i}_country_fr_full.json') as jf:
      jd = json.load(jf)
  
  df = open(f'{i}_country_fr_full.csv', 'w', newline='')
  cw = csv.writer(df)
  
  c = 0
  for data in jd:
      if c == 0:
          header = data.keys()
          cw.writerow(header)
          c += 1
      cw.writerow(data.values())
  
  df.close()
