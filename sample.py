def problem_1(S, K):
    i = len(S) - 1
    license = ""
    timer = 0
    while i > -1:
        if timer == K:
            timer = 0
            license = "-" + license
        elif S[i] == "-":
            i = i - 1
            pass
        else:
            license = S[i].upper() + license
            timer += 1
            i = i - 1
    return license

def solution(A, B, T):
    # write your code in Python 2.7
    if T is None: 
        return (0,0)

    l_size, l_best = solution(A,B,T.l) 
    r_size, r_best = solution(A,B,T.r) 

    if A <= T.x <= B and l_size >= 0 and r_size >= 0:
        return (1 + l_size + r_size,1 + l_size + r_size)
    else:
        return (-1,max(l_best,r_best))

def solved(A, B, T):
    if T is None:
        return (0, 0, None, None)
    left_ans, left_size, left_min, left_max = solved(A, B, T.l)
    right_ans, right_size, right_min, right_max = solved(A, B, T.r)
    cur_tree_size = 1 + left_size + right_size

    print T.x
    
    if T.x is None:
        range_min = left_min
    if left_min is None:
        range_min = T.x
    elif T.x is not None and left_min is not None:
        range_min = min(T.x, left_min)
    
    if T.x is None:
        range_max = right_max
    if right_max is None:
        range_max = T.x
    elif T.x is not None and right_max is not None:
        range_max = max(T.x, right_max)
        
    cur_ans = max(left_ans, right_ans)

    if A < range_min and range_max < B:
        cur_ans = cur_tree_size 

    return (cur_tree_size, cur_ans, range_min, range_max)


class Tree(object):
    def __init__(self, X, left=None, right=None):
        self.x = X
        self.r = right
        self.l = left


if __name__ == "__main__":
    # S = "2-4A0r7-4k"
    # K = 7
    # print problem_1(S, K)
    T = Tree(25, 
            Tree(19, 
                Tree(12, Tree(4), None), 
                Tree(22, None, Tree(23))), 
            Tree(37, 
                Tree(26, None, Tree(30)), 
                None))
    A = 15
    B = 29
    print solution(A, B, T)    