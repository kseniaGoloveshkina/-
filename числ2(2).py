import math
 
def fun(x):
    return (2*x+math.cos(x)-0.5)
 
x1=float(input("Введите приближенное значение Х="))
e=float(input("Введите точность e="))
a=float(input("a="))
b=float(input("b="))
a=abs((fun(a+0.0001)-fun(a))/0.0001)
b=abs((fun(b+0.0001)-fun(b))/0.0001)
q=max(a,b)
q=(1-q)/q 
iters=0
x0=x1
x1=fun(x0)
while abs(x1-x0) <= abs(q*e):
    iters+=1
    x0=x1
    x1=fun(x0)

print('Вычисленное значение корня:',x1)
print('Число итераций:',iters)
