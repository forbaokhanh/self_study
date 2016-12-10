import random
"""
TIME:
                Average     Worst
    Access:     O(nlogn)    O(n)
    Search:     O(nlogn)    O(n)
    Insertion:  O(nlogn)    O(n)
    Deletion:   O(nlogn)    O(n)

    Deletion is very simple if you are given a node to delete as 
    opposed to the SLL, because no back pointer.
SPACE: O(nlogn)
"""
class SkipListError(Exception):
    pass

class Node(object):
    def __init__(self, data, level):
        self.data = data
        if level <= 0:
            raise SkipListError("level must be > 0")
        self.level = level
        self.forward = [None] *  level

class SkipList(object):
    """ simple skiplist
    """
    def __init__(self, **kvargs):
        try:
            self.max_level = int(kvargs["max_level"])
        except: 
            self.max_level = 16
        self.head = Node(None, self.max_level)
        self.list_level = 1
        self.head.forward = [None] * self.max_level
    
    def __random_level(self):
        # return reduce(lambda x, y: x+y, [1 for i in range(self.max_level - 1) if random.uniform(0, 1) < 0.5 else 0])
        result = 1
        while random.uniform(0, 1) < 0.5 and result < self.max_level:
            result += 1
        return result
    
    def insert(self, data):
        node = Node(data, self.__random_level())
        update = [None] * self.max_level
        current = self.head
        for i in reversed(range(self.list_level)):
            while current.forward[i] and cmp(data, current.forward[i].data) > 0:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        if current and data == current.data:
            return True
        
        if node.level > self.list_level:
            for i in range(self.list_level, node.level):
                update[i] = self.head
            self.list_level = node.level
        
        for i in range(node.level):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node
        
        return True
    
    def search(self, data):
        current = self.head
        for i in range(self.list_level)[::-1]:
            while current.forward[i] and cmp(data, current.forward[i].data) > 0:
                current = current.forward[i]
        
        current = current.forward[0]
        if current and data == current.data:
            return True
        else:
            return False
    
    def delete(self, data):
        update = [None] * self.max_level
        current = self.head
        for i in reversed(range(self.list_level)):
            while current.forward[i] and cmp(data, current.forward[i].data) > 0:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        if not current or data != current.data:
            return False
        
        for i in range(self.list_level):
            if update[i].forward[i] != current: break
            update[i].forward[i] = current.forward[i]
        del current
        
        while self.list_level > 0 and self.head.forward[self.list_level - 1] == None:
            self.list_level -= 1
        
        return True
    
    def __str__(self):
        datas = []
        current = self.head.forward[0]
        avg_level = 0
        total_level = 0
        count = 0
        while current:
            datas.append("(data: %s, level: %d)" % (str(current.data), current.level))
            total_level += current.level
            count += 1
            current = current.forward[0]
        avg_level = 1.0 * total_level / count
        return "SkipList: list_level -> %d, avg_level -> %f, data -> [%s]" % \
               (self.list_level, avg_level, ",".join(datas[:100]))
        
if __name__ == "__main__":
    l = SkipList()
    assert l.insert(0.00)
    for i in reversed(range(10000)):
       assert l.insert(i)

    import string
    for i in string.lowercase:
        assert l.insert(i)

    assert l.search("b")
    assert l.delete("b")
    assert not l.search("b")
    print l