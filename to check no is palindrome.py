i=int(input("enter anumber:"))
rev=0
origin=i
while(i>0):
     rev=rev*10+i%10
     i=i//10
print("reverse=",rev)
if(origin==rev):
    print("no is palindrome")
else:
    print("no is not palindrome")
