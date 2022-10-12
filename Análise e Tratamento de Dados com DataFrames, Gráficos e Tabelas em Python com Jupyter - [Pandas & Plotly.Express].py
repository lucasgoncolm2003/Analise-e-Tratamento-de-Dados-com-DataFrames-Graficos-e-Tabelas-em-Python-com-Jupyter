#!/usr/bin/env python
# coding: utf-8

# In[8]:


# ----Importação da base de dados
import pandas as pd
tabela = pd.read_csv(r"Endereço até o Arquivo")
# read_csv: Leitura da Base de Dados em Formato CSV
tabela = tabela.drop("Unnamed: 0", axis=1)
# drop: Apaga a Coluna Sem Nome (axis=1 é Coluna)
display(tabela)
# display: Mostra a Tabela no Display


# In[9]:


# ----Tratamento de Dados
# Converte Valores da Coluna "Total Gasto" para Numérico, com Erro Coerce.
# Erro Coerce: Conversão Inválida é definida por NaN.
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# dropna(how="all", axis=1): deleta Todas as Colunas (axis=1) da Base.
tabela = tabela.dropna(how="all", axis=1)
# dropna(how="any", axis=0): deleta Qualquer uma das Linhas (axis=0) da Base.
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())


# In[10]:


# ----Análise Inicial
# Contagem de Instâncias na Coluna de Churn, ou de Cancelamento
print(tabela["Churn"].value_counts())
# normalize=True: retorna a Porcentagem dos Valores Contados
# map("{:.1%}".format): faz um Map dos Valores Formatados para uma Casa Decimal
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[11]:


# ----Análise Completa
import plotly.express as px
for coluna in tabela.columns:
# Cria um Gráfico com base em uma Coluna da Tabela
# Edições em Gráficos são feitas em: https://plotly.com/python/histograms/
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
# Elaboração de Histograma, com Texto Automático.
# color_discrete_sequence=["blue", "green"] muda as Cores do Gráfico
# show: realiza a Exibição do Gráfico
    grafico.show()


# In[12]:


get_ipython().system('pip install plotly')

