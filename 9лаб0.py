print('Ведите кол-во секунд')
N= int(input())
s= N%60
print(s)
print('')
print('Введиете день(1-365)')
K= int(input())
no= K%7
print(no)
print('')
print('Введите N(1-7)')
N3= int(input())
print('Введите К(1-365)')
K3= int(input())
d= ((K3+N3-2)%7)+1
print(d)
print('')
print('Введите А')
A= int(input())
print('Введите В')
B= int(input())
print('Введите С')
C= int(input())
ko= (A//C)*(B//C)
S= (A*B)-((ko*C)*C)
print('Кол-во=', ko)
print('Площадь=', s)
print('')
print('Ведите номер года')
ng= int(input())
ns= ((ng-1)//100)+1
print('Номер столетия=', ns)
