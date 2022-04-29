a=int(input(""))
b=int(input(""))
c=int(input(""))
d=a*b*c
e=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def fun(a):
    if a=='0':
        e[0]+=1
        
    elif a=='1':
        e[1]+=1
        
    elif a=='2':
        e[2]+=1
        
    elif a=='3':
        e[3]+=1
        
    elif a=='4':
        e[4]+=1
        
    elif a=='5':
        e[5]+=1
        
    elif a=='6':
        e[6]+=1
        
    elif a=='7':
        e[7]+=1
        
    elif a=='8':
        e[8]+=1
        
    elif a=='9':
        e[9]+=1



        
list=str(d)

for i in range(len(list)):
    fun(list[i])

for i in range(0,10):
    print(e[i])
