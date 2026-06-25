import random

def busca_dados():
    if random.random() > 0.5:
         return None
    return 'xxxxx'

def processa_dados(dados):
     return f'Dados "{dados}" foram processados'

dados_banco = busca_dados()

if dados_banco is not None:
     dados_processados = processa_dados(dados_banco)
else:
     dados_processados = 'N/A'

print(f'Resultados: {dados_processados}')





if (dados_banco := busca_dados()) is not None:
     dados_processados = processa_dados(dados_banco)
else:
     dados_processados = 'N/A'

print(f'Resultados: {dados_processados}')

dados_processados = processa_dados(dados_banco) if (dados_banco := busca_dados()) is not None else 'N/A'

print(f'Resultados: {dados_processados}')

