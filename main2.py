import pygame
pygame.init() # init lib
win = pygame.display.set_mode((500, 500))  # размеры окна

#  создаем героя (квадрат) и учимся его двигать
# заголовок
pygame.display.set_caption("Cubes game")
#  загрузка изображений
walk_right = [pygame.image.load('game_img/right_1.png'), pygame.image.load('game_img/right_2.png'), pygame.image.load('game_img/right_3.png'),
              pygame.image.load('game_img/right_4.png'), pygame.image.load('game_img/right_5.png'), pygame.image.load('game_img/right_6.png')]
walk_left = [pygame.image.load('game_img/left_1.png'), pygame.image.load('game_img/left_2.png'), pygame.image.load('game_img/left_3.png'),
              pygame.image.load('game_img/left_4.png'), pygame.image.load('game_img/left_5.png'), pygame.image.load('game_img/left_6.png')]
playerStand = pygame.image.load('game_img/idle.png')
bg = pygame.image.load('game_img/pygame_bg.jpg')
# нужно создать минимум 5 переменных: положение героя, ширина и высота игрока и скорость
x = 50
y = 425

width = 60
height = 71
speed = 5

is_jump = False # прыгает или нет
jump_count = 10
# В любом приложении, которое пишется на pygame нам нужно создавать цикл
# В цикле мы проверяем все действия пользователя

left = False
right = False
anim_count = 0
clock = pygame.time.Clock()

def draw_window():
    #  чтобы не рисовать
    global anim_count
    #  рамки списка
    win.blit(bg, (0, 0)) # картинка и старт
    if anim_count + 1 >=30:
        anim_count = 0
    # шагаем влево что рисуем и где
    if left:
        win.blit(walk_left[anim_count // 5], (x,y))
        anim_count+=1
    elif right:
        win.blit(walk_right[anim_count // 5], (x,y))
        anim_count +=1
    else:
        win.blit(playerStand, (x,y))

    pygame.display.update()  # чтобы видеть изменения окна

run= True
while run:
    clock.tick(30)
    # pygame.time.delay(50) # кол во мс через кот будет выполнятся цикл

#   мы можем отслеживать события с помощью цикла, и у нас все события хратся в массиве
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # все нажимаемые клавиши
    # отслеживаем
    if keys[pygame.K_LEFT] and  x > 5:
        x -=speed
    #     двигаемся влево
        left =True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500-width-5:
        x +=speed
        right = True
        left = False
    else:
        left = False
        right = False
        anim_count = 0

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
    draw_window()
pygame.quit()
