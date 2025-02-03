"""
Desafio 3 - Manipulação de arquivo XLSX
Carregue o arquivo Excel vendas_ecommerce.xlsx em um DataFrame
Calcule o total de vendas por categoria de produto.
Crie na planilha enviada uma nova aba chamada “Total Vendas por Categoria”. Dentro dessa
aba, adicione a relação de categorias e valor total por categoria.
"""
import pandas as pd

# carregar o arquivo
path_excel = "vendas_ecommerce.xlsx"
df = pd.read_excel(path_excel)

# valor total
df["Valor Total"] = df["Quantidade Vendida"] * df ["Preço Unitário"]

# calcular valor de vendas por categoria
total_per_category = df.groupby("Categoria do Produto")["Valor Total"].sum().reset_index()
total_per_category.columns = ["Categoria do Produto", "Valor Total"]

print(f"Total de vendas por categoria: \n{total_per_category}")

# salvar nova aba ao arquivo já existente
with pd.ExcelWriter(path_excel, mode="a", engine="openpyxl") as writer:
    total_per_category.to_excel(writer, sheet_name="Total Vendas por Categoria", index=False)

print(f"Total de vendas por categoria adicionada ao arquivo {path_excel}")