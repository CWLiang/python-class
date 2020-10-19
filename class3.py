'''
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
'''
#%%
print('case1')
x = 1
y = 2
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal to y')
print()

print('case2')
x = 1
y = 1
if x > y:
    print('x is greater than y')
elif x < y:
    print('x is less than y')
else:
    print('x is equal to y')
print()

print('case3')
N = 7
if N < 7:
    print("N<7")
elif N == 7:
    print("N=7")
elif N >= 7:
    print('N>=7')
print()

print('case4')
N = 7
if N < 7:
    print("N<7")
if N == 7:
    print("N=7")
if N >= 7:
    print("N>=7")
print()

print("inline if else")
x = 1
y = 2
z = x if x > y else y
print(z)


# %%
