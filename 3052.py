list=[1,2,3,4,5,6,7,8,9,10]


for i in range(0,10):
    b=int(input(""))
    b=b%42
    list[i]=b

a=set(list)
print(len(a))
