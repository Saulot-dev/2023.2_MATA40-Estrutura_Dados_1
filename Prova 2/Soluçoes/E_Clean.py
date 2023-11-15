#mini-heap to simulate a process manager
#the lower the priority, the higher
#put the lower in the root, take it off
#then put put the last node in it's place
#fix down comparing prioritys

#todo
    #fix down

class No:
    def __init__(self, id, pri):
        self.id = id
        self.pri = int(pri) #priority
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
            self.insert_subtree(self.root, node)
    
    def insert_subtree(self, node):
        temp_root = self.last_father()
        if not temp_root.left:
            temp_root.left = node
        elif not temp_root.right: #elif redundant
            temp_root.right = node
        node.father = temp_root
        self.fix_up(node)

    def fix_up(self, node): #if father's pri > son's, change. Recursive
        if node.father:
            if node.pri < node.father.pri:
                temp_son = (node.father.id, node.father.pri)
                #exchange
                node.father.id = node.pri
                node.father.pri = node.id
                node.id = temp_son.id
                node.pri = temp_son.pri
                self.fix_up(node.father)

    def last_father(self): #find last element in Heap
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
            
    #if son's pri (wich one(left/right)) < father's, change. Recursive
    #def fix_down(self, r):

    
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
    node = No(id, pri)
    count += 1
    h.insert(node)
    """ if count == q:
        count = 0 """
h.preorder(h.root)