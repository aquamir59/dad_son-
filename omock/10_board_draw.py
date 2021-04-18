#  오목판 
import pygame
import os
from PIL import Image

pygame.init()

# 화면 크기 설정
screen_width = 1030
screen_height = 1030
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('[ 오 목 ]')
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
bg = pygame.image.load(os.path.join(image_path, "game_board.png"))

# 이벤트 루프
running = True  
while running:
    clock.tick(5)       # 초당 화면 새로 보여주는 횟수 5 -> 초당 5번 화면 update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 오목판 마우스 위치 표시
    mouse_pos =pygame.mouse.get_pos()
    print(mouse_pos[0], mouse_pos[1])

    screen.blit(bg,(0,0))
    pygame.display.update() 

# pygame 종료
pygame.quit()