print('Введите угол a, 0<a<360')
a= float(input())
r= abs(3.14*a/180)
print(r)

print('Введите угол a, 0<a<2*П')
a= float(input())
g= abs(180/3.14*a)
print(g)

print('Введите вес конфет, кг')
x= int(input())
print('Введите стоимость этих конфет')
a= float(input())
kg= a/x
print('Введите другой вес конфет, чтобы узнать их стоимость')
y= int(input())
ctoim= y*kg
print('стоимость 1 кг конфет', kg)
print('стоимость' ,y ,'кг конфет', ctoim)

print('Введите скорость первого автомобиля')
vo= float(input())
print('Введите скорость второго автомобиля')
vt= float(input())
print('введите начальное расстояние между ними')
s= float(input())
print('введите время, которое прошло после того, как они стартанули')
t= float(input())
st= (s+(vo+vt)*t)
print('расстояние, которое пройдут два автомобиля через',t,'ч' , st)

print('введите коэффициент А, который не равен 0')
a= float(input())
print('введите коэффициент В')
b= float(input())
x= b/a
print('x', x)




print('Введите А1')
A1= float(input())
print('Введите В1')
B1= float(input())
print('введите С1')
C1= float(input())
print('Введите А2')
A2= float(input())
print('Введите В2')
B2= float(input())
print('Введите С2')
C2= float(input())

a= A1*B2 - A2*B1
x= (C1*B2 - C2*B1)/a
y= (A1*C2 - A2*C1)/a

print('x=', x)
print('y=', y)
