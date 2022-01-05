import csv 
with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
new_data = []
for i in range(len(fileData)):
    n = fileData[i][1]
    new_data.append(float(n))

num = len(new_data)
total=0
for y in new_data:
    total+=y
mean = total/num
print (mean)
