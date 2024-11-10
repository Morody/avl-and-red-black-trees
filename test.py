import pprint
class Node:


    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
    


def insert(node: Node, key, value):
    if (node is None): return None
    else:
        if (key < node.key):
            if (node.left is None): node.left = Node(key, value)
            else: insert(node.left, key, value)
        if (node.key is key): return node
        if (key > node.key):
            if (node.right is None): node.right = Node(key, value)
            else: insert(node.right, key, value)
    updateHeight(node)
    balance(node)



def search(node, key):
    if (node is None): return None
    else:
        if (key < node.key): return search(node.left, key)
        elif (key is node.key): return node
        elif (key > node.key): return search(node.right, key)


def getMin(node):
    if (node is None): return None
    if (node.left is None): return node
    return getMin(node.left)

def getMax(node):
    if (node is None): return None
    if (node.right is None): return node
    return getMax(node.right)


def delete(node, key):
    if (node is None): return None
    elif (key < node.key): node.left = delete(node.left, key)
    elif (key > node.key): node.right = delete(node.right, key)
    else:
        if (node.left is None or node.right is None):
            node = node.right if (node.left is None) else node.left
        else:
            maxInLeft = getMax(node.left)
            node.key = maxInLeft.key
            node.value = maxInLeft.value
            node.left = delete(node.left, maxInLeft.key)
    
    if (node is not None):
        updateHeight(node)
        balance(node)
    return node

def updateHeight(node):
    node.height = max(getHeight(node.left), getHeight(node.right)) + 1


def getHeight(node):
    return -1 if node is None else node.height

def getBalance(node):
    return getHeight(node.right) - getHeight(node.left) if (node is not None) else 0


def swap(a: Node, b: Node):
    bufferKey = a.key
    bufferVal = a.value
    a.key = b.key
    a.value = b.value
    b.key = bufferKey
    b.value = bufferVal

def rightRotate(node):
    buffer = node.right
    swap(node, node.left)
    node.right = node.left
    node.left = node.right.left
    node.right.left = node.right.right
    node.right.right = buffer
    updateHeight(node)
    updateHeight(node.right)

def leftRotate(node):
    buffer = node.left
    swap(node, node.right)
    node.left = node.right
    node.right = node.left.right
    node.left.right = node.left.left
    node.left.left = buffer
    updateHeight(node.left)
    updateHeight(node.right)


def balance(node):
    balance = getBalance(node)
    if (balance == -2):
        if(getBalance(node.left) == 1): leftRotate(node.left)
        rightRotate(node)
    if (balance == 2):
        if(getBalance(node.right) == -1): rightRotate(node.right)
        leftRotate(node) 

node = Node(5, 'Alex')

insert(node, 2, 'Brah')
insert(node, 4, 'Lol')
insert(node, 3, 'Sally')
insert(node, 0, 'Brown')
insert(node, 1, 'Drake')
insert(node, 10, 'Kelly')
insert(node, 6, 'Mars')
insert(node, 9, 'John')
#delete(node, 3)


pprint.pprint(vars(node.right.right.left.right))
