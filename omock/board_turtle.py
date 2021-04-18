import turtle as tt
import time

omock_board =  tt.Screen()
board_size = 1030
tt.setup(width=board_size, height=board_size)
tt.bgcolor("#ffd966")
# tt.shape('turtle')
tt.ht()
tt.speed(20)

# 외곽선 그리기
tt.penup()
# tt.goto((-500,500))   # 외곽선 위치로
tt.setpos(-500,500)
tt.pendown()
tt.pensize(2.5)

for i in range(4):
    tt.forward(1000)
    tt.right(90)

# v펜 두께는 선은 1.45  외곽은 2.5
tt.pensize(1.45)
x_pos = -450   # 내선 첫 위치
y_pos = 450
tt.penup()

# 가로선 그리기
for i in range(19):
    tt.setpos(x_pos,y_pos)
    tt.pendown()
    tt.forward(900)
    tt.penup()
    y_pos -= 50

# 세로선 그리기
x_pos = -450   # 내선 첫 위치
y_pos = 450
tt.right(90)
for i in range(19):
    tt.setpos(x_pos,y_pos)
    tt.pendown()
    tt.forward(900)
    tt.penup()
    x_pos -= -50

# 바둑판 점 그리기
list_1 = [-300,0,300]
for x_pos in list_1:
    for y_pos in list_1:
        tt.setpos(x_pos,y_pos)
        tt.dot(15)

# 마우스 해당 위치에 바둑알 그리기 위한 작업

    # if keyboard.is_pressed("Esc"):   # ESC 키로 마우스 위치 확정 작업 중지
    #     running = False

    # 마우스 위치 표시
    # s_column, s_row =pyautogui.position()
    # print('{0},{1}' .format(s_column,s_row))

    ####### 오목판에 마우스가 올라가면 마우스 모양이 동그라미로 변한다. *****************
    # if mouse.is_pressed("left"):             # 마우스 왼쪽 클릭이면
    #     pos = mouse.get_position()       # 현재 마우스 포인터 좌표
    #     print(pos)            
    #     running = False

    # if mouse.is_pressed("right"):             # 마우스 왼쪽 클릭이면
    #     break

    # if s_column <  0:       # 화면 벗어나면 작업 중지 : 임시 
    #     running = False

# 오목판에 마우스 위치 표시
def fxn(x, y):
    tt.goto(x, y)
    tt.write(str(int(x))+"  "+str(int(y)))

# onclick action 
omock_board.onclick(fxn)

# 마우스 위치를 바둑알 위치로 변경 식
# x 축 ( 커서 허용 범위 : -475   ~  475 ) : 맨 좌측이 -450
# : int((y_pos+24) / 50) 나온 결과 -> (결과 * 50 - 22) : x축은 -22
# y 축 ( 커서 허용 범위 : 475 ~ -475 ) : 맨 위가 450 
#   : int((y_pos+24) / 50) 나온 결과 -> (결과 * 50 + 22) : y축은 +22



tt.mainloop()