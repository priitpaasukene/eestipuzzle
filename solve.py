#!/usr/local/bin/python3.7

import numpy as np

from check_if_fits import check_if_fits

def rotate(a):
    rotated=[[a[0][1],a[1][1]],[a[0][0],a[1][0]]]
    return rotated

def printfield(field):
    print('current field:', end=' ')
    print(field)

def printunused(unused):
    print('unused blocks:', unused.__len__(),end=' ')
    print(unused)

def checkblock_right(current_block,new_block):
    found=False
    for a in 0,1,2,3:
        if check_if_fits(current_block,new_block):
            found=True
            found_block=new_block
            break
        new_block=rotate(new_block)
    if found:
        return new_block
    else:
        return False


# Our building blocks
blocks=[
    [[-1,1],[2,4]],
    [[-1,3],[4,2]],
    [[3,2],[-4,-2]],
    [[-4,2],[1,-3]],
    [[-1,-3],[-4,2]],
    [[-1,3],[-3,4]],
    [[-2,4],[1,-3]],
    [[-2,3],[4,-1]],
    [[4,-1],[-2,3]]
]

# Empty playing field.
field=[ [[],[],[]],
        [[],[],[]],
        [[],[],[]]
        ]

#Solving logic:
# 1. place first piece in corner (iterate over all pieces)
# 2. start from first available piece: match it to right
# if fail, rotate piece up to 3 times trying again
# if still fail, put piece back, take next piece.
# if no match found, return to 1.
# If match found:
# 3. start from first available piece: match it down
# rotate up to 3 times
# if match found, place piece.

for start in range(0,9):
    print('start block:',start)
    unused_blocks=blocks
    printfield(field)
    printunused(unused_blocks)

    current_block=unused_blocks.pop(start)
    field[0][0]=current_block
    maxrow=field.__len__()-1
    maxcol=field[0].__len__()-1
    for row in range(0,field.__len__()):
        print('row:',row, end=' ')
        for col in range(0,field[row].__len__()-1):
            print('col:',col, end=' ')
            tried_blocks=0
            #try block to right
            if row<maxrow:
                while tried_blocks<unused_blocks.__len__():
                    current_block=unused_blocks.pop(0)
                    tried_blocks+=1
                    print('cheking fit:',field[row][col],'with',current_block)
                    found=False;

                    if found and col<maxcol:
                        print(row+1,',',col,' populated with:', found_block)
                        field[row][col+1]=found_block
                        printfield(field)
                        break
                    else:
                        unused_blocks.append(current_block)
                        print('blocks available:',unused_blocks.__len__())



    # free start block
