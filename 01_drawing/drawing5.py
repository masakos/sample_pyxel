import pyxel

WIDTH = 160
HEIGHT = 120
GRAVITY = 0.3
JUMP_POWER = -6
GROUND_Y = 96

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("my_resource.pyxres")

        self.px = 40
        self.py = GROUND_Y
        self.vy = 0
        self.on_ground = True

        self.ex = 100
        self.ey = GROUND_Y
        self.enemy_dir = 1

        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btn(pyxel.KEY_LEFT):
            self.px -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.px += 2

        if pyxel.btnp(pyxel.KEY_SPACE) and self.on_ground:
            self.vy = JUMP_POWER
            self.on_ground = False

        self.vy += GRAVITY
        self.py += self.vy

        if self.py >= GROUND_Y:
            self.py = GROUND_Y
            self.vy = 0
            self.on_ground = True

        self.ex += self.enemy_dir
        if self.ex < 20 or self.ex > 140:
            self.enemy_dir *= -1

    def draw(self):
        pyxel.cls(0)

        # 🔵 背景（Tilemap 0）
        pyxel.bltm(0, 0, 0, 0, 0, WIDTH, HEIGHT)

        # 👾 敵（Image 0 の右上に描いた場合）
        pyxel.blt(self.ex, self.ey - 16, 0, 240, 0, 16, 16, 0)

        # 🧍 プレイヤー（Image 0 の右下に描いた場合）
        pyxel.blt(self.px, self.py - 16, 0, 240, 240, 16, 16, 0)

App()
