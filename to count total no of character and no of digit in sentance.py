sent=input('enter a sentence:')
letter=0
digit=0
i=1
for i in range(1, len(sent)):
        if(65<=i>=122 and i>=65):
            letter+=1
            print( 'no of letter=',letter)
               
        else:
                digit=digit+1
                print("no of digit=",digit)

               
