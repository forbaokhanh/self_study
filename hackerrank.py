def array_left_rotation(a, n, k):
    k = k % n
    b = [0]*n
    for i in range(len(a)):
        new_i = i - k
        if new_i < 0:
            new_i = n + new_i
        b[new_i] = a[i]
    return b
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))