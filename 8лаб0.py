print('введите размер файла в битах')
ba= int(input())
ki = ba//1024
print('полных килобайт=', ki)
print('')

print('Ведите A')
A= int(input())
print('Введите B')
B= int(input())
k=0
while A>B:
    A-=B
    k+=1
m= A%B
print('кол-во отрезков В', k)
print('длинна незанятой части', m)
print('')
print('Введите 2-значное число')
a= input()
print(a[::-1])
print('')
print('Ведите 3-значное число')
a= input()
print(a[1:3]+a[0:1])
