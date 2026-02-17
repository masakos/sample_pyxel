import pyxel

# -----------------
# 定数
# -----------------
WIDTH = 160
HEIGHT = 120

GRAVITY = 0.3
JUMP_POWER = -5
MOVE_SPEED = 2
GROUND_Y = 100  # 上から100ピクセル下の高さ　

PLAYER_SIZE = 8
ENEMY_SIZE = 8


class Enemy:
    def __init__(self):
        # 右端から出現
        self.x = WIDTH
        self.y = GROUND_Y
        self.speed = 1.5

    def update(self):
        # 常に左へ移動
        self.x -= self.speed

    def is_out(self):
        # 画面左外に出たら True
        return self.x < -ENEMY_SIZE

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            0,
            8, 8,  # 敵画像 (8,8)
            ENEMY_SIZE,
            ENEMY_SIZE,
            0
        )


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Right Spawn Enemy")
        pyxel.load("my_resource.pyxres")

        # プレイヤー
        self.x = 15
        self.y = GROUND_Y
        self.vy = 0
        self.on_ground = True

        self.enemies = []

        pyxel.run(self.update, self.draw)

    def update(self):

        # -----------------
        # プレイヤー移動
        # -----------------
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= MOVE_SPEED

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += MOVE_SPEED

        if pyxel.btnp(pyxel.KEY_SPACE) and self.on_ground:
            self.vy = JUMP_POWER
            self.on_ground = False

        # 重力
        self.vy += GRAVITY
        self.y += self.vy

        if self.y >= GROUND_Y:
            self.y = GROUND_Y
            self.vy = 0
            self.on_ground = True

        # -----------------
        # 敵出現（60フレームごと）
        # -----------------
        if pyxel.frame_count % 60 == 0:
            self.enemies.append(Enemy())

        # 敵更新
        for enemy in self.enemies:
            enemy.update()

        # 画面外の敵を削除
        self.enemies = [e for e in self.enemies if not e.is_out()]

    def draw(self):
        pyxel.cls(6)
        pyxel.text(60, 60, "Hello, Pyxel!", 5)

        # 地面
        pyxel.rect(
            0,
            GROUND_Y + PLAYER_SIZE,
            WIDTH,
            HEIGHT - GROUND_Y,
            3
        )

        # プレイヤー描画
        pyxel.blt(
            self.x,
            self.y,
            0,
            8, 0,      # プレイヤー画像 (8,0)
            PLAYER_SIZE,
            PLAYER_SIZE,
            0
        )

        # 敵描画
        for enemy in self.enemies:
            enemy.draw()


App()
