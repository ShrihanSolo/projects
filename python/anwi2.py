"""count=0
no1=0 count+=1
no2=1 count+=1
no3=no1+no2 count+=1
no4=no2+no3 count+=1
no5=no3+no4 count+=1"""
count=0
no1=0
print(no1)
count+=1
no2=1
print(no2)
count+=1
while count != 100000000000000000001:
    nextno=no1+no2
    count+=1
    print(nextno)
    no1=no2
    no2=nextno


#0,1,1,2,3,5,8,13,21,34
