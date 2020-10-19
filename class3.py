N = 5
for i in range(N):
    print('i=', i)
    for j in range(i):
        print('j=', j, end=" ")
    print()

dic = {'a':'apple','b':'banana','c':'cat'}

for key in dic:
    print(key, dic[key])

l = list()
l = []
for i in range(1,6,2):
    l.append(i)
print(l)

l = [1,1,2,3,4,5,6,6,6]
s = set(l)
print(s)

N = 7
print(N==7)
print('case1')
if N < 7:
    print("N<7")
elif N == 7:
    print("N=7")
elif N >= 7:
    print('N>-8')

print('case2')
if N < 7:
    print("N<7")
if N == 7:
    print("N=7")
if N >= 7:
    print("N>7")


x = 1
y = 2

z = x if x > y else y
print(z)

l = ['a','b','c','d']
for index, value in enumerate(l):
    print(index, value)
print("length of l = ",len(l))
for i in range(len(l)):
    print(l[i])

