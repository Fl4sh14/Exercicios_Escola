from collections import deque
sites = deque()

sites.append('site 1')
sites.appendleft('site 2')
sites.appendleft('site 3')
sites.appendleft('site 4')

sites.popleft()
sites.popleft()

for objeto in sites:
    print(objeto)
