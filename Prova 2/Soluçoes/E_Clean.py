#mini-heap to simulate a process manager
#the lower the priority, the higher
#put the lower in the root, take it off
#then put put the last node in it's place
#fix down comparing prioritys

#todo
    #fix down

class Node:
    def __init__(self, id, pri):
        self.id = id
        self.pri = pri #priority
        self.left = None
        self.right = None
        self.father = None

class QNode:
    def __init__(self, node):
        self.node = node
        self.next = None

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, node):
        if self.front is None:
            self.front = node
        else:
            temp = self.front
            while temp.next:
                temp = temp.next
            temp.next = node
    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next
            return temp
        
class MiniHeap:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            self.insert_subtree(node)
    
    def insert_subtree(self, node):
        last_root = self.last_root()
        if not last_root.left:
            last_root.left = node
        elif not last_root.right: #elif redundant
            last_root.right = node
        node.father = last_root
        self.fix_up(node)

    def fix_up(self, node): #if father's pri > son's, change. Recursive
        if node.father:
            if node.pri < node.father.pri:
                temp_son = Node(node.father.id, node.father.pri)
                #exchange
                node.father.id = node.id
                node.father.pri = node.pri
                node.id = temp_son.id
                node.pri = temp_son.pri
                self.fix_up(node.father)

    def last_root(self): #find last element in Heap
        que = Queue()
        que.enqueue(QNode(self.root))
        #search for an empty slot in the heap, lvl by lvl
        while 1:
            temp_root = (que.dequeue()).node
            if temp_root.left:
                que.enqueue(QNode(temp_root.left))
                if temp_root.right:
                    que.enqueue(QNode(temp_root.right))
                else: #empty slot right
                    return temp_root
            else: #empty slot left
                return temp_root
            
    def change_root(self):
        last_root = self.last_root()
        if last_root.right:
            new_root = Node(last_root.right.id, last_root.right.pri)
            last_root.right = None
        elif last_root.left: #elif redundant
            new_root = Node(last_root.left.id, last_root.left.pri)
            last_root.left = None
        self.root.id = new_root.id
        self.root.pri = new_root.pri

    #if son's pri (wich one(left/right)) < father's, change. Recursive
    def fix_down(self, root):
        if root.left:
            if root.right:
                if root.pri > root.left.pri or root.pri > root.right.pri:
                    if root.left.pri < root.right.pri:
                        minor = root.left
                    else:
                        minor = root.right
                    temp_father = Node(root.id, root.pri)
                    root.id = minor.id
                    root.pri = minor.pri
                    minor.id = temp_father.id
                    minor.pri = temp_father.pri
                    self.fix_down(minor)
            elif root.pri > root.left.pri:
                minor = root.left
                temp_father = Node(root.id, root.pri)
                root.id = minor.id
                root.pri = minor.pri
                minor.id = temp_father.id
                minor.pri = temp_father.pri
                self.fix_down(minor)

    
    def preorder(self, r):
        if r:
            print(f'{r.id} {r.pri}')
            self.preorder(r.left)
            self.preorder(r.right)

#main
n, q  = map(int, input().split())
h = MiniHeap()
count = 0
for i in range(n):
    id, pri = input().split()
    node = Node(id, int(pri))
    count += 1
    h.insert(node)
    if count == q:
        h.change_root()
        h.fix_down(h.root)
        count = 0
h.preorder(h.root)