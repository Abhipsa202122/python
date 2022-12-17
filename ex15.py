'''var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)
x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)'''
x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)
x = 100
y = 50
print(x and y)
a = 4
b = 11
print(a | b)
print(a >> 2)
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
print('[%c]' % 65)
print('%d %d %.2f' % (11, '22', 11.22))


    


