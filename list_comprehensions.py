import random
#list comprehensions
a = [x**2 for x in range(10)]
print(a)
b = [random.randint(0,100) for x in range(10)]
print(b)
c = [1,2,3,4,5,6,7,8,9]
d = []
for x in c:
	if x%2==0:
		d.append(x**2)
print(c)
print(d)
e = [x**2 for x in c if x%2==0]
print(e)

f=[random.randint(-10,10) for x in range(10)]
print(f)
g=[0 if x<0 else x**2 for x in f]
print(g)
h = list(range(0,20,3))
print(h)