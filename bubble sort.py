numbers=[9,5,4,3,4,1,6,2,8,7]
n=len(numbers)
for i in range (n-1):
    for j in range(n-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print("sloted list",numbers)            
