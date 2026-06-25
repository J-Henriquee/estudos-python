import pandas as pd
import random
from pathlib import Path

# 1. Montando o cenário de pastas (Igual ao do professor)
pasta_atual = Path(__file__).parent
pasta_planilhas = pasta_atual / 'planilhas'
pasta_consolidada = pasta_planilhas / 'planilha_consolidada'
pasta_separadas = pasta_planilhas / 'planilhas_separadas'

# Garante que toda a árvore de pastas exista antes de gerar o arquivo
pasta_consolidada.mkdir(parents=True, exist_ok=True)
pasta_separadas.mkdir(parents=True, exist_ok=True)

# 2. Gerando a massa de dados
estados = ['SP', 'PR', 'SC', 'RS']
nomes_base = ['Patricia Tattershall', 'Heather Glaze', 'Eleanor Bryant', 'Luis Rivers', 
              'Vicki Gonzalez', 'Jennifer Agro', 'Andrew Nichols', 'Leo Mendoza']

caminho_final_excel = pasta_consolidada / 'clientes.xlsx'

with pd.ExcelWriter(caminho_final_excel) as writer:
    for estado in estados:
        dados_estado = []
        for i in range(15):
            nome = random.choice(nomes_base) + f" {i}{estado}"
            telefone = f"9{random.randint(10000000, 99999999)}"
            email = nome.split()[0].lower() + "@gmail.com"
            receita = round(random.uniform(1000.0, 900000.0), 2)
            dados_estado.append([nome, telefone, email, receita, estado])
        
        df_estado = pd.DataFrame(dados_estado, columns=['Nome', 'Telefones', 'email', 'receita', 'Estado'])
        df_estado.to_excel(writer, sheet_name=estado, index=False)

print("✅ Cenário montado em 'planilhas/planilha_consolidada/clientes.xlsx'!")