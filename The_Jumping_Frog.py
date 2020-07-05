def jumping_frog(n, stones):
    jumps = {0: 1}
    queue = [0]
    while len(queue) > 0:
        cur = queue.pop(0)
        jump = stones[cur]
        if cur + jump >= n:
            return jumps[cur] + 1
        if cur + jump == n - 1:
            return jumps[cur] + 2
        if cur + jump not in jumps:
            jumps[cur + jump] = jumps[cur] + 1
            queue.append(cur + jump)
        if cur - jump > 0 and cur - jump not in jumps:
            jumps[cur - jump] = jumps[cur] + 1
            queue.append(cur - jump)            
    return "no chance :-("
