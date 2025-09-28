import pygame
import sys
import random
import time

# 初始化 Pygame
pygame.init()
pygame.mixer.init() # 初始化音效模組

# 遊戲視窗設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('貪食蛇')

# 載入音樂與音效
# 請確認你有 background.mp3 和 eat.wav 檔案在同一個資料夾
try:
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)  # -1 表示無限循環播放
    eat_sound = pygame.mixer.Sound('eat.wav')
except pygame.error as e:
    print(f"無法載入音效檔案: {e}")
    eat_sound = None

# 顏色設定
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 蛇的設定
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15
direction = 'RIGHT'
change_to = direction

# 食物設定
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
food_spawn = True

# 分數設定
score = 0
level = 1
next_level_score = 50

# 遊戲時脈
clock = pygame.time.Clock()

# 分數顯示函式
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score : {score}  Level : {level}', True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

# 遊戲結束函式
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# 遊戲主迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 鍵盤事件
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # 避免蛇直接反向
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # 移動蛇
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # 蛇的身體增長
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        if eat_sound:
            eat_sound.play()
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True


    # 填充背景色
    screen.fill(black)

    # 畫出蛇
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # 畫出食物
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # 遊戲結束判斷
    if snake_pos[0] < 0 or snake_pos[0] > screen_width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > screen_height-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # 顯示分數
    show_score(1, white, 'times new roman', 20)

    # 更新螢幕
    pygame.display.update()
    
    # 等級系統：根據分數提升速度
    if score >= next_level_score:
        level += 1
        snake_speed += 2
        next_level_score += 50

    # 控制遊戲速度
    clock.tick(snake_speed)
