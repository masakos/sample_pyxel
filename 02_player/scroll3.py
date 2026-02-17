
import pyxel
import random

WIDTH = 160
HEIGHT = 120
TILE_SIZE = 8

MAP_TILE_WIDTH = 20
MAP_PIXEL_WIDTH = MAP_TILE_WIDTH * TILE_SIZE

GROUND_Y = 100
GRAVITY = 0.5
JUMP_POWER = -6
MOVE_SPEED = 2
SCROLL_BORDER = WIDTH // 2

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Scroll Control")
        pyxel.load("my_resource.pyxres")

        # プレイヤー（世界座標）
        self.player_world_x = 20
        self.player_y = GROUND_Y
        self.player_vy = 0
        self.is_jumping = False

        # カメラ
        self.camera_x = 0

        # 敵リスト
        self.enemies = []

        pyxel.run(self.update, self.draw)

    def update(self):

        # -------------------
        # 左右移動（自分で操作）
        # -------------------
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_world_x += MOVE_SPEED

            # スクロール境界
            if self.player_world_x - self.camera_x > SCROLL_BORDER:
                self.camera_x += MOVE_SPEED

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_world_x -= MOVE_SPEED

            # カメラが左に行きすぎない
            if self.player_world_x - self.camera_x < SCROLL_BORDER:
                if self.camera_x > 0:
                    self.camera_x -= MOVE_SPEED

        # -------------------
        # ジャンプ
        # -------------------
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.is_jumping:
            self.player_vy = JUMP_POWER
            self.is_jumping = True

        self.player_vy += GRAVITY
        self.player_y += self.player_vy

        if self.player_y >= GROUND_Y:
            self.player_y = GROUND_Y
            self.player_vy = 0
            self.is_jumping = False

        # -------------------
        # 敵ランダム出現
        # -------------------
        if random.randint(0, 90) == 0:
            spawn_x = self.camera_x + WIDTH + random.randint(0, 40)
            self.enemies.append({"x": spawn_x, "y": GROUND_Y})

        # 敵更新
        for enemy in self.enemies:
            enemy["x"] -= 1

        # 画面外削除
        self.enemies = [
            e for e in self.enemies
            if e["x"] > self.camera_x - 20
        ]

        # -------------------
        # 当たり判定
        # -------------------
        player_left = self.player_world_x
        player_right = self.player_world_x + 8
        player_top = self.player_y
        player_bottom = self.player_y + 8

        for enemy in self.enemies:
            enemy_left = enemy["x"]
            enemy_right = enemy["x"] + 8
            enemy_top = enemy["y"]
            enemy_bottom = enemy["y"] + 8

            if (
                player_right > enemy_left and
                player_left < enemy_right and
                player_bottom > enemy_top and
                player_top < enemy_bottom
            ):
                pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        # -------------------
        # 背景ループ表示
        # -------------------
        map_x = self.camera_x % MAP_PIXEL_WIDTH

        pyxel.bltm(0, 0, 0, map_x, 0, WIDTH, HEIGHT)

        if map_x + WIDTH > MAP_PIXEL_WIDTH:
            pyxel.bltm(
                MAP_PIXEL_WIDTH - map_x,
                0,
                0,
                0,
                0,
                WIDTH,
                HEIGHT
            )

        # -------------------
        # プレイヤー描画
        # -------------------
        screen_x = self.player_world_x - self.camera_x
        pyxel.blt(
            screen_x,
            self.player_y,
            0,
            8, 0,
            8, 8,
            0
        )

        # -------------------
        # 敵描画
        # -------------------
        for enemy in self.enemies:
            enemy_screen_x = enemy["x"] - self.camera_x
            pyxel.blt(
                enemy_screen_x,
                enemy["y"],
                0,
                8, 8,
                8, 8,
                0
            )

App()
