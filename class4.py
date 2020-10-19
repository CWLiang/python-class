'''
function

def function_name(parameters):
    expressions ...
'''
#%%

def func1():
    print('This is func1')
    a = 1+2
    print(a)

def func2(a, b):
    c = a+b
    print(f'{a} + {b} = {c}')

def func3(a, b=2):
    c = a+b
    print(f'{a} + {b} = {c}')

def func4(name, *grades):
    total_grade = 0
    print(f"The type of grades is {type(grades)}")
    print(f"The value of grades is {grades}")
    for index, grade in enumerate(grades):
        print(f"Grade {index}. {grade}")
        total_grade += grade
    print(f'Total grade of {name} is {total_grade}')

def func5(name, **kw):
    total_grade = 0
    print(f"The type of kw is {type(kw)}")
    print(f"The value of kw is {kw}")
    for subject, grade in kw.items():
        print(f"{subject}: {grade}")
        total_grade += grade
    print(f'Total grade of {name} is {total_grade}')

print('case1')
func1()
print()

print('case2')
func2(3,5)
print()

print('case3')
func3(8)
print()

print('case4')
func4('Sam',100,98,95,100)
print()

print('case5')
func5('Amy',math=100,chinese=98,science=95,english=100)
print()

#%%

'''
Assignment

Please write a function 
which take three input parameters
to print the triangle with conditions.
Function declaration:

def print_triangle(N, plus, minus):
    expressions

For example,

function call:
print_triangle(5, 3, 2) 

Output:
    *
   - -
  + + +
 * * * *
* * * * *
'''

