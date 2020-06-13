from timeit import default_timer as timer

start = timer()
partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
n = 11
partition = 42
pentagonals = []

for k in range(1, 2000):
    pentagonals.append(k*(3*k-1)/2)
    k *= -1
    pentagonals.append(k*(3*k-1)/2)

while partition != 0:
    partition = 0
    pentagonal = 0
    index = 0
    temp = 0
    is_positive = False
    while pentagonal <= n:
       if is_positive: partition += temp
       else: partition -= temp
       pentagonal = pentagonals[index]
       temp = partitions[n - pentagonal]
       if index % 2 == 0: is_positive = not is_positive
       index += 1
    partition %= 1000000
    partitions.append(partition)
    n += 1

ans = n - 1
elapsed_time = (timer() - start) * 1000
print "Found %d as the answer in %d ms." % (ans, elapsed_time)
