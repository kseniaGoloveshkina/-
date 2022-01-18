import random
pr= round(random.uniform(0, 100),2)
print('Цена 1кг: ', pr)
for i in range(1,11):
    a= 0.1*i
    print('Итоговая цена {0:.1f} кг: {1:.2f}'.format(a, a*pr))
print('')
print('Введите N>0')
n= int(input())
pro= 1.0
for q in range(1, n+1):
    k= 1+q*0.1
    pro*=k
    print(q, ' : ',k,' : ',pro)
print('Производная= ',pro)
print('')
print('Введите N>0')
ni= int(input())
s= 0.0
for w in range(1, ni+1):
    x= 2*w-1
    s+=x
    print(w,' : ', x , ' : ', s)
print('Сумма= ', s)
print('')
nw= random.randrange(1,10)
print('N=', nw)
aw= random.randrange(-10,10)
print('A =', aw)
pw=1.0
sw=1.0
for iw in range(1, nw+1):
    pw*=aw
    sw+=pw
    print(iw, ' : ', pw, ' : ', sw)
print('Ответ =', sw)
print('')
ne= random.randrange(1,10)
print('N=', ne)
ae= random.randrange(-10,10)
print('A =', ae)
pe=1.0
se=1.0
for ie in range(1, ne+1):
    se= se*ae*(-1)
    pe+= se
    print(ie , ' : ', pe , ' : ', se)
print('Ответ =', se)
