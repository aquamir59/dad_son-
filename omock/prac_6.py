import numpy as np

three_serial_black = np.array([0, 1, 1, 1, 0])
three_serial = [[0, 1, 1, 1, 0],[0, 10, 10, 10, 0]]
three_gap = [[0, 1, 0, 1, 1, 0],[0, 1, 1, 0, 1, 0]]

array = np.array([[0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 #0  1  2  3   4  5  6  7  8  9  *  1  2  3  4  5  6  7  8  9
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 10, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

row_no = 1
col_no = 5
col_no  = col_no - 4
end_no = col_no +5
black_ = 0
threethree_sum = 0
three_check = False
for i in range(0,3):
    col_no += 1
    print(row_no, col_no)
    aa = array[[row_no:col_no]: [row_no:end_no]]
    # aa = array[(row_no:col_no): (row_no:end_no)]
    # aa = array[(row_no,col_no): (row_no,end_no)]
    # aa = array[(row_no)(col_no): (row_no)(end_no)]
    # aa = array[[row_no][col_no]: [row_no][col_no+5]]
    # aa = array[[row_no,col_no]: [row_no + 5,col_no]]
    print(aa)
    if (aa == three_serial_black).all():
        three_check = True
        threethree_sum += 1
        break
    # else:
    #     three_check = False
    #     break

print(three_check)
