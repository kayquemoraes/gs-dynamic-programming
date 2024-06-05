# Projeto: Otimização da Distribuição de Sensores Subaquáticos para Monitoramento de Poluição Oceânica

## Descrição
Este projeto utiliza técnicas de programação dinâmica para otimizar a alocação de sensores subaquáticos e a coleta de dados sobre a poluição oceânica. O objetivo é identificar áreas críticas de poluição e priorizar ações de monitoramento e resposta.

## Arquivos
- `sensor_optimization.py`: Contém o código principal para calcular a distância entre pontos e encontrar a distribuição ótima dos sensores utilizando programação dinâmica.

## Como Executar
1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Execute o script `sensor_optimization.py`:

   ```bash
   python sensor_optimization.py
## Exemplo de Aplicação
Neste exemplo, temos um conjunto de pontos representando possíveis locais onde os sensores podem ser alocados. O objetivo é distribuir três sensores de maneira ótima para cobrir a maior área possível, minimizando as distâncias entre os pontos monitorados.

## Pontos Disponíveis
Os pontos onde os sensores podem ser alocados são:
- (0, 0)
- (1, 3)
- (4, 3)
- (6, 1)
- (3, 5)
- (5, 4)

## Número de Sensores
O número de sensores disponíveis é 3.

## Saída Esperada
A distribuição ótima dos sensores encontrada pelo script será:
   ```yaml
   Distribuição Ótima dos Sensores:
   (0, 0)
   (1, 3)
   (5, 4)
   ```
## Referência
- Ziviani, N. (2004). Projeto de Algoritmos: com Implementações em Pascal e C (3ª ed.). Thomson Learning.