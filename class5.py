
'''
1. w -> write
2. r -> read
3. a -> append
'''

fileName = "example.txt"
'''
fout = open(fileName, 'w')
for i in range(10):
    text = f"No.{i} Example to write the {fileName}\n"
    #text = "Example to write the " + fileName
    fout.write(text)
fout.close()
'''

fin = open(fileName, 'r')
lines = fin.readlines()
fin.close()
for line in lines:
    print(line)
