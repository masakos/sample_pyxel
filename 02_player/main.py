import pyxel

# -----------------
# 定数
# -----------------
WIDTH = 160
HEIGHT = 120

GRAVITY = 0.4
JUMP_POWER = -6
MOVE_SPEED = 2
GROUND_Y = 100  # 地面の高さ


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=" Jump Sample")
        pyxel.load("my_resource.pyxres")

        # プレイヤー初期位置
        self.x = 15
        self.y = GROUND_Y

        # 速度
        self.vy = 0

        # 地面にいるかどうか
        self.on_ground = True

        pyxel.run(self.update, self.draw)

    # -----------------
    # 更新処理
    # -----------------
    def update(self):

        # 左移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= MOVE_SPEED

        # 右移動
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += MOVE_SPEED

        # ジャンプ（押した瞬間）
        if pyxel.btnp(pyxel.KEY_SPACE) and self.on_ground:
            self.vy = JUMP_POWER
            self.on_ground = False

        # 重力
        self.vy += GRAVITY
        self.y += self.vy

        # 地面との衝突判定
        if self.y >= GROUND_Y:
            self.y = GROUND_Y
            self.vy = 0
            self.on_ground = True

    # -----------------
    # 描画処理
    # -----------------
    def draw(self):
        pyxel.cls(0)

        # 地面
        pyxel.rect(0, GROUND_Y + 8, WIDTH, HEIGHT - GROUND_Y, 3)

        # プレイヤー描画
        pyxel.blt(
            self.x,
            self.y,
            0,      # image 0
            8, 0,   # 読み込み座標
            8, 8, # サイズ
            0       # 透明色
        )


App()
