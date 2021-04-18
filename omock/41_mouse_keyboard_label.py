# 메뉴 (계속 게임, quit) 표시 및 작동

from tkinter import *
import pygame
import os
import time
import numpy as np

# 시작전 돌 놓은 방법으로 마우스와 키보드 선택하는 화면
root = Tk()
root.title("오목 도구 선정")
root.geometry("640x480")

option_1 = {'font': ('a시네마b', 18)}       #  라벨 폰트
option_2 = {'font': ('a시네마m', 15)}       #  버튼 폰트

# 흑돌 라벨 및 Radio button
label_black = Label(root, text="흑돌 선택", width=10, height=1, fg='black', bg='#9d9d9d',
                    borderwidth = 4, relief="raised", **option_1)
label_black.place(x=150, y=100, width=120, height=60) 
black_var = StringVar()
btn_black1 = Radiobutton(root, text="마우스", value ='마우스', variable= black_var, width =10, height =1, 
                        bg='#00ffff', **option_2)
btn_black2 = Radiobutton(root, text="키보드", value ='키보드', variable= black_var, width =10, height =1,
                        bg='#28ff28', **option_2)
btn_black1.select()

btn_black1.place(x=300, y=90)
btn_black2.place(x=300, y=130)
Label(root, text=':  방향키 + Enter 사용').place(x=438, y=133)

# 백돌 라벨 및 Radio button
lable_white = Label(root, text="백돌 선택", width=10, height=1, fg='#ffffff', bg='#9d9d9d',
                    borderwidth = 4, relief="raised", **option_1)
lable_white.place(x=150, y=220, width=120, height=60) 
white_var = StringVar()
btn_white1 = Radiobutton(root, text="마우스", value ='마우스', variable= white_var, width =10, height =1, 
                        bg='#00ffff', **option_2)
btn_white2 = Radiobutton(root, text="키보드", value ='키보드', variable= white_var, width =10, height =1,
                        bg='#28ff28', **option_2)
btn_white2.select()

btn_white1.place(x=300, y=210)
btn_white2.place(x=300, y=260)
Label(root, text=':  방향키 + Enter 사용').place(x=438, y=263)

def btncmd():
    root.destroy()
    print(black_var.get())
    print(white_var.get())

btn = Button(root, text="클릭", bg='#eeffee',  **option_1, command = btncmd)
btn.place(x=235, y=320, width=110, height=40)

root.mainloop()

#############################
#   게임 시작
########################
pygame.init()
pygame.mouse.set_visible(True)  # 마우스 포인트 보이기 or 안 보이기

# 흑돌과 백돌 교체에 따른 변수 변경
def doll_change(black_or_white):
    global mark_color, doll_color, array_no
    if black_or_white:      # 돌이 black인 경우, 배열에 들어갈 숫자 : 1  
        mark_color = mark_black
        doll_color = doll_black
        array_no = 1        
    else:                   #  돌이 white인 경우, 배열에 들어갈 숫자 : -1 
        mark_color = mark_white
        doll_color = doll_white
        array_no = -1    

# 오목 완성 여부 판단 : 상,하,좌,우,대각선 4방향 검토
def board_decision(row, col):
    sum_array = 0
    # 기준 돌 좌와 우 같이 검토, 육목 확인하기 위해 기준점 대비 양쪽 5개씩 검사
    # 수직 계산
    for row_temp in range(row - 5, row + 6):        
        if board_array[row_temp, col] == array_no:      # 같은 돌인 경우    
            sum_array += board_array[row_temp, col]
        elif sum_array == array_no * 5:                 #  육목 체크
            return sum_array
        else:                                           # 연속 같은 돌 아닌 경우
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

    return sum_array   # 결과값 송부 (오목이 아닌 경우)
#  =================================================

# 화면 크기 설정
screen_width = 1218
screen_height = 1030
screen = pygame.display.set_mode((screen_width, screen_height))

# 오목판을 계산할 배열 생성
board_array = np.zeros((24,24))     #   오목판은 19,19 이지만 승패 판단을 위해 추가로 +5 넓게 만듬 (육목 확인용 포함)
                        #  맨 끝에 위치한 (19번 줄) 경우 연달아 동일 색 5개를 확인하려면 배열 밖으로 나가 에러 발생
                        #  배열 밖인지 아닌지 따지는 식 만들기 싫어서 배열 크기를 넓히는 방법 사용
# 화면 타이틀 설정
pygame.display.set_caption('[ 오 목 ]')
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
baduk_board = pygame.image.load(os.path.join(image_path, "game_board.png"))

# 마우스 위치 표시 이미지 가져오기
mark_black = pygame.image.load(os.path.join(image_path, "select1.png"))
mark_white = pygame.image.load(os.path.join(image_path, "select2.png"))

# 바둑알 가져오기
doll_black = pygame.image.load(os.path.join(image_path, "doll_black.png"))
doll_white = pygame.image.load(os.path.join(image_path, "doll_white.png"))

# 판정 (흑승, 백승) 가져오기
win_black = pygame.image.load(os.path.join(image_path, "win_black.png"))
win_white = pygame.image.load(os.path.join(image_path, "win_white.png"))

# 메뉴 가져오기
menu_more = pygame.image.load(os.path.join(image_path, "menu_more.png"))
menu_quit = pygame.image.load(os.path.join(image_path, "menu_quit.png"))


# 이벤트 루프
# screen.blit(baduk_board,(0,0))
# pygame.display.update() 

running = True
black_white = True       # True : black,  False  : white
result_decision = 0         # 오목 여부 확인 변수
doll_change(black_white)

while running:
    # 화면 표시  : 오목판 -> 메뉴 -> 마우스 현재 위치 -> 바둑돌 모양   -> 결과 표시
    screen.blit(baduk_board,(0,0))
    screen.blit(menu_more,(1050,600))
    screen.blit(menu_quit,(1050,750))
    clock.tick(60)       # 초당 화면 새로 보여주는 횟수 5 -> 초당 5번 화면 update

    mouse_pos =pygame.mouse.get_pos()           # 오목판 마우스 위치 

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    # 메뉴 마우스 클릭시
    if event.type == pygame.MOUSEBUTTONDOWN:
        # more button : width : 1050 ~ 1190, 600 ~ 660
        if 1050 <= mouse_pos[0] <= 1190 and 600 <= mouse_pos[1] <= 660:
            # 초기화 : 배열 0으로, 승패 판단 x, .흑돌로 시작
            board_array = np.zeros((24,24))
            result_decision = 0
            black_white = True
            doll_change(black_white)
            
        # quit button : width : 1050 ~ 1201, 750 ~ 817
        if 1050 <= mouse_pos[0] <= 1190 and 750 <= mouse_pos[1] <= 810:
            running = False

# # event를 get으로 얻는 경우, 위는 poll로 얻는 경우
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # 메뉴 마우스 클릭시
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # more button : width : 1050 ~ 1190, 600 ~ 660
#             if 1050 <= mouse_pos[0] <= 1190 and 600 <= mouse_pos[1] <= 660:
#                 # 초기화 : 배열 0으로, 승패 판단 x, .흑돌로 시작
#                 board_array = np.zeros((24,24))
#                 result_decision = 0
#                 black_white = True
#                 doll_change(black_white)
                
#             # quit button : width : 1050 ~ 1201, 750 ~ 817
#             if 1050 <= mouse_pos[0] <= 1190 and 750 <= mouse_pos[1] <= 810:
#                 running = False

    # 판에 돌을 놓을 경우 작업 : 배열에 값 입력, 오목 여부 판단
            # 게임 중에는 오목 판에서만 마우스 작동하도록 :  x, y 축 ( 커서 허용 범위 : 40   ~  989 ) 
            # 마우스가 오목판안에서만 작동 and  결과가 나면 작동 안 하도록 (result_decision == 5)
    if mouse_pos[0] >= 40 and mouse_pos[0] < 990 and mouse_pos[1] >= 40 and mouse_pos[1] < 990 \
        and abs(result_decision) != 5 :
        
        # 마우스 클릭시 해당 돌을 배열에 입력
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # 마우스의 포지션을 받아서 배열을 수정
            array_width = (int((mouse_pos[0] - 40) / 50)) 
            array_height = (int((mouse_pos[1] - 40) / 50)) 
            
            # 배열내 클릭 위치에 숫자 입력
            if board_array[array_height, array_width]  == 0:
                board_array[array_height, array_width]  = array_no

                # 오목 여부 확인
                result_decision = board_decision(array_height, array_width)

                # 흑돌과 백돌 교체 
                black_white = not black_white
                doll_change(black_white)

        # 마우스 현재 위치 표시하는 넓은 사각형 표시   
        # 먼저 해당 위치에 돌이 있는지 확인하기 위해서 배열을 체크 : 배열의 위치 확인
            # 이미 돌이 있는 경우에는 넓은 사각형 표시 안 하게 하는 프로그램 -> 안 사용하는 게 더 좋을 것 같음. 마지막 놓은 자리 표시하기 위해
                # array_width_col = (int((mouse_pos[0] - 40) / 50))     
                # array_height_row = (int((mouse_pos[1] - 40) / 50)) 

                # if board_array[array_height_row, array_width_col] == 0:
        # 넓은 사각형 표시할 위치 계산
        mouse_width_col = (int((mouse_pos[0] + 10) / 50)) * 50 - 10
        mouse_height_row = (int((mouse_pos[1] + 10) / 50)) * 50 - 10
        screen.blit(mark_color,(mouse_width_col, mouse_height_row))

    # board_array에 있는 자료로 화면에 돌 표시
    for i in range(19):
        for j in range(19):
            if board_array[i,j] != 0:            #  배열에 숫자가 있으면 (돌이 놓여 있으면)
                array_height_row = i * 50 + 41
                array_width_col = j * 50 + 41
                if board_array[i,j] == 1:            #  돌 색깔에 따라 1 이면 black, -1 이면 white
                    screen.blit(doll_black,(array_width_col, array_height_row))
                else:
                    screen.blit(doll_white,(array_width_col, array_height_row))

    # 오목이면 표시 : 화면 순서를 위해 맨 마지막으로 온 것 임.
    if result_decision == 5:                    # 흑 승
        screen.blit(win_black,(1055, 300))
    elif result_decision == -5:
        screen.blit(win_white,(1055, 300))

    pygame.display.update() 

# pygame 종료
pygame.time.delay(1000)     # 1초 대기
pygame.quit()