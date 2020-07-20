def line(p1, p2, point3, test_point):
    x = point3[0]
    m = (p2[1] - p1[1]) / (p2[0]-p1[0])
    y = m * (x - p1[0]) + p1[1]
    if point3[1] > y:
        string =  'greater'
    else:
        string ='less'
    if string == 'greater':
        return m * (test_point[0] - p1[0]) + p1[1] < test_point[1]
    else:
        return m * (test_point[0] - p1[0]) + p1[1] > test_point[1]
def within_triangle(p1, p2, p3, test):
    sorted_ordered_pair = sorted([p1, p2, p3])
    return line(p1, p2, p3, test) and line(p1, p3, p2, test) and line(p2, p3, p1, test)    
within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2))
