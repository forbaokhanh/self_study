"""
TIME:
            Average == Worst
    Access:     O(n)
    Search:     O(n)
    Insertion:  O(1)
    Deletion:   O(1)
"""
class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()

    def peek(self, item):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

"""
TIME:
            Average == Worst
    Access:     O(n)
    Search:     O(n)
    Insertion:  O(1)
    Deletion:   O(1)
"""
class Queue:
    def __init__(self, capacity=10):
        self.capacity = 10
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


"""
TIME:
            Average == Worst
    Access:     O(n)
    Search:     O(n)
    Insertion:  O(1)
    Deletion:   O(1)
"""
class SinglyLinkedList:

    class SingleNode:
        def __init__(self, initdata):
            self.data = initdata
            self.next = None

        def getData(self):
            return self.data

        def getNext(self):
            return self.next

        def setData(self,newdata):
            self.data = newdata

        def setNext(self,newnext):
            self.next = newnext

    def __init__(self, data=None):
        self.head = None
        self.curr = self.head

    def add(self, item):
        temp = SingleNode(item)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        curr = this.head
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def search(self, item):
        curr = this.head
        node = None
        found = False
        while curr is not None and not found:
            if curr.getData() == item:
                node = curr
                found = True
            else:
                curr = curr.getNext()
        return node

    def remove(self, item):
        prev = None
        curr = this.head
        found = False
        while curr is not None and not found:
            if curr.getData() == item:
                if prev == None:
                    self.head = curr.getNext()
                found = True
                prev.setNext(curr.getNext())
                curr.setNext(None)
                return
            else:
                prev = curr
                curr = curr.getNext() 
        return

"""
TIME:
            Average == Worst
    Access:     O(n)
    Search:     O(n)
    Insertion:  O(1)
    Deletion:   O(1)

    Deletion is very simple if you are given a node to delete as 
    opposed to the SLL, because no back pointer.
"""
class DoublyLinkedList:

    class DoubleNode:
        def __init__(self, initdata):
            self.data = initdata
            self.next = None
            self.prev = None

        def getData(self):
            return self.data

        def getNext(self):
            return self.next

        def getPrev(self):
            return self.prev

        def setData(self,newdata):
            self.data = newdata

        def setNext(self,newnext):
            self.next = newnext

        def setPrev(self, newprev):
            self.prev = newprev

    def __init__(self, data=None):
        self.head = None
        self.curr = self.head

    def add(self, item):
        temp = DoubleNode(item)
        temp.setNext(self.head)
        self.head.setPrev(temp)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        curr = this.head
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def search(self, item):
        curr = this.head
        node = None
        found = False
        while curr is not None and not found:
            if curr.getData() == item:
                node = curr
                found = True
            else:
                curr = curr.getNext()
        return node

    def remove(self, item):
        prev = None
        curr = this.head
        found = False
        while curr is not None and not found:
            if curr.getData() == item:
                if prev == None:
                    self.head = curr.getNext()
                    curr.getNext.setPrev(prev)
                found = True
                prev.setNext(curr.getNext())
                curr.getNext().setPrev(prev)
                curr.setNext(None)
                curr.setPrev(None)
                return
            else:
                prev = curr
                curr = curr.getNext()
        return

############ HashTable helper functions
def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size

"""
TIME:
                Average     Worst
    Access:      N/A        N/A
    Search:      O(1)       O(n)
    Insertion:   O(1)       O(n)
    Deletion:    O(1)       O(n)

    Deletion is very simple if you are given a node to delete as 
    opposed to the SLL, because no back pointer.
"""
class HashTable:
    """ Hash table which uses strings for keys. Value can be any object.
    Example usage:
        ht = HashTable(10)
        ht.set('a', 1).set('b', 2).set('c', 3)
        ht.get('c') = 30
    """
    def __init__(self, capacity = 1000):
        self.capacity = capacity
        self._keys = []
        self.size = 0
        self.data = [[] for i in range(capacity)]

    def find_by_key(self, key):
        index = hash_function(key, self.capacity)
        hash_table_cell = self.data[index]
        found_item = None
        for item in hash_table_cell:
            if item[0] == key:
                found_item = item
                break
        return found_item, hash_table_cell

    def set(self, key, obj):
        """ Insert object with key into hash table. If key already exists, then the object will be
        updated. Key must be a string. Returns self. """
        found_item, hash_table_cell = self.find_by_key(key)
        if found_item:
            found_item[1] = obj
        else:
            hash_table_cell.append((key, obj))
            self.size += 1
            self._keys.append(key)
        return self


    def get(self, key):
        """ Get object with key (key must be a string). If not found, it will raise a KeyError. """
        found_item, hash_table_cell = self.find_by_key(key)
        if found_item:
            return found_item[1]
        else:
            raise KeyError(key)

    def remove(self, key):
        """ Remove the object associated with key from the hashtable. If found, the object will
        be returned. If not found, KeyError will be raised. """
        found_item, hash_table_cell = self.find_by_key(key)
        if found_item:
            hash_table_cell.remove(found_item)
            self._keys.remove(key)
            self.size -= 1
            return found_item[1]
        else: raise KeyError(key)

    def keys(self):
        return self._keys

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        return '{' + ', '.join([key + ': ' + str(self.get(key)) for key in self._keys]) + '}'



class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

def preorder(root):
    if root == None:
        return
    print root.data
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    preorder(root.left)
    print root.data
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    preorder(root.left)
    preorder(root.right)
    print root.data


import heapq




if __name__ == '__main__':





