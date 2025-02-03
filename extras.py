"""
Desafio Extra (Opcional) - Desenvolvimento de Algoritmos

1. Função de Algoritmo:
-Escreva uma função que receba uma lista de inteiros (representando valores de
transações diárias) e retorne a maior soma de um subarray contínuo (subconjunto de
transações).

2. Otimização:
-Otimize a função para garantir que ela execute com a melhor complexidade temporal
possível.

3. Testes Unitários:
-Escreva testes unitários para validar a função com diferentes casos de teste,
incluindo casos de borda e entradas grandes.
"""

def max_sum(int_list:list) -> int:
    # checar se existe a lista
    if not int_list:
        return 0

    max_global = int_list[0]
    max_local = int_list[0]

    for num in int_list[1:]:
        # atualiza a contagem local do maior subarray
        max_local = max(num,max_local + num)

        # substitui o max global se encontrar um subarray local maior
        if max_local > max_global:
            max_global = max_local

    return max_global
