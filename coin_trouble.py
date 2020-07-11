def coins_div(lst):
    if len(lst) < 3 or sum(lst)%3 != 0:
        return False
    lst.sort(reverse=True)
    groups = [sum(lst)//3]*3
    return depth_first_search(lst, 0, groups)
        
def depth_first_search(lst, idx, groups):
    if idx == len(lst):
        return True
    for i in range(3):
        if groups[i] >= lst[idx]:
            groups[i] -= lst[idx]
            if depth_first_search(lst, idx+1, groups):
                return True
            groups[i] += lst[idx]
    return False
