# pygame에서 버튼 모양 만들고 제어하는 프로그램

import pygame
from sys import exit as _exit
import time
# pygame에서 button 제어

# board class
class PG_Widnow_UI:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        # pygame.display.set_caption('[ 오 목 ]')

    def update(self):
        pygame.display.flip()

    def clear(self, r, g, b):
        self.window.fill((r, g, b))

    def close(self):
        pygame.quit()
        _exit()

# event 중 quit  처리
def handleEvents(events):
    for event in events:
        if event.type == pygame.QUIT:
            pg_window.close()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if point_in(mousePos[0], mousePos[1], 200, 50, 1050, 800):
            # if point_in(mousePos[0], mousePos[1], self.size[0], self.size[1], self.position[0], self.position[1]):
                print('button-retry')

# 클릭 위치가 버튼 안쪽 여부 체크
def point_in(point_x, point_y, rec_w, rec_h, rec_x, rec_y):
    if point_x > rec_x and point_x < rec_x + rec_w and point_y > rec_y and point_y < rec_y + rec_h:
        return True
    return False

# button 저의
class button:
    def __init__(self, text:str, position: tuple, size:tuple=(130,50), outline:bool=True):
        self.position = position
        self.size = size
        self.button = pygame.Surface(size).convert()        # 버튼 내 색 정의 위한 작업(?)
        self.button.fill((255, 0, 0))                           #  버튼 내 색 정의
        self.outline = outline

        font = pygame.font.SysFont('a시네마b',25)      # 폰트 지정, 크기 지정
        self.textsurf = font.render(f'{text}', True, (255,255,255))                         # 문자의 내용과 색 정의

    # 클릭 시 작업
    def clicked(self, events):
        mousePos = pygame.mouse.get_pos()
        # button 범위 내에 있는지 체크
        if point_in(mousePos[0], mousePos[1], self.size[0], self.size[1], self.position[0], self.position[1]):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False
    # 버튼 정의, 보여주기.  display : ?????
    def render(self, display):
        # 문자 위치
        text_x = self.position[0] + (self.button.get_rect().width/2) - (self.textsurf.get_rect().width/2)
        text_y = self.position[1] + (self.button.get_rect().height/2) - (self.textsurf.get_rect().height/2)

        display.blit(self.button, (self.position[0], self.position[1]))       # 버튼 바탕색 display
        display.blit(self.textsurf, (text_x, text_y))                           # 버튼내 문자 display

        # 버튼 외곽선
        if self.outline:
            thickness = 4
            pos_x = self.position[0] - thickness           #  pos_x, pos_y : 좌상 위치
            pos_y = self.position[1] - thickness
            size_x = self.size[0] + thickness * 2            #  size_x, size_y : 우하 위치
            size_y = self.size[1] + thickness * 2
            pygame.draw.rect(display, (255, 0, 0), (pos_x, pos_y, size_x, size_y), thickness)

######################################################
window_width = 1350
window_height =1000
pg_window = PG_Widnow_UI(window_width, window_height)

# 버튼 갯수
number_of_buttons = 5
# buttons = [button(f'버튼 {i}', ((120 * (i % 5) + 10), ((i % 5) * 70) + 10)) for i in range(number_of_buttons)]
button_retry = button('종  료',((1050, 800)))

pg_window.clear(255, 255, 255)
while True:
    events = pygame.event.get()
    # 종료 클릭 여부 확인
    handleEvents(events)

    button_retry.render(pg_window.window)
    # for button in buttons:
    #     button_retry.render(pg_window.window)
    #     if button.clicked(events):
    #         print(f'button at position : {button.position} was clicked')

    pg_window.update()
