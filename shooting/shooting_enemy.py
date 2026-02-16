import pyxel
import random

WIDTH = 160
HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Image Shooting")

        # 画像読み込み（0番のイメージバンク）
        pyxel.image(0).load(0, 0, "face.png")

        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - 15
        self.bullets = []
        self.enemies = []
        self.frame_count = 0

    def update(self):
        # 左右移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x -= 3
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += 3

        self.player_x = max(8, min(WIDTH - 8, self.player_x))

        # 発射
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append([self.player_x, self.player_y])

        # 弾移動
        for bullet in self.bullets:
            bullet[1] -= 4
        self.bullets = [b for b in self.bullets if b[1] > 0]

        # 敵出現
        self.frame_count += 1
        if self.frame_count % 40 == 0:
            x = random.randint(16, WIDTH - 16)
            self.enemies.append([x, 0])

        # 敵移動
        for enemy in self.enemies:
            enemy[1] += 2

    def draw(self):
        pyxel.cls(0)

        # プレイヤー
        pyxel.tri(
            self.player_x, self.player_y - 6,
            self.player_x - 6, self.player_y + 6,
            self.player_x + 6, self.player_y + 6,
            11
        )

        # 弾
        for bullet in self.bullets:
            pyxel.circ(bullet[0], bullet[1], 2, 10)

        # 敵（画像表示）
        for enemy in self.enemies:
            pyxel.blt(
                enemy[0] - 8,  # 表示位置X
                enemy[1] - 8,  # 表示位置Y
                0,             # イメージバンク
                0, 0,          # 画像の左上座標
                16, 16,        # 幅・高さ
                0              # 透明色
            )

App()

