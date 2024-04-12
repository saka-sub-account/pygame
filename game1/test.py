
import pygame
import sys

pygame.init()



# ウィンドウの設定をする
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# いろの定義
BLACK = (0, 0, 0)

# 画像の読み込み
player_image = pygame.image.load('/Users/yuta/Downloads/pygame_test6/game1/samurai.png')  # キャラクター画像を読み込む
player_size = player_image.get_size()  # 画像のサイズを取得
player_x = screen_width // 2 - player_size[0] // 2
player_y = screen_height - player_size[1]
player_velocity = 3
player_jump = False
player_jump_height = 10

# メインゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー操作を検出
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_velocity:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size[0] - player_velocity:
        player_x += player_velocity
    if not player_jump:
        if keys[pygame.K_SPACE]:
            player_jump = True
    else:
        if player_jump_height >= -10:
            neg = 1
            if player_jump_height < 0:
                neg = -1
            player_y -= (player_jump_height ** 2) * 0.5 * neg
            player_jump_height -= 1
        else:
            player_jump = False
            player_jump_height = 10

    # 画面のクリア
    screen.fill(BLACK)

    # プレイヤーの描画
    screen.blit(player_image, (player_x, player_y))  

    # 画面の更新
    pygame.display.flip()
    pygame.time.Clock().tick(30)
