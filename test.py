import pygame
import sys

# pygameの初期化
pygame.init()

# ウィンドウの設定
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# カラー定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# プレイヤー設定
player_size = 50
player_x = screen_width // 2
player_y = screen_height - player_size
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

    # キー操作の検出
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_velocity:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size - player_velocity:
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
    screen.fill(WHITE)

    # プレイヤーの描画
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    # 画面の更新
    pygame.display.flip()
    pygame.time.Clock().tick(30)
