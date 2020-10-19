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
