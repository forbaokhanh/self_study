# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
        return
    middle = findMiddle(len(nums))
    root = TreeNode(nums[middle])
    if len(nums) == 1:
        return root
    leftHalf = nums[:middle]
    rightHalf = nums[middle + 1:]
    build(rightHalf, root, False)
    build(leftHalf, root, True)
    return root
    
def build(nums, node, left):
    if len(nums) == 0:
        return
    middle = findMiddle(len(nums))
    middleNode = TreeNode(nums[middle])
    if left:
        node.left = middleNode
    else:
        node.right = middleNode
    if len(nums) == 1:
        return
    leftHalf = nums[:middle]
    rightHalf = nums[middle + 1:]
    build(rightHalf, middleNode, False)
    build(leftHalf, middleNode, True)

def findMiddle(num):
    if num % 2 == 0:
        return num / 2 - 1
    return num / 2

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Works by checking whether the number at an index has been flipped already!
    This works because the values at an index all fall into the index range.
    """
    ret = []
    for n in nums:
        if nums[abs(n)-1] < 0:
            ret.append(abs(n))
        else:
            nums[abs(n)-1] *= -1
    return ret

def poorPigs(self, buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.stack = {}
        self.keys = []
        

    def get(self, key):
        """
        :rtype: int
        """
        return self.stack.get(key, -1)
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.capacity == self.count:
            key = self.keys.pop()
            self.stack.pop(key)
            self.count -= 1
        if key not in self.keys:
            self.keys.insert(0,key)
            self.count += 1
        self.stack[key] = value
        return

def wordSquares(words):
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """
    def gather_trie(trie, res, item):
        if not trie:
            if len(item) > 0:
                res.append(item)
        for c in trie:
            gather_trie(trie[c], res, item + c)
            
    def get_words(trie, prefix):
        for c in prefix:
            if c not in trie:
                return []
            trie = trie[c]
        res = []
        gather_trie(trie, res, prefix)
        return res
        
    def add_word(trie, word, start):
        if start==len(word):
            return
        if (word[start] not in trie):
            trie[word[start]] = {}
        add_word(trie[word[start]], word, start + 1)
        
    def build_trie(words):
        trie = {}
        for word in words:
            add_word(trie, word, 0)
        return trie
        
    def backtrack(trie, res, item, chari, avg_len, prefix):
        candidates = get_words(trie, prefix)
        for cand in candidates:
            if len(item) == avg_len - 1:
                res.append(list(item + [cand]))
                continue
            new_prefix = ''.join([word[chari + 1] for word in (item + [cand])])
            backtrack(trie, res, item + [cand], chari + 1, avg_len, new_prefix)
        
    if len(words) == 0:
        return [[]]
    trie = build_trie(words)
    res = []
    avg_len = len(words[0])
    backtrack(trie, res, [], 0, avg_len, '')
    return res

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    A = nums1
    B = nums2
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
    return

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.data = matrix
        self.rows = len(matrix)
        if self.rows != 0:
            self.cols = len(matrix[0])
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if row < self.rows and hasattr(self, 'cols'):
            if self.cols > col:
                self.data[row][col] = val
                print self.data[row][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        start_col = col1
        while row1 <= row2:
            while start_col <= col2:
                res += self.data[row1][start_col]
                start_col += 1
            start_col = col1
            row1 += 1
        return res

# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heappush(h, value)
#     return [heappop(h) for i in range(len(h))]

# heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

def findMissingRanges(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    range_array = [(lower, upper)]
    i = 0
    for i in range(len(nums)):
        print range_array
        x = nums[i]
        prev_range = range_array.pop()
        prev_lower = prev_range[0]
        prev_upper = prev_range[1]
        if x == prev_lower:
            if x + 1 != upper:
                new_lower = x + 1
                new_lower_tuple = (x + 1, prev_range[1])
                range_array.append(new_lower_tuple)
                continue
            else:
                return range_array
        elif x - 1 == prev_lower:
            new_lower_tuple = (x - 1)
            range_array.append(new_lower_tuple)
        else:
            print "here"
            new_lower_tuple = (prev_lower, x - 1)
            range_array.append(new_lower_tuple)
        new_upper_tuple = (x + 1, prev_upper)
        range_array.append(new_upper_tuple)
    return range_array

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return_str = ""
    string = s.split(' ')
    new_string = []
    for x in string:
        if x:
            new_string.append(x)
    print new_string
    i = len(string) - 1
    print string
    while i >= 0:
        return_str += string[i]
        if i != 0:
            return_str += ' '
        i -= 1
    return return_str

if __name__ == '__main__':
    print reverseWords("    ")






