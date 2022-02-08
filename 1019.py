tempo = int(input())

hora = tempo //3600
tempo %= 3600
minuto = tempo // 60
tempo %= 60
segundo = tempo

print(f"{hora}:{minuto}:{segundo}")