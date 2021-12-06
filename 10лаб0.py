print('Ведите А')
A=int(input())
print('Введите В')
B=int(input())
print('Введите С')
C=int(input())
if A>2 and B <=3:
    print('True')
else:
    print('False')
    
print('')
if A <B < C:
    print('True')
else:
    print('False')

print('введите любое число')
a=int(input())
if (a%2==0)and (a>=10 and a<=99):
    print('двузначное, чётное')
elif ((a%2!=0)and (a>=10 and a<=99)):
    print('двузначное,нечётное')
else:
    print('False')
print('')
print('Введите трёхзначное число')
x=int(input())
if ((x//100-(x//10)%10)*((x//10)%10 -x%10) >= 0) and (x//100 != x%10):
    print('True')
else:
    print('False')
print('')
print('Введите любое четырехзначное число')
p=int(input())
s=str(p)
if s==s[::-1] and 10000>p>999:
    print('True')
else:
    print('False')
print('')
import math
print('Введите сторону треугольника')
ap=int(input())
