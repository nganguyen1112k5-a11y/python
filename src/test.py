import array as arr
import copy
a = arr.array('i',[1,2,3,4,5])
b = arr.array('i',sorted(a,reverse= True))
print(a,b)


