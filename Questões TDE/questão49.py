def converter_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


def converter_para_horario(segundos_totais):
    horas = segundos_totais // 3600
    segundos_totais %= 3600
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    return horas, minutos, segundos


hora_inicio = int(input("Hora de início (0-23): "))
minuto_inicio = int(input("Minuto de início (0-59): "))
segundo_inicio = int(input("Segundo de início (0-59): "))


duracao_segundos = int(input("Duração da experiência em segundos: "))


segundos_inicio = converter_para_segundos(
    hora_inicio, minuto_inicio, segundo_inicio)


segundos_termino = segundos_inicio + duracao_segundos


hora_termino, minuto_termino, segundo_termino = converter_para_horario(
    segundos_termino)


print("Horário de término da experiência:",
      f"{hora_termino:02d}:{minuto_termino:02d}:{segundo_termino:02d}")
