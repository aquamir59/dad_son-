import numpy as np

three_serial = [[0, 1, 1, 1, 0],[0, 10, 10, 10, 0]]
three_gap = [[0, 1, 0, 1, 1, 0],[0, 1, 1, 0, 1, 0]]

array = np.array([[0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 #0  1  2  3   4  5  6  7  8  9  *  1  2  3  4  5  6  7  8  9
                [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
col_no = 9
row_no = 0
col_no  = col_no - 3
black_ = 0
three_check = False

# 연속 이어진 3을 체크
for i in range(0,3):
    chk_no = col_no + i
    for j in range(0,5):
        if array[row_no, chk_no] != three_serial[black_][j]:
            break
        else:
            three_check = True
            chk_no += 1
            
            
    if three_check == True:
        break

if not  three_check:
    중간에 갭이 발생한 3 체크
    col_no -= 1
    for i in range(0,4):
        chk_no = col_no + i
        for j in range(0,6):
            if array[row_no, chk_no] == three_gap[black_][j]:
                break
            else:
                three_check = True
                chk_no += 1

        if three_check == True:
            break


    # print(i)

print(three_check)