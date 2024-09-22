import numpy as np

def calculate(list):
    try:
        matriz = np.array(list).reshape(3,3)
        mediaEixo1 = np.mean(matriz, axis=0)
        mediaEixo2 = np.mean(matriz, axis=1)
        mediaLista = np.mean(list)
        varianciaEixo1 = np.var(matriz, axis=0)
        varianciaEixo2 = np.var(matriz, axis=1)
        varianciaLista = np.var(list)
        desvioPadrao1 = np.std(matriz, axis=0)
        desvioPadrao2 = np.std(matriz, axis=1)
        desvioPadraoLista = np.std(list)
        maxEixo1 = np.max(matriz, axis=0)
        maxEixo2 = np.max(matriz, axis=1)
        maxLista = np.max(list)
        minEixo1 = np.min(matriz, axis=0)
        minEixo2 = np.min(matriz, axis=1)
        minLista = np.min(list)
        sumEixo1 = np.sum(matriz, axis=0)
        sumEixo2 = np.sum(matriz, axis=1)
        sumLista = np.sum(list)
        calculations = {
            'mean': [mediaEixo1, mediaEixo2, mediaLista],
            'variance': [varianciaEixo1, varianciaEixo2, varianciaLista],
            'standard deviation': [desvioPadrao1, desvioPadrao2, desvioPadraoLista],
            'max': [maxEixo1, maxEixo2, maxLista],
            'min': [minEixo1, minEixo2, minLista],
            'sum': [sumEixo1, sumEixo2, sumLista]
        }
        return calculations
    except ValueError as ve:
        raise ValueError("List must contain nine numbers.")
print(calculate([1,2,3,4,5,6,7,8,9]))