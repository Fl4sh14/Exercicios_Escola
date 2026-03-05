from collections import deque

fila = deque()

fila.append('João')
fila.appendleft('Maria')
fila.appendleft('Joaquina')
fila.appendleft('António')

fila.popleft()
fila.pop()

print(f'Quem ficou na fila: {list(fila)}')
