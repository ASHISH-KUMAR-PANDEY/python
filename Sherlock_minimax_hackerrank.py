import math
import os
import random
import re
import sys

# Complete the sherlockAndMinimax function below.
def sherlockAndMinimax(arr, p, q):
    arr = sorted(arr)
    minimum = sys.maxint
    min_ind = 0
    max_ans = -1
    max_ind = -1
    for i in range(0,len(arr)):
        if (abs(arr[i]-p)<minimum):
            minimum=abs(arr[i]-p)
            min_ind=p
    if (max_ans < minimum):
        max_ans = minimum
        max_ind = min_ind
    minimum = sys.maxint
    for i in range(0,len(arr)):
        if (abs(arr[i] - q) < minimum):
            minimum = abs(arr[i] - q)
            min_ind = q
    if (max_ans < minimum):
        max_ans = minimum
        max_ind = min_ind
    for i in range(1,len(arr)):
        mid=(arr[i]+arr[i-1])//2
        minimum = sys.maxint
        if (mid > p and mid < q):
            if (abs(arr[i] - mid) < minimum):
                minimum =abs(arr[i] - mid)
                min_ind = mid
            
            if (abs(arr[i - 1] - mid) < minimum):
                minimum = abs(arr[i - 1] - mid)
                min_ind = mid
            
            if (max_ans < minimum):
                max_ans = minimum
                max_ind = min_ind
            
    return max_ind


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    pq = raw_input().split()

    p = int(pq[0])

    q = int(pq[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
