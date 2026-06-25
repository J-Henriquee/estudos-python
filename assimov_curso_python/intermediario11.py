import datetime

def diff_tempo(horarioI, horarioF):
    horarioI = datetime.datetime.strptime(horarioI, '%H:%M:%S')
    horarioF = datetime.datetime.strptime(horarioF, '%H:%M:%S')
    delta = horarioF - horarioI
    total_segundos =int(delta.seconds)
    horas = total_segundos // 3600
    minutos = total_segundos % 3600 // 60 
    segundos = total_segundos % 60

    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

inicio = '08:34:21'
fim = '13:55:09'

diff = diff_tempo(inicio, fim)

print(diff)