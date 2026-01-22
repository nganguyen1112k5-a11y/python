
a=[2]
print(id(a))
a.append(3)
print(id(a))

b = a
print(id(a) == id(b))
b.append(5)
print(a,b)