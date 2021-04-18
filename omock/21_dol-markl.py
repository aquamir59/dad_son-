# 흑돌 백돌 번갈아 표시 및 배열에 데이터 입력

import pygame
import os
from PIL import Image
import time
import numpy as np

pygame.init()

pygame.mouse.set_visible(True)  # 마우스 포인트 보이기 or 안 보이기

# 화면 크기 설정
screen_width = 1030
screen_height = 1030
screen = pygame.display.set_mode((screen_width, screen_height))

# 오목판을 계산할 배열 생성
board_array = np.zeros((19,19))

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

screen.blit(bg,(0,0))
pygame.display.update() 

# 이벤트 루프
running = True
black_or_white = True       # True : black,  False  : white
while running:

    clock.tick(10)       # 초당 화면 새로 보여주는 횟수 5 -> 초당 5번 화면 update
    # 흑돌과 백돌 번갈아가면 둘수 있게
    if black_or_white:      # 돌이 black인 경우
        mark_color = mark_black
        doll_color = doll_black
        array_no = 1        # 배열에 들어갈 검은돌 숫자
    else:                   #  돌이 white인 경우
        mark_color = mark_white
        doll_color = doll_white
        array_no = 2        # 배열에 들어갈 흰색돌 숫자

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
        
        # 배열에 클릭 위치의 숫자 변경
        if board_array[array_height_row, array_width_col]  == 0:
            board_array[array_height_row, array_width_col]  = array_no
            # print('번호 : ',array_no, 'True or ', black_or_white)
            black_or_white = not black_or_white     # 돌 교체
        # else:
        #     print('이미 돌이 있습니다.')

    # 화면 표시  : 오목판 -> 바둑돌 모양 -> 마우스 현재 위치
    screen.blit(bg,(0,0))

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
pygame.quit()

print(board_array)