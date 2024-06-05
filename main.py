import math


# Função para calcular a distância euclidiana entre dois pontos
def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos.

    :param ponto1: Uma tupla (x1, y1) representando o primeiro ponto.
    :param ponto2: Uma tupla (x2, y2) representando o segundo ponto.
    :return: A distância euclidiana entre ponto1 e ponto2.
    """
    return math.sqrt((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2)


# Função para encontrar a distribuição ótima dos sensores utilizando programação dinâmica
def encontrar_distribuicao_otima(sensores, pontos):
    """
    Encontra a distribuição ótima dos sensores nos pontos dados usando programação dinâmica.

    :param sensores: Número de sensores disponíveis.
    :param pontos: Lista de pontos (x, y) onde os sensores podem ser alocados.
    :return: Lista de pontos onde os sensores serão alocados para otimizar a cobertura.
    """
    n = len(pontos)
    # Inicializa a tabela dp com infinito (float('inf')), indicando distâncias inicialmente impossíveis
    dp = [[float('inf')] * (sensores + 1) for _ in range(n + 1)]
    # A distância de não colocar nenhum sensor em nenhum ponto é 0
    dp[0][0] = 0

    # Preenchendo a tabela dp
    for i in range(1, n + 1):  # Para cada ponto até o i-ésimo ponto
        for j in range(1, sensores + 1):  # Para cada quantidade de sensores até j
            for k in range(i):  # Verifica todos os pontos anteriores até o k-ésimo ponto
                # Calcula a distância entre o ponto atual (i-1) e o ponto anterior (k)
                distancia = calcular_distancia(pontos[i - 1], pontos[k])
                # Atualiza a tabela dp com a menor distância encontrada
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + distancia)

    resultado = []
    i, j = n, sensores
    # Reconstrói a solução a partir da tabela dp
    while i > 0 and j > 0:
        for k in range(i):  # Para cada ponto até o k-ésimo ponto
            # Se a distância atual na tabela dp é igual à distância do ponto anterior mais a distância calculada
            if dp[i][j] == dp[k][j - 1] + calcular_distancia(pontos[i - 1], pontos[k]):
                # Adiciona o ponto atual à solução
                resultado.append(pontos[i - 1])
                # Atualiza i e j para continuar a reconstrução da solução
                i = k
                j -= 1
                break  # Sai do loop interno para continuar a reconstrução

    # Retorna a solução na ordem correta
    return resultado[::-1]


# Exemplo de uso
if __name__ == "__main__":
    # Definindo os pontos onde os sensores podem ser alocados
    pontos = [(0, 0), (1, 3), (4, 3), (6, 1), (3, 5), (5, 4)]
    # Definindo o número de sensores disponíveis
    sensores = 3

    # Encontrando a distribuição ótima dos sensores
    distribuicao_otima = encontrar_distribuicao_otima(sensores, pontos)

    print("Distribuição Ótima dos Sensores:")
    for ponto in distribuicao_otima:
        print(ponto)
