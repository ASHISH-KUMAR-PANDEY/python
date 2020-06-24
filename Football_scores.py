def tournament_scores(lst):
    d = {'A': [0, 0, 0], 'B': [0, 0, 0], 
         'C': [0, 0, 0], 'D': [0, 0, 0]}

    for game in lst:        
        home, home_score = game[0], int(game[2])
        away, away_score = game[-1], int(game[-3])
        
        d[home][1] += home_score
        d[away][1] += away_score
        d[home][2] += home_score - away_score
        d[away][2] += away_score - home_score

        if home_score > away_score:
            d[home][0] += 3
        elif home_score < away_score:
            d[away][0] += 3
        else:
            d[home][0] += 1
            d[away][0] += 1

    res = [[k] + v for k, v in d.items()]
    res.sort(key=lambda x: x[1:], reverse=True)
    return res
