a=[]
size=int(input("enter no of element:"))
for i in range(size):
    val=int(input("enter the number:"))
    a.append(val)
count=0
sum=0
for i in range(size):
    if(a[i]%2==0):
        count=count+1
        sum=sum+a[i]
print("no of even no=",count)        

print("sum of even no=",sum)
