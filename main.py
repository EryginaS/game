import pygame
pygame.init() # init lib
win = pygame.display.set_mode((500, 500))  # размеры окна

#  создаем героя (квадрат) и учимся его двигать
# заголовок
pygame.display.set_caption("Cubes game")

# нужно создать минимум 5 переменных: положение героя, ширина и высота игрока и скорость
x = 50
y = 425

width = 40
height = 60
speed = 5

is_jump = False # прыгает или нет
jump_count = 10
# В любом приложении, которое пишется на pygame нам нужно создавать цикл
# В цикле мы проверяем все действия пользователя

run= True

while run:
    pygame.time.delay(50) # кол во мс через кот будет выполнятся цикл

#   мы можем отслеживать события с помощью цикла, и у нас все события хратся в массиве
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # все нажимаемые клавиши
    # отслеживаем
    if keys[pygame.K_LEFT] and  x > 5:
        x -=speed
    if keys[pygame.K_RIGHT] and x < 500-width-5:
        x +=speed
    if not is_jump:
        if keys[pygame.K_UP] and y > 5:
            y -=speed
        if keys[pygame.K_DOWN] and y < 450-height -15:
            y +=speed
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            #     прыгаем 
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            # закончили прыжок
            is_jump = False
            jump_count = 10
    #  чтобы не рисовать
    win.fill((0,0,0))
    # персонаж (окно, цвет и характеристики)
    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update() # чтобы видеть изменения окна


pygame.quit()





