"""
Desafio 2 - Manipulação de Dados
Parte 1
Utilize os seguintes dados para criar um DataFrame com a biblioteca Pandas:
{
"Nomes": ["Ana", "Bruno", "Carlos", "Daniela"],
"Idades": [22, 23, 21, 22],
"Notas": [88, 92, 95, 85]
}
Calcule a média das notas.
Adicione uma nova coluna chamada "Status", que indicará "Aprovado" para notas iguais ou
superiores a 90, e "Reprovado" para notas inferiores.
Por fim print o resultado da média e o Dataframe com a coluna Status.
"""

import pandas as pd

data = {
    "Nomes": ["Ana", "Bruno", "Carlos", "Daniela"],
    "Idades": [22, 23, 21, 22],
    "Notas": [88, 92, 95, 85]
}

# criar dataframe
df = pd.DataFrame(data)

# calcular a média das notas
media_notas = df["Notas"].mean()
print(f"Média das notas: {media_notas}")

# criar uma nova coluna Status
status_list = []
for nota in df["Notas"]:
    if nota >= 90:
        status_list.append("Aprovado")
    else:
        status_list.append("Reprovado")

# adicionar nova coluna ao dataframe
df["Status"] = status_list

print(df)