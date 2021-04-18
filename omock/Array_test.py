import numpy as np
# board_array = np.ones((24,24))
array_no = 1

board_array= np.array([
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0,10, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0,10, 0,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     #0  1  2  3  4  5  6  7  8  9  *  1  2  3  4  5  6  7  8  9  *  1  2  3
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


qq = 13
ww = 10
print('현 위치 숫자 : ', board_array[qq, ww])

# 오목 완성 여부 판단 : 상,하,좌,우,대각선 4방향 검토
def board_decision(row, col):
    sum_array = 0
    # 수직 계산
    for row_temp in range(row - 5, row + 6):
        if board_array[row_temp, col] == array_no:
            sum_array += board_array[row_temp, col]
        elif sum_array == array_no * 5:
            return sum_array
        else:
            sum_array = 0


    # 수평  계산
    sum_array = 0   
    for col_temp in range(col - 5, col + 6):
        if board_array[row, col_temp] == array_no:
            sum_array += board_array[row, col_temp]
        elif sum_array == array_no * 5:       # 오목 (연속 5개 같은 돌) 나오면
            return sum_array
        else:
            sum_array = 0 

    # 북서- 남동 방향 계산
    sum_array = 0
    temp_row = row - 5 
    for col_temp in range(col - 5, col + 6):
        if board_array[temp_row, col_temp] == array_no:
            sum_array += board_array[temp_row, col_temp]
        elif sum_array == array_no *  5:
            return sum_array
        else:
            sum_array = 0
        temp_row += 1

    # 남서 - 북동 방향 계산
    sum_array = 0
    temp_row = row + 5 
    for col_temp in range(col - 5, col + 6):
        if board_array[temp_row, col_temp] == array_no:
            sum_array += board_array[temp_row, col_temp]
        elif sum_array == array_no * 5:
            return sum_array
        else:
            sum_array = 0
        temp_row -= 1

    return sum_array

sum_array = board_decision(qq,ww)
if sum_array == array_no * 5:
    print(sum_array, '오목 완성')
else:
    print(sum_array)