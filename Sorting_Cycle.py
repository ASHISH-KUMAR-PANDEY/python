def swap(i,j,lst):
  lst[i], lst[j] = lst[j], lst[i]
  return lst

def cycle_length(lst, n):
  i=0
  correct_index = sorted(lst).index(n)
  while(lst.index(n) != correct_index):
    cur = lst.index(n)
    lst = swap(cur, correct_index, lst)
    n = lst[cur]
    correct_index = sorted(lst).index(n)
    print(lst)
    i+=1
  return i
