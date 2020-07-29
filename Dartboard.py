def make_dartboard(n):

  board = []
  highest = 1
  for num in range(int(n/2)+1):
    row = []
    score = 1
    d = highest - 1
    for numb in range(n):
      row.append(str(score))
      if score < highest:
        score += 1
    
    for numb in range(1, 1+d):
      row[-numb] = str(0 + numb)
    board.append(int(''.join(row)))
    highest += 1
  
  if n%2!=0:
    return board + list(reversed(board[:-1]))
  else:
    return board + list(reversed(board[:-2]))
