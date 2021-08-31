import numpy as np

a = np.array([range(i, i + 3) for i in [1, 4, 7]])
#a = np.full((3, 3), '_')
print(a)
n = a.shape[0]
print(n)
for i in range(n):
    print(a[i])
    print(a[:, i])

for i in range(n):
    print(a[i,i])

for i in range(0, n):
    print(a[i, n - 1 - i])

print('_' in set(a[1]))
print(a.diagonal())
print(len(set(np.fliplr(a).diagonal())))
