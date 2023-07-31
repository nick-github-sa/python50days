import csv
import re

with open("python.csv", 'r') as file:
  test = []
  test1 = []
  csvreader = csv.reader(file, delimiter=',')
  for row in csvreader:
    test.append(row)

for words in test:
  for inner_words in words:
    test1.append(inner_words)

a = ' '.join(test1)

b = re.findall(r'\d+', a)
c = ', '.join(b)
print(c)