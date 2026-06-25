import re
import datetime


texto = ''''A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal'''

padrao = '[0-9]{2}/[0-9]{2}/[0-9]{4}'



datas = re.findall(padrao, texto)
datas_new = []

for data in datas:
    data = datetime.datetime.strptime(data, '%d/%m/%Y')
    datas_new.append(data.date())

print(datas_new)
