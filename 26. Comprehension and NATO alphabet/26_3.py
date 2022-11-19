import pandas
with open ("file1.txt") as file1:
    data1 = file1.readlines()
with open ("file2.txt") as file2:
    data2 = file2.readlines()  

result=[int(n) for n in data1 if n in data2]
print(result)