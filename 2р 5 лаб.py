A = int(input())
B = int(input())
C = int(input())
r1=(A-C)
r2=(B-C)
if r1<0:
    r1*=(-1)
if r2<0:
    r2*=(-1)
r3=(r1+r2)
print("Расстояние между АС =", r1)
print("Расстояние между ВС =", r2)
print("Их сумма =", r3)
