#  마우스 위치 표시 및 돌 오목판에 표시

import pygame
import os
from PIL import Image
import time
import numpy as np

pygame.init()

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
select_black = pygame.image.load(os.path.join(image_path, "select1.png"))

# 바둑알 가져오기
doll_black = pygame.image.load(os.path.join(image_path, "doll_black.png"))

screen.blit(bg,(0,0))
pygame.display.update() 

# 이벤트 루프
running = True  
while running:
    clock.tick(60)       # 초당 화면 새로 보여주는 횟수 5 -> 초당 5번 화면 update
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
        array_width = (int((mouse_pos[0] - 40) / 50)) 
        array_height = (int((mouse_pos[1] - 40) / 50)) 

        # 배열에 클릭 위치의 숫자 변경
        board_array[array_height, array_width]  = 1

    # 마우스 현재 위치 표시하는 넓은 사각형 표시    
    # : int((y_pos+10) / 50) 나온 결과 -> (결과 * 50 - 10)
    mouse_width = (int((mouse_pos[0] + 10) / 50)) * 50 - 10
    mouse_height = (int((mouse_pos[1] + 10) / 50)) * 50 - 10

    # 화면 표시  : 오목판 -> 바둑돌 모양 -> 마우스 현재 위치
    screen.blit(bg,(0,0))

    # board_array에 있는 자료로 화면에 돌 표시
    for i in range(19):
        for j in range(19):
            if board_array[i,j] > 0:            #  배열에 숫자가 있으면 (돌이 놓여 있으면)
                array_width = i * 50 + 41
                array_height = j * 50 + 41
                screen.blit(doll_black,(array_height, array_width))

    screen.blit(select_black,(mouse_width,mouse_height))
            

    pygame.display.update() 

# pygame 종료
pygame.quit()

print(board_array)