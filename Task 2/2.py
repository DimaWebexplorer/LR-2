import numpy as np
import os

#variant = 39

matrix = np.load('matrix_39_2.npy')

size = len(matrix)

x = list()
y = list()
z = list()

limit = 539

for i in range(0, size):
    for j in range(0, size):
        if matrix[i][j] > limit:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez(file = 'points', x = x, y = y, z = z)
np.savez_compressed('points_zip', x = x, y = y, z = z)

print(f"points     = {os.path.getsize('points.npz')}")
print(f"points_zip = {os.path.getsize('points_zip.npz')}")
