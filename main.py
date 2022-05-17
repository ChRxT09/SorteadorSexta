import Jogador as J
import random as r


def listarJogadores(time1):
  for i in range(len(time1)):
    print(f"{time1[i].getNome()}", end=";\n")
    
jogadores = []

def dividir(posicao,lista1,lista2):
  for i in range(len(posicao)):
    if i % 2 == 0:
      lista1.append(posicao[i])
    else:
      lista2.append(posicao[i])

time_verde = []
time_amarelo = []

aberto = True
positions = ['g','z','le', 'ld', 'm', 'a']

while aberto:
  print('=' * 20)
  player = input("insira o nome do jogador : ")
  if player =='':
    break
  position = input("insira a posição que joga : ")
  while position not in positions:
    print('*' * 20)
    position = input("insira uma posição válida : ")
  
  
  
  jogadores.append(J.Jogador(player,position))
  print('=' * 20)
  print('jogadores cadastrados:')
  for i in range(len(jogadores)):
    print(jogadores[i].getNome())

g = []
z = []
le = []
ld = []
m = []
a = []


for i in range(len(jogadores)):
  if jogadores[i].getPosicao() == 'g':
    g.append(jogadores[i])
  elif jogadores[i].getPosicao() == 'z':
    z.append(jogadores[i])
  elif jogadores[i].getPosicao() == 'le':
    le.append(jogadores[i])
  elif jogadores[i].getPosicao() == 'ld':
    ld.append(jogadores[i])
  elif jogadores[i].getPosicao() == 'm':
    m.append(jogadores[i])
  else:
    a.append(jogadores[i])


for i in range(20):
  r.shuffle(g)
  r.shuffle(z)
  r.shuffle(le)
  r.shuffle(ld)
  r.shuffle(m)
  r.shuffle(a)

dividir(g,time_amarelo,time_verde)
dividir(z,time_amarelo,time_verde)
dividir(le,time_amarelo,time_verde)
dividir(ld,time_amarelo,time_verde)
dividir(m,time_amarelo,time_verde)
dividir(a,time_amarelo,time_verde)

listarJogadores(time_amarelo)
print('='* 20)
listarJogadores(time_verde)