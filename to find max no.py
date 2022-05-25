dct={'a':30,'b':18,'c':12,'d':50}
print(dct)
max=dct['b']
min=dct['d']

for i in dct:
    if(dct[i]>max):

       print("max no=",dct[i])
for i in dct:
    if(dct[i]<min):
        print("min no=",dct[i])


