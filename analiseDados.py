import pandas as pd

tabela = pd.read_csv(r"C:\Users\paulo\Dropbox\Projetos\Python\telecom_users.csv")
#axis é o eixo 1 para coluna e 0 para linha
tabela = tabela.drop(["Unnamed: 0"], axis=1)
print(tabela)
print(tabela.info())