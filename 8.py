print("Введите число:")
c = int(input())
print("Введите систему счисления:")
s = int(input())
l=''

if s==2:
    while c > 0:
        l = str(c % 2) + l
        c = c // 2
    print ("Вывод")    
    print(l)
else:
    if s==8:
        while c > 0:
            l = str(c % 8) + l
            c = c // 8
        print("Вывод")  
        print(l)
    else:
        print("Ошибка")



