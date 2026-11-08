arr = [10,12,23,45,67,76,88,98,176,198,244]
item = 88
flag=False
arrIndex = 0

for i in arr:
    if(i==item):
        flag=True
        arrIndex=arr.index(i)
        
if flag:
    print("Item Found at ",arrIndex+1)
else:
    print("Item not found.")