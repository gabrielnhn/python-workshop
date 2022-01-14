a = [1,2,3]
b = a
print(b)

b.append(4)
print(b)

print(4 in a)
print(a)

print(a is b)
print(id(a) == id(b))
