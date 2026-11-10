arr=[10,20,45,23,56,76,98,192]
largest=0
secondLargest=0

for i,j in arr:
    if i>secondLargest:
        secondLargest=i
        
        if j>largest:
            largest=j
            
print(secondLargest)