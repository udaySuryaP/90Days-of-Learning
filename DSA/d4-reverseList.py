lst=[10,20,45,23,56,76,98,192]
newLst=[]

for element in range((len(lst)-1),-1,-1):
    newLst.append(lst[element])

print(newLst)

