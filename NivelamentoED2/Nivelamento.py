from queue import PriorityQueue
from queue import Queue
import random

# questao 1
# os primeiros 4 elementos sao hardcoded
print("QUESTAO 1")
nums = [1, 7, 2, 9]

i = 0
num_max = 100
while i < num_max:
  nums.append(nums[i] + nums[i + 1])
  i += 1

print(nums)

# questao 2
print("\nQUESTAO 2")
lista = [1, 5, 4, 3, 2, 6, 7]
lista.sort()
print(lista)

# questao 3
# sim, eh possivel inverter
# percorrer cada caracter da pilha empilhando, e desempilhar na nova string ao chegar a um espaço
print("\nQUESTAO 3")
texto = "o rato roeu a roupa do rei de roma "
pilha = []
out = ""

for i in range(0, len(texto)):
  if texto[i] == " ":
    for j in range(0, len(pilha)):
      out += pilha.pop()
    out += " "
  else:
    pilha.append(texto[i])
print(out)

#questao 4
print("\nQUESTAO 4")


class Cabo:

  def __init__(self, tam):
    self.tam = tam


n = 10
fila = PriorityQueue(n)

fila.put(2)
fila.put(1)
fila.put(3)
fila.put(4)
fila.put(5)
fila.put(6)
fila.put(7)
fila.put(8)
fila.put(9)
fila.put(10)

print(fila.queue)

for i in range(n - 1):
  fila.put(fila.get() + fila.get())
  print(fila.queue)

#questao 5
print("\nQUESTAO 5")

pilha = Queue()
cont = 1

while True:
  num = int(
    input(
      'Digite 1 para avançar a página, 2 para voltar ou 3 para encerrar: '))

  if num == 1:
    pilha.put('pagina' + str(cont))
    cont += 1
    print('Você está na pagina ' + str(cont))

  elif num == 2:
    if pilha.empty() is True:
      print('Não é possível voltar mais!')
    else:
      pilha.get()
      cont -= 1
      print('Você está na pagina ' + str(cont))
  else:
    break

#questao 6
print("\nQUESTAO 6 (forma facil)")
lista = []
num_nos = int(input("Digite o numero de nos da lista: "))
for k in range(num_nos):  #populando a lista com numeros aleatorios
  lista.append(random.randint(0, 10))

print("O no do meio é o No[" + str(int(num_nos / 2) + 1) +
      "] cujo valor é = " + str(lista[int(num_nos / 2) + 1]))

#questão 6.1
print("\nQUESTAO 6.1 (forma razoavel)")
lista1 = []
num_nos1 = int(input("Digite o numero de nos da lista: "))
for z in range(num_nos1):  #populando a lista com numeros aleatorios
  lista1.append(random.randint(0, 100))

print("A lista gerada foi: " + str(lista1))

x = 0
y = len(lista1) - 1
for z in range(num_nos1):
  if x == y:
    print("nó central é " + str(x + 1) + " cujo valor é " + str(lista1[x + 1]))
    break
  elif x + 1 == y:
    print("os nós do meio são " + str(x + 1) + " e " + str(y + 1) +
          " e seus valores são " + str(lista1[x + 1]) + " e " +
          str(lista1[y + 1]))
    break
  else:
    x += 1
    y -= 1

# questao 7
print("\nQUESTAO 7")
from queue import Queue

fila = Queue()

#Colocando as musicas na fila
musica = "musica1"
fila.put(musica)

musica = "musica2"
fila.put(musica)

musica = "musica3"
fila.put(musica)

#Tirando a musica da fila e colocando para tocar
print("Musica sendo tocada agora: " + fila.get())

print("Musica sendo tocada agora: " + fila.get())

print("Musica sendo tocada agora: " + fila.get())

# questao 7.1
print("\nQUESTAO 7.1 (forma razoavel)")

fila1 = Queue()
contador = 1
musica1 = None

while True:
  escolha = (int(
    input(
      'Digite 1 para adicionar uma música a fila, 2 para tocar a próxima música e 3 para encerrar o programa: '
    )))

  if escolha == 1:
    fila1.put(input('Digite o nome da musica que deseja adicionar à fila: '))
  elif escolha == 2:
    if fila1.empty():
      print("A fila de músicas está vazia")
    else:
      musica1 = fila1.get()
      print("Música que está tocando atualmente: " + musica1)
  else:
    break

# questao 8
print("\nQUESTAO 8")
lotes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]

for i in range(len(lotes) - 1):
  trocarealizada = False
  for j in range(len(lotes) - 1):
    if (lotes[j] > lotes[j + 1]):
      trocarealizada = True
      aux = lotes[j]
      lotes[j] = lotes[j + 1]
      lotes[j + 1] = aux
  if not trocarealizada:
    break
  print(lotes)
