from pathlib import Path
import shutil
import os 


caminho_padrão = Path(__file__).parent

caminhos_organizados = caminho_padrão / 'ORGANIZADO'

caminhos_organizados.mkdir(exist_ok= True)


arquivos =  os.listdir(caminho_padrão)

extensões = set()

for arquivo in arquivos:
    arquivo = caminho_padrão / f'{arquivo}'
    sufixo = arquivo.suffix
    if arquivo.is_file() and arquivo.name != Path(__file__).name:
        caminho_organizado = caminhos_organizados / f'{sufixo.lstrip('.').upper()}'
        caminho_organizado.mkdir(exist_ok= True)
        shutil.move(arquivo, caminho_organizado)
    

extensões = list(extensões)








#for extensão in extensões:
#    caminho_organizado = caminho_padrão / f'{extensão.lstrip('.').upper()}'
#    if not (caminhos_organizados / f'{caminho_organizado}').exists():
#        caminho_organizado.mkdir(exist_ok= True)
#        shutil.move(caminho_organizado, caminhos_organizados)

