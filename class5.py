'''
File IO (input/ouput)
1. w -> write
2. r -> read
3. a -> append
'''
#%%
fileName = "class5.txt"

fout = open(fileName, 'w')
for i in range(10):
    text = f"Write number {i} into {fileName}\n"
    fout.write(text)
fout.close()


fin = open(fileName, 'r')
lines = fin.readlines()
fin.close()
for line in lines:
    print(line)

# %%
'''
Assignment

Please write a function 
which take four input parameters
to write the triangle into file with conditions.
Function declaration:

def print_triangle(N, plus, minus, fileName):
    expressions

For example,

function call:
print_triangle(5, 3, 2, "my_triangle.txt") 

Output (in "my_triangle.txt"):
    *
   - -
  + + +
 * * * *
* * * * *
'''