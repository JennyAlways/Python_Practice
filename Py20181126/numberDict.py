#key is the number, value is the square root
import math
b=0
numberDict = {}
for a in range(11):
    b=a+10
    numberDict[b]=math.sqrt(b)

print numberDict
