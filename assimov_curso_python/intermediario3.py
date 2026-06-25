gosta_de_programar = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
gosta_de_futebol = {'Mateus', 'Roberto', 'Paulo', 'Pedro'}
estuda_na_asimov_academy = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}

conjunto_escolhido = gosta_de_programar & estuda_na_asimov_academy - gosta_de_futebol
print(conjunto_escolhido)