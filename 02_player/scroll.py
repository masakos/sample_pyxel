import pyxel

WIDTH = 160
HEIGHT = 120
TILE_SIZE = 8
SCROLL_BORDER = WIDTH // 2
GROUND_Y = 100

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Scroll")
        pyxel.load("my_resource.pyxres")

        # プレイヤー（世界座標）
        self.player_world_x = 20
        self.player_y = GROUND_Y

        # 敵（世界座標）
        self.enemy_world_x = 200
        self.enemy_y = GROUND_Y

        # カメラ
        self.camera_x = 0

        pyxel.run(self.update, self.draw)

    def update(self):

        # 右移動
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_world_x += 2

            if self.player_world_x - self.camera_x > SCROLL_BORDER:
                self.camera_x += 2

        # 左移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_world_x -= 2

            if self.player_world_x - self.camera_x < SCROLL_BORDER:
                if self.camera_x > 0:
                    self.camera_x -= 2

        # 敵は左に移動（世界座標）
        self.enemy_world_x -= 1

        # 画面外に行ったら右端に再出現
        if self.enemy_world_x < self.camera_x - 20:
            self.enemy_world_x = self.camera_x + WIDTH + 50

    def draw(self):
        pyxel.cls(0)

        # 背景（タイルマップ）
        pyxel.bltm(
            0,
            0,
            0,
            self.camera_x,
            0,
            WIDTH,
            HEIGHT
        )

        # プレイヤー描画
        player_screen_x = self.player_world_x - self.camera_x
        pyxel.blt(
            player_screen_x,
            self.player_y,
            0,
            8, 0,
            8, 8,
            0
        )

        # 敵描画
        enemy_screen_x = self.enemy_world_x - self.camera_x
        pyxel.blt(
            enemy_screen_x,
            self.enemy_y,
            0,
            8, 8,
            8, 8,
            0
        )

App()

