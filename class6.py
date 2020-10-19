'''
* tuple (tuple)
* list (list)
* dict (dictionary)
'''
#%%

tupleVar = (1,3,5,6)
print("Tuple case:")
print(f"Type of tup is {type(tupleVar)}")
print(f"Values of tup are {tupleVar}")
print()

print("for loop + tuple:")
for t in tupleVar:
    print(t, end=" ")
print('\n')

listVar = [1,2,5,7]
print("List case:")
print(f"Type of tup is {type(listVar)}")
print(f"Values of tup are {listVar}")
print()

print("for loop + list + enumerate:")
for index, l in enumerate(listVar):
    print(f"listVar[{index}] = {l}")
print()

dictVar = {'name':'Peter','Gender':'Man','Height':170,'Weight':60}
print("Dictionary case:")
print(f"Type of tup is {type(dictVar)}")
print(f"Values of tup are {dictVar}")
print()

print("for loop + dict:")
for key, value in dictVar.items():
    print(f"dictVar['{key}'] = {value}")
print()
# %%
