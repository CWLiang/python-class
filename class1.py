'''
Basic function:
* print
* type
* len

Data type:
* int (integer)
* float (float)
* str (string)
* bool (True or False)

Operation:
* = (assign)
* +,-,*,/
* +=,-=,*=,/=
* ** (次方), % (取餘數)
* >, <, >=, <=, ==
'''

intVar = 5
floatVar = 5.0
strVar = "5" # or '5'

print("The type of intVar is",type(intVar))
print("The type of floatVar is",type(floatVar))
print("The type of strVar is",type(strVar))

print("Convert intVar to float:",float(intVar))
print("Convert floatVar to string:",str(floatVar))
print("Convert strVar to int:",int(strVar))

print("intVar == intVar ? ",intVar==intVar)
print("intVar == floatVar ? ",intVar==floatVar)
print("inVar == strVar ? ",intVar==strVar)