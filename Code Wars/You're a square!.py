def is_square(n):
    if n>=0:
        sq = n**0.5
        mod = sq%1
        return mod == 0
    else:
        return False