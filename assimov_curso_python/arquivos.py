from pathlib import Path 
import os

print(Path.home() / 'LivroFacu')
diretório = input('Type your directory location\n')

# Adicionamos um parâmetro 'prefixo' que começa vazio
def return_size_directories(d_location, profundidade=1, prefixo=''):
    
    diretórios = os.listdir(d_location)
    files_sum = 0 # 1. Criamos a "caixa" FORA do loop para não resetar

    for name in diretórios:
        loc = Path(d_location) / name
        
        if os.path.isfile(loc):
            # É arquivo: calcula o tamanho e soma na caixa
            loci = os.path.getsize(loc) / (1024 * 1024)
            print(f'{prefixo}{name} {loci:.2f} mb') # O prefixo aparece aqui!
            files_sum += loci
            
        else:
            # É pasta! 
            if profundidade > 0:
                print(f'{prefixo}[PASTA] {name}')
                
                # 2. A MÁGICA: Chamamos a função de novo. 
                # Diminuímos a profundidade E somamos um '-' no prefixo atual!
                tamanho_subpasta = return_size_directories(loc, profundidade - 1, prefixo + '-')
                
                # 3. Pegamos o que a função devolveu (número puro) e somamos na caixa principal
                files_sum += tamanho_subpasta

    # No final do diretório atual, devolvemos a soma de tudo que achamos
    return files_sum 

# Chamada inicial
tamanho_total = return_size_directories(diretório, profundidade=2)
print(f'\nTamanho total do diretorio principal: {tamanho_total:.2f} mb')