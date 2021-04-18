# 오목 여부 판단

import pygame
import os
import time
import numpy as np

pygame.init()
pygame.mouse.set_visible(True)  # 마우스 포인트 보이기 or 안 보이기

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
bg = pygame.image.load(os.path.join(image_path, "game_board.png"))

# 마우스 위치 표시 이미지 가져오기
mark_black = pygame.image.load(os.path.join(image_path, "select1.png"))
mark_white = pygame.image.load(os.path.join(image_path, "select2.png"))

# 바둑알 가져오기
doll_black = pygame.image.load(os.path.join(image_path, "doll_black.png"))
doll_white = pygame.image.load(os.path.join(image_path, "doll_white.png"))

# 바둑알 가져오기
win_black = pygame.image.load(os.path.join(image_path, "win_black.png"))
win_white = pygame.image.load(os.path.join(image_path, "win_white.png"))


# 이벤트 루프
screen.blit(bg,(0,0))
pygame.display.update() 

running = True
black_or_white = True       # True : black,  False  : white
while running:
    # 화면 표시  : 오목판 -> 바둑돌 모양 -> 마우스 현재 위치  -> 결과 표시
    screen.blit(bg,(0,0))
    clock.tick(10)       # 초당 화면 새로 보여주는 횟수 5 -> 초당 5번 화면 update
    # 흑돌과 백돌 번갈아가면 둘수 있게
    if black_or_white:      # 돌이 black인 경우, 배열에 들어갈 숫자 : 1  
        mark_color = mark_black
        doll_color = doll_black
        array_no = 1        
    else:                   #  돌이 white인 경우, 배열에 들어갈 숫자 : 10 (2로 하면 연속 돌 계산 시 흑돌과 혼돈 초래)
        mark_color = mark_white
        doll_color = doll_white
        array_no = 10     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos =pygame.mouse.get_pos()           # 오목판 마우스 위치 
                                                # print(mouse_pos[0], mouse_pos[1])
                                                
    # 선택 돌이 화면 위치 안에서만 표시하도록
     # x, y 축 ( 커서 허용 범위 : 40   ~  989 ) 
    if mouse_pos[0] < 40 or mouse_pos[0]  >= 990 or mouse_pos[1] < 40 or mouse_pos[1] >= 990 :
        continue

    # 마우스 클릭시 해당 돌을 표시
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        # 마우스의 포지션을 받아서 배열을 수정
        array_width_col = (int((mouse_pos[0] - 40) / 50)) 
        array_height_row = (int((mouse_pos[1] - 40) / 50)) 
        
        # 배열내 클릭 위치에 숫자 입력
        if board_array[array_height_row, array_width_col]  == 0:
            board_array[array_height_row, array_width_col]  = array_no
            # 승패 판정
            result_decision = board_decision(array_height_row, array_width_col)
            if result_decision == 5:
                screen.blit(win_black,(1050, 300))
                print('흑돌 승')
                running = False
            elif result_decision == 50:
                screen.blit(win_white,(1050, 300))
                print('백돌 승')
                running = False

            black_or_white = not black_or_white     # 돌 교체 (black -> white)
        # else:
        #     print('이미 돌이 있습니다.')

    # board_array에 있는 자료로 화면에 돌 표시
    for i in range(19):
        for j in range(19):
            if board_array[i,j] > 0:            #  배열에 숫자가 있으면 (돌이 놓여 있으면)
                array_height_row = i * 50 + 41
                array_width_col = j * 50 + 41
                if board_array[i,j] == 1:            #  돌 색깔에 따라 1이면 black, 2이면 white
                    screen.blit(doll_black,(array_width_col, array_height_row))
                else:
                    screen.blit(doll_white,(array_width_col, array_height_row))

    # 마우스 현재 위치 표시하는 넓은 사각형 표시   
    # 먼저 해당 위치에 돌이 있는지 확인하기 위해서 배열을 체크 : 배열의 위치 확인
    array_width_col = (int((mouse_pos[0] - 40) / 50)) 
    array_height_row = (int((mouse_pos[1] - 40) / 50)) 

    if board_array[array_height_row, array_width_col] == 0:
        # 넓은 사각형 표시할 위치 계산
        mouse_width_col = (int((mouse_pos[0] + 10) / 50)) * 50 - 10
        mouse_height_row = (int((mouse_pos[1] + 10) / 50)) * 50 - 10
        screen.blit(mark_color,( mouse_width_col, mouse_height_row))

    pygame.display.update() 

# pygame 종료

# 2초 대기
pygame.time.delay(2000)
pygame.quit()