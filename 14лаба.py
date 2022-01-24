print('Введите А')
A= int(input())
print('Ведите В')
B= int(input())
while (A-B)>= 0:
    print('без наложений')
    A-=B
print('Длина незанятой части= ', A)
print('')
n= int(input())
kq=0
print('1')
for i in range(1,1000000000):
    kq+=i
    if n<=kq:
        break
print('Ответ:', kq)
print('')
import random
Ss = 1000
Se = 1100
P = random.randrange(10,260)/10
print('P = ', P)
co = 1 + P/100
print("".format(Ss,P,co))
K = 0
S = Ss
while S < Se:
    S *= co
    K += 1
    print("K = {0}, S = {1}".format(K,S))
print()
print("Months = {0}, Final = {1}".format(K,S))
print('')
q=int(input())
w=int(input())
def gcd(q, w):
    while q != w:
        if q > w:
            q = q - w
        else:
            w = q - w        
print(q+w)
