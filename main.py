import pygame
from time import sleep, gmtime, time, strftime
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 750))
clock = pygame.time.Clock()
colour = (211, 211, 211)
main_screen = False
run_1 = 1
next = False
Qn = ''
ab = 0
Qn_success = False
Ql = 0
sp = False
home_screen = 1
run = 1
text_ = ''
pygame.font.init()
font = pygame.font.SysFont('Microsoft YaHei ', 60)
font1 = pygame.font.SysFont('Microsoft YaHei Light', 120)
text_display = font1.render('', 1, (0, 255, 0))
text_displays = font.render('Enter the number questions', 1, (0, 0, 255))
timmer = 0
start_time = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        elif event.type == pygame.KEYDOWN:
            if main_screen:
                if event.key == pygame.K_SPACE:
                    sp += True
                    Ql += 1
                    start_time -= timmer % 144
                    mixer.Sound('ting_ding.wav').play()
            elif home_screen:
                if event.key == pygame.K_BACKSPACE:
                    text_ = text_[0:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    ab = int(text_)
                    home_screen = 0
                    main_screen = 1
                elif event.key == pygame.K_DELETE:
                    text_ = ''
                else:
                    text_ += event.unicode
                text_display = font1.render(text_, 1, (0, 0, 0))

    if home_screen:
        screen.fill((255, 255, 255))
        screen.blit(text_displays, (0, 50))
        screen.blit(text_display, (150, 360))
    elif main_screen:
        screen.fill(colour)
        timr = 144 * int(ab)
        if run_1 == 1:
            start_time = time()
            run_1 += 1

        current_time = time()

        stop_time = start_time + timr
        timmer = stop_time - current_time

        actual_time = strftime("%H:%M:%S", gmtime(timmer))
        text_time = pygame.font.SysFont('microsoft yahei Light', 100).render(
            (actual_time), False, (0, 0, 0))
        screen.blit(text_time, (250, 300))
        screen.blit(
            pygame.font.SysFont('microsoft yahei Light', 100).render(
                (str(Ql)), False, (0, 0, 0)), (375, 400))

        if int(timmer) % 144 == 0 and int(timmer) != 0 and Ql != ab:
            mixer.Sound('ting_ding.wav').play()
            Ql += 1

        if timmer <= 0 or Ql == ab:
            mixer.Sound('ting_ting_ting_ting.wav').play(-1)
            sleep(8)
            run = 0
        write_time = ''
    pygame.display.update()
    clock.tick(100)

pygame.quit()
