from collections import deque
sites = deque()

sites.append('site 1')
sites.append('site 2')
sites.append('site 3')
sites.append('site 4')

sites.pop()
sites.pop()

for objeto in sites:
    print(objeto)
