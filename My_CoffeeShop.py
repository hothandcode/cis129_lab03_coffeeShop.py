print('\033[1m*****Welcomoe to My Coffee Shop!!!*****\033[0m]')
a = int(input('Number of Coffees bought?'))
b = int(input('Number of muffins bought'))
c = 5
d = 4
g = 2
h = 3
e = int(input('Number of hot cocoas bought'))
f = int(input('Number of cheese danishes bought'))
ac = a * c
bd = b * d
eg = e * g
fh = f * h
tax = (ac + bd + eg + fh) * .06
total = ac + bd + eg + fh + tax
print('***************\nMy Coffee and Muffin Shop\nNumber\
 of coffees bought?')
print(a)
print('Number of muffins bought?')
print(b)
print('Number of hot cocoas bought?')
print(e)
print('Number of cheese danishes bought?')
print(f)
print('***************\n\n***************')
print('My Coffee and Muffin Shop Receipt')
print((a), 'Coffee(s) at $5 each: $', ac)
print((b), 'Muffins(s) at $4 each: $', bd)
print((e), 'Hot Cocoa(s) at $2 each: $', eg)
print((f), 'Cheese Danish(s) at $3 each: $', fh)
print('6% tax: $', tax)
print('------------------')
print('Total: $', total)