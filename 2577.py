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

#ASCII 코드를 이용해서 e 인덱스 접근
# (number -> ASCII code)
# 0 -> 48 | 1 -> 49 | 2 -> 50
# 3 -> 51 | 4 -> 52 | 5 -> 53
# 6 -> 54 | 7 -> 55 | 8 -> 56 | 9 -> 57 
# ASCII code를 어떻게 활용하는가
#만약 함수에 들어온 값이 2이면,
#2의 아스키코드는 50이므로, 0의 아스키코드인 48로 빼면 처음에 들어온 2로 나옴
#def fun(a):
#    ascii_value = ord(a); #아스키코드로 변환
#    increasValue = ascii_value - 48 #증가하는 값을 찾는 과정
#    e[increasValue]+=1 #해당 인덱스의 e 값 +1

list=str(d)

for i in range(len(list)):
    fun(list[i])

for i in range(0,10):
    print(e[i])
