import math

def encryption(txt):
    txt = txt.replace(' ', '')
    n = len(txt)
    r = int(math.sqrt(n))
    if r**2 == n:
        # n is a perfect square:
        rows, cols = r, r
    else:
        rows = r
        cols = r + 1
        if rows * cols < n:
            rows, cols = r + 1, r + 1
    table = []
    while len(txt) > 0:
        table.append(txt[:cols])
        txt = "" if len(txt) <= cols else txt[cols:] 
    while len(table[-1]) < cols:
        table[-1] += ' '
    cipher = ""
    for col in range(cols):
        for row in range(rows):
            cipher += table[row][col] if table[row][col] != ' ' else ''
        cipher += ' '
    return cipher.strip()
