print('Введите переменную А')
A=int(input())
print('Введите переменную В')
B=int(input())
if A!=B:
    if A>B:
        B=A
    else:
        A=B
else:
    A=B=0
print(A,B)
print('')
print('Введите переменную A')
x=int(input())
print('Введите переменную В')
y=int(input())
print('Введите переменную C')
z=int(input())
if x<y:
    m=x
else:
    m=y
if z<m:
    m=z
s=x+y+z-m
print(s)
print('')
print('Введите переменную A')
i=float(input())
print('Введите переменную B')
j=float(input())
print('Введите переменную C')
k=float(input())
ij=abs(i-j)
ik=abs(i-k)
if ij < ik:
    print('Точка В ближе к А. Расстояние равно %.2f' % ij)
if ik < ij:
    print('Точка C ближе к А. Расстояние равно %.2f' % ik)
if ij == ik:
    print('Точки B и С равноудалены от точки A')
print('')
print('Введите х')
xс = float(input())
print('введите у')
yс = float(input())
if xс > 0 and yс > 0:
    print("Точка находится в I четверти")
elif xс < 0 and yс > 0:
    print("Точка находится в II четверти")
elif xс < 0 and yс < 0:
    print("Точка находится в III четверти")
elif xс > 0 and yс < 0:
    print("Точка находится в IV четверти")
print('')
print('введите число')
q=int(input())
if q>0:
    if q%2==0:
        print('положительное чётное')
    else:
        print('положительное нечётное')
elif q==0:
    print('нулевое')
else:
    if q%2==0:
        print('отрицательное чётное')
    else:
        print('отрицательное нечётное')
print('')
print('')
w=int(input())
if w>=1 and w<10:
    if w%2==0:
        print('однозначное, чётное')
    else:
        print('однозначное, нечётное')
if (w>=10 and w<=99):
    if w%2==0:
        print('двузначное,чётное')
    else:
        print('двузначное нечётное')
if w>=100 and w<1000:
    if w%2==0:
        print('трёхзначное чётное')
    else:
        print('трёхзначное нечётное')
