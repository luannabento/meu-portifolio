import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Utilizar gráficos no python
sns.set(style=("whitegrid"))

#dados
np.random.seed(42)

df = pd.DataFrame({
    "data": pd.date_range(start="2025-01-01", periods=300),
    "produto": np.random.choice(["Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar"], 300),
    "regiao": np.random.choice(["Norte", "Sul", "Sudeste", "Nordeste"], 300),
    "cliente": np.random.choice(["Cliente A", "Cliente B", "Cliente C", "Cliente D"], 300),
    "quantidade": np.random.randint(1, 20, 300),
    "preco": np.round(np.random.uniform(5, 30), 2)
})

df["valor total"] = df["quantidade"] * df["preco"]
print(df)

#Limpeza e tratamento - ETL
#Criar colunas - mes e ano
df["mes"] = df["data"].dt.month
df["ano"] = df["data"].dt.year

#Categorizar ticket
df["categoria ticket"] = df["valor total"].apply(
    lambda x:
    "alto" if x > 200 else "médio" if x > 100 else "baixo"
)

#Faturamento por produto
fat_produto = df.groupby("produto")["valor total"].sum().reset_index()

#Faturamento por mês
fat_mes = df.groupby("mes")["valor total"].sum().reset_index()

#Faturamento por região
fat_regiao = df.groupby("regiao")["valor total"].sum().reset_index()
#fat_regiao.to_excel("Faturamento_regiao.xlsx", index=False)

#Faturamento por cliente
fat_cliente = df.groupby("cliente")["valor total"].sum().reset_index()

#Ticket médio
fat_ticket_medio = df.groupby("produto")["valor total"].mean().reset_index()

#Exportar planilha de dados para o Excel
#df.to_excel("Base_de_Vendas.xlsx", index=False)

#Gráfico Faturamento x Produto
plt.figure()
sns.barplot(data=fat_produto, x = "produto", y = "valor total")

#Configuração do gráfico
plt.title("Faturamento x Produto")
plt.xlabel("Produto")
plt.ylabel("Valor total")
plt.xticks(rotation=45)
plt.show()

#Gráfico Faturamento x Região
plt.figure()
sns.barplot(data=fat_regiao, x = "regiao", y = "valor total")
plt.title("Faturamento x Região")
plt.xlabel("Região")
plt.ylabel("Valor total")
plt.xticks(rotation=45)
plt.show()

#Gráfico de Evolução do Faturamento
plt.figure()
sns.lineplot(data=fat_mes, x = "mes", y = "valor total")
plt.title("Faturamento x Mês")
plt.xlabel("Mês")
plt.ylabel("Valor total")
plt.xticks(rotation=45)
plt.show()

#Gráfico de Top Clientes
plt.figure()
sns.barplot(data=fat_cliente, x = "cliente", y = "valor total")
plt.title("Faturamento x Cliente")
plt.xlabel("Cliente")
plt.ylabel("Valor total")
plt.xticks(rotation=45)
plt.show()

#Gráfico de Distribuição de Ticket Médio
plt.figure()
sns.barplot(data=fat_ticket_medio, x = "produto", y = "valor total")
plt.title("Faturamento x Categoria Ticket")
plt.xlabel("Categoria Ticket")
plt.ylabel("Valor total")
plt.xticks(rotation=45)
plt.show()