import random
import math
def PowerA3(A):
    return A*A*A
A= random.randrange(-10,10)
B= PowerA3(A)
print('A=', A, 'B=', B)
print('')
def Sign(X):
    if X < 0:
        return -1
    elif X > 0:
        return 1
    return 0

C = random.randrange(-10,10)
D = random.randrange(-10,10)
print('A = ', C)
print('B = ', D)
s_C = Sign(C)
s_D = Sign(D)
print('Sign(A) = ', s_C)
print('Sign(B) = ', s_D)
print('Sign(A) + Sign(B) = ', s_C+s_D)
print('')
def RingS(R1,R2):
    return math.pi * (R1**2 - R2**2)

def CircleS(R):
    return math.pi * R**2

for i in range(0,3):
    print(i)
    L = sorted(random.sample(range(1, 10), 2), reverse=True)
    print(L)
    print("R_1 = {0}; R_2 = {1}".format(L[0], L[1]))
    print("Площадь круга 1: ", CircleS(L[0]))
    print("Площадь круга 2: ", CircleS(L[1]))
    print("Площадь кольца: ", RingS(L[0], L[1]))
print('')
def chetv(z,y):
    if((z>0)and(y>0)):
        res="первая четврть"
        print(res)
    if((z<0)and(y>0)):
        res = "вторая четврть"
        print(res)
    if((z<0)and(y<=0)):
        res = "третья четврть"
        print(res)
    if((z>0)and(y<0)):
        res = "четвертая четврть"
        print(res)
    return res
 
if __name__ == '__main__':
    z=float(input())
    y= float(input())
    for i in range(3):
        chetv(z=random.randint(-10,10), y=random.randint(-10,10))
print('')
def Fact2(N):
   if N <= 2:
      return N
   else:
      return N * Fact2(N-2)

W = [random.randrange(1,10) for w in range(5)]
for t in range(5):
   print("{0}!! = {1}".format(W[t],Fact2(W[t])))

print(6,"!! = ", Fact2(6))
print(7,"!! = ", Fact2(7))
