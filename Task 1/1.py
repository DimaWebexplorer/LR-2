import numpy as np
import json

#variant = 39

matrix = np.load('matrix_39.npy')

size = len(matrix)

matrixStat = dict()
matrixStat['sum'] = 0
matrixStat['avr'] = 0
matrixStat['sumMD'] = 0
matrixStat['avrMD'] = 0
matrixStat['sumSD'] = 0
matrixStat['avrSD'] = 0
matrixStat['max'] = matrix[0][0]
matrixStat['min'] = matrix[0][0]

for i in range(0, size):
    for j in range(0, size):
        matrixStat['sum'] += matrix[i][j]
        if i == j:
            matrixStat['sumMD'] += matrix[i][j]
        if i + j == size:
            matrixStat['sumSD'] += matrix[i][j]
        matrixStat['max'] = max(matrixStat['max'], matrix[i][j])
        matrixStat['min'] = min(matrixStat['min'], matrix[i][j])

matrixStat['avr'] = matrixStat['sum'] / (size * size)
matrixStat['avrMD'] = matrixStat['sumMD'] / size
matrixStat['avrSD'] = matrixStat['sumSD'] / size

for key in matrixStat.keys():
    matrixStat[key] = float(matrixStat[key])

with open('matrixStat.json', 'w') as result:
    result.write(json.dumps(matrixStat))

normalMatrix = np.ndarray(shape = (size, size), dtype = float)

for i in range(0, size):
    for j in range(0, size):
        normalMatrix[i][j] = matrix[i][j] / matrixStat['sum']

np.save('normalMatrix', normalMatrix)

