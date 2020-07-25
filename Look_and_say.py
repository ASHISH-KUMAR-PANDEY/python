def look_and_say_term(term):
    ans = ""
    last = term[0]
    cnt = 1
    for cur in term[1:]:
        if last == cur:
            cnt += 1
        else:
            ans += str(cnt) + last
            cnt = 1
        last = cur
    ans += str(cnt) + last
    return int(ans)

def look_and_say(start, n):
    cur = start
    ans = [cur]
    while len(ans) < n:
        cur = look_and_say_term(str(cur))
        ans.append(cur)
    return ans
