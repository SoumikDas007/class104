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
new_data.sort()
 
if num %2==0:
    median1 = float(new_data[num//2])
    median2 = float(new_data[num//2-1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]
    print(num)
print(median)


