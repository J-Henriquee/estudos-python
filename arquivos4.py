from pathlib import Path
import pandas as pd


pasta_atual = Path(__file__).parent

pasta_unificada = pasta_atual / 'planilhas' / 'planilha_consolidada' / 'clientes.xlsx'

excel = pd.ExcelFile(pasta_unificada)

abas = excel.sheet_names
    
def separar_pasta(pasta):
    for n in abas:
        tabela_excel = pd.read_excel(pasta, sheet_name={n})
        tabela_excel.to_excel(pasta_atual / 'planilhas' / 'planilhas_separadas'/ f'clientes_{n}.xlsx', index=False)
    


separar_pasta(pasta_unificada)


def juntar_planilha(pasta):
    with pd.ExcelWriter(pasta_atual / 'planilhas' / 'planilhas_juntas.xlsx') as planilha_unificada:
        for n in abas:
            tabela = pd.read_excel(pasta / f'clientes_{n}.xlsx')
            tabela.to_excel(planilha_unificada, sheet_name={n}, index=False)

juntar_planilha(pasta_atual / 'planilhas' / 'planilhas_separadas')




            
