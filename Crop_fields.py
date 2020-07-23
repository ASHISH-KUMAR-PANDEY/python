def crop_hydrated(arr):
    
    for x, i in enumerate(arr):
        for y, item in enumerate(i):

            if item != 'c':
                continue

            up = x != 0
            down = x != len(arr) - 1
            left = y != 0
            right = y != len(i) - 1
 
            if up:
                if arr[x-1][y] == 'w':
                    continue
            
            if down:
                if arr[x+1][y] == 'w':
                    continue
            
            if left:
                if arr[x][y-1] == 'w':
                    continue
            
            if right:
                if arr[x][y+1] == 'w':
                    continue
            
            if up and right:
                if arr[x-1][y+1] == 'w':
                    continue
            
            if up and left:
                if arr[x-1][y-1] == 'w':
                    continue
            
            if down and left:
                if arr[x+1][y-1] == 'w':
                    continue
            
            if down and right:
                if arr[x+1][y+1] == 'w':
                    continue
            
            return False
    return True
