i=int(input("enter the number:"));
sum=0
origin=i
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("sum of cube of digit=",sum)
if (origin==sum ):
    print("i is armstrong number");
else:
    print("i is not armstrong number");
