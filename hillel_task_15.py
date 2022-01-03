#sqrt(x) = x^0.5

def distance(x1, y1, x2, y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**.5
    return(dist)

print(distance(4, 5, 6, 8))