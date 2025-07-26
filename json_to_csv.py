import json
import csv
i = 0
while i < 86:
  i += 1
  print(i)
  with open(f'{i}_country_fr_full.json') as jf:
      jd = json.load(jf)
  Ed = d['wines']
  df = open(f'{i}_country_fr_full.csv', 'w', newline='')
  cw = csv.writer(df)

  c = 0
  for emp in Ed:
      if c == 0:
          # Writing headers of CSV file
          h = emp.keys()
          cw.writerow(h)
          c += 1
      # Writing data of CSV file
      cw.writerow(emp.values())
  df.close()


