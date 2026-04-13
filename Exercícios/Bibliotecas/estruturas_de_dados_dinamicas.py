# programa em Python para implementar uma pilha

# Função para criar a pilha
def createStack():
    stack = []
    return stack

# A pilha está vazia quando o tamanho é 0
def isEmpty(stack):
    return len(stack) == 0

# Função para adicionar um elemento à pilha
def push(stack, item):
    stack.append(item)
    print(item + " inserido na pilha ")

# Função para remover um elemento da pilha.
def pop(stack):
    if (isEmpty(stack)):
        raise IndexError("Pilha está vazia")
    else:
        return stack.pop()

# função para mostrar o elemento do topo da pilha sem o remover
def peek(stack):
    if (isEmpty(stack)):
        raise IndexError("Pilha está vazia")
    else:
        return stack[len(stack) - 1]

# teste às funções anteriores
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " removido da pilha")
print(pop(stack) + " removido da pilha")


from collections import deque
deque()
deque(['a','b','c'])
deque([{'data': 'a'}, {'data': 'b'}])
llist = deque("abcde")
llist
llist.append("f")
llist
llist.pop()
llist
llist.appendleft("z")
llist
llist.popleft()
llist


from collections import deque
queue = deque()
queue
queue.append("Mary")
queue.append("John")
queue.append("Susan")
queue
queue.popleft()
queue
queue.popleft()
queue


from collections import deque
history = deque()
history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
history
history.popleft()
history.popleft()
history
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
class LinkedList:
    def __init__(self):
     self.start_node = None
def traverse_list(self):
    if self.start_node is None:
        print("A lista encadeada está vazia")
        return
    else:
        n = self.start_node
    while n is not None:
        print(n.item , " ")
        n = n.ref
def insert_at_start(self, data):
    new_node = Node(data)
    new_node.ref = self.start_node
    self.start_node= new_node
def insert_at_end(self, data):
    new_node = Node(data)
    if self.start_node is None:
        self.start_node = new_node
        return
    n = self.start_node
    while n.ref is not None:
        n= n.ref
        n.ref = new_node;
def insert_after_item(self, x, data):
    n = self.start_node
    print(n.ref)
while n is not None:
    if n.item == x:
        break
        n = n.ref
    if n is None:
        print("item not in the list")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node
