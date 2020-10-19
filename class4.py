

# def -> define 定義
def print_function(input):
    print(input)
    output = input * 2
    return output

def report(name, *grades):
    total_grade = 0
    print(type(grades),grades)
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)

def portrait(name, **kw):
    print('name is', name)
    print(type(kw),kw)
    for k,v in kw.items():
        print(k, v)

#report("Mike",1,2,3,4,5)

#portrait('Mike', age=24, country='China', education='bachelor')



#name = input("What's your name: ")
#print(name)

'''
N = 5
plus = 3
minus = 2
    *
   - -
  + + +
 * * * *
* * * * *
def print_triangle(N, plus, minus):
'''
'''
i = 0
while True:
    i += 1
    if i == 3: 
        continue
    if i >= 5:
        break
    print(i)
'''

'''
1. read -> 'r'
2. write -> 'w'
3. append -> 'a'
'''
fileName = "example.txt"
fout = open(fileName, 'w')
for i in range(5):
    text = f"No.{i} Example to write the {fileName}\n"
    #text = "Example to write the " + fileName
    fout.write(text)
fout.close()