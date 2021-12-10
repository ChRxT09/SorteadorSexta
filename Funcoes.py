
def dividir(posicao, time1, time2):
  for i in range(len(posicao)):
    if i % 2 == 0:
      time1.append(posicao[i])
    else:
      time2.append(posicao[i])
