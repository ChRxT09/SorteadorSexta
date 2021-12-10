import random as r
import Funcoes as f
jogadores = []

goleiros = []
zagueiros = []
lateralEsq = []
lateralDir =[]
meias = []
atacantes = []

time_verde = []
time_amarelo = []

aberto = True
positions = ["g",'z','le', 'ld', 'm', 'a']

while aberto:
  print('=' * 20)
  player = input("insira o nome do jogador : ")
  if player =='':
    break
  position = input("insira a posição que joga : ")
  while position not in positions:
    print('*' * 20)
    position = input("insira uma posição válida : ")
  
  
  
  jogadores.append({"nome": player, "posição": position})



for i in range(len(jogadores)):
  if jogadores[i]["posição"] =='g':
    goleiros.append(jogadores[i])
  elif jogadores[i]["posição"] == 'z':
    zagueiros.append(jogadores[i])
  elif jogadores[i]["posição"] == 'le':
    lateralEsq.append(jogadores[i])
  elif jogadores[i]["posição"] == 'ld':
    lateralDir.append(jogadores[i])
  elif jogadores[i]["posição"] == 'm':
    meias.append(jogadores[i])
  elif jogadores[i]["posição"] == 'a':
    atacantes.append(jogadores[i])



for i in range(10):
  r.shuffle(goleiros)
  r.shuffle(zagueiros)
  r.shuffle(lateralEsq)
  r.shuffle(lateralDir)
  r.shuffle(meias)
  r.shuffle(atacantes)



f.dividir(goleiros, time_verde, time_amarelo)
f.dividir(zagueiros, time_verde, time_amarelo)
f.dividir(lateralEsq, time_verde, time_amarelo)
f.dividir(lateralDir, time_verde, time_amarelo)
f.dividir(meias, time_verde, time_amarelo)
f.dividir(atacantes, time_verde, time_amarelo)


print()
print(f"{'#' * 10} TIME VERDE {'#' * 10}")
for i in range(len(time_verde)):
  if i != len(time_verde) - 1:
    print(f'{time_verde[i]["nome"]}', end='; \n')
  else:
    print(f'{time_verde[i]["nome"]}', end='. \n \n')



print(f"{'#' * 10} TIME AMARELO {'#' * 10}")
for i in range(len(time_amarelo)):
  if i != len(time_amarelo) - 1:
    print(f'{time_amarelo[i]["nome"]}', end='; \n')
  else:
    print(f'{time_amarelo[i]["nome"]}', end='.')

