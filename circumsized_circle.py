def square_areas_difference(r):
    length_big_square = 2 * r
    area_big_square = (2 * r)  ** 2
    area_small_square = r**2 + r**2
    return area_big_square - area_small_square
