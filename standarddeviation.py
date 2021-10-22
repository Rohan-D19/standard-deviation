import math

import csv
with open('data.csv', newline='') as f:
  reader = csv.reader(f)
  file_data= list(reader)
  
data = file_data[0]

def mean(data):
  n = len(data)
  total = 0
  for x in data:
    total = +=int(x)
   
  mean = total/n
  return mean


  squared_list = [0]
  for number in data:
    a = int(number)-mean(data)
    a= a**2
    
  sum = 0
  for sum in i:
    sum = sum + 1
    
  result = sum / (len(data)-1)
  
  standard_deviation = math.sqrt(result)
  print(standard_deviation)
