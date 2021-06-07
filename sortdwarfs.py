import csv
import pandas as pd
data=[]
df = pd.read_csv("brown_dwarfs.csv")
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
df.to_csv("brown_dwarfs2.csv")
with open("brown_dwarfs2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[1:]
newdata=[]
for data_point in planet_data:
   if(data_point[3]==''):
       planet_data.remove(data_point)
   data_point[3]= float(data_point[3])*0.000954588
   data_point[4]= float(data_point[4])*0.102763
with open("brown_dwarfs_sorted.csv", "a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)