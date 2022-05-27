def vote(a):
  if a>=18:
       return a


x=int(input("enter the age:"))
z=vote(x)
if x>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
