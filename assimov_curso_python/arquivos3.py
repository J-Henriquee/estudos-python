#Importando biblioteca
from pathlib import Path

#Passando item a ser deletado

item_deletado = 'Passear com cachorro'


caminho_padrão =  Path(__file__).parent 

#Abrindo arquivo html passado para leitura
with open(caminho_padrão / 'arquivo3.html') as arquivo_html:
    file_default = arquivo_html.readlines()

# Iterando sobre arquivo html e deletando o item solicitaod do to do list
for i, item in enumerate(file_default):
     print(item.replace('\n', '').strip())
     if item.replace('\n', '').strip() == item_deletado:
        del file_default[i - 2: i + 2] 
        break     
#Escrevendo novo arquivo atualizado
with open(caminho_padrão / 'arquivo3UP.html', mode= 'w' ) as arquivo_htmlUP:
    arquivo_htmlUP.writelines(file_default)





            
