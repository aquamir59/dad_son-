# pygame에서 Radio Button 만들고 제어하기

import pygame

class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__() 
        text_surf = font.render(text, True, (0, 0, 0))
        # 선택 안 당한 상태의 button, 커서가 안 올라온 상태의 button
        self.button_image = pygame.Surface((w, h))
        self.button_image.fill((96, 96, 96))
        self.button_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        # 커서가 올라온 상태의 button
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill((96, 96, 96))
        self.hover_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (96, 196, 96), self.hover_image.get_rect(), 3)   # 버튼 외곽 색 : (96, 196, 96)
        # 선택이 되어진 상태의 button
        self.clicked_image = pygame.Surface((w, h))
        self.clicked_image.fill((96, 196, 96))
        self.clicked_image.blit(text_surf, text_surf.get_rect(center = (w // 2, h // 2)))
        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.buttons = None

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())  # 충돌 여부 확인 : 버튼 클릭여부
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover :
                # if hover and event.button == 1:
                    for rb in self.buttons:
                        rb.clicked = False
                    self.clicked = True
        
        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image


pygame.init()
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
font50 = pygame.font.SysFont(None, 50)

radioButtons = [
    RadioButton(50, 40, 200, 60, font50, "option 1"),
    RadioButton(50, 120, 200, 60, font50, "option 2"),
    RadioButton(50, 200, 200, 60, font50, "option 3")
]

for rb in radioButtons:
    rb.setRadioButtons(radioButtons)
    
radioButtons[0].clicked = True

group = pygame.sprite.Group(radioButtons)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    group.update(event_list)

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()