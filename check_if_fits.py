#!/usr/local/bin/python3.7


def check_if_fits(piece, right=False, down=False ):
    if not down:
        if (piece[0][1] + right[1][0]) == 0:
            return True
        return False
    if not right:
        if (piece[1][1]+down[0][0]) == 0:
            return True
        return False
    if check_if_fits(piece,False,down):
        if check_if_fits(piece,right,False):
            return True
    return False
