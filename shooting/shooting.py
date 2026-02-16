import pyxel 
import random

WIDTH = 160
HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Simple Shooting")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - 15
        self.bullets = []
        self.enemies = []
        self.score = 0
        self.frame_count = 0
        self.game_over = False

    # -------------------
    # 更新処理
    # -------------------
    def update(self):

        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.reset()
            return

        # プレイヤー移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x -= 3
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += 3

        self.player_x = max(5, min(WIDTH - 5, self.player_x))

        # 弾発射
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append([self.player_x, self.player_y])

        # 弾移動
        for bullet in self.bullets:
            bullet[1] -= 4

        self.bullets = [b for b in self.bullets if b[1] > 0]

        # 敵出現
        self.frame_count += 1
        if self.frame_count % 30 == 0:
            x = random.randint(10, WIDTH - 10)
            self.enemies.append([x, 0])

        # 敵移動
        for enemy in self.enemies:
            enemy[1] += 2

        # 当たり判定
        for enemy in self.enemies:
            for bullet in self.bullets:
                if abs(enemy[0] - bullet[0]) < 6 and abs(enemy[1] - bullet[1]) < 6:
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    self.score += 10
                    break

        # プレイヤーに当たったらゲームオーバー
        for enemy in self.enemies:
            if abs(enemy[0] - self.player_x) < 8 and abs(enemy[1] - self.player_y) < 8:
                self.game_over = True

        # 画面外削除
        self.enemies = [e for e in self.enemies if e[1] < HEIGHT]

    # -------------------
    # 描画処理
    # -------------------
    def draw(self):
        pyxel.cls(0)

        if self.game_over:
            pyxel.text(WIDTH//2 - 20, HEIGHT//2, "GAME OVER", 8)
            pyxel.text(WIDTH//2 - 30, HEIGHT//2 + 10, "Press R to Restart", 7)
            pyxel.text(5, 5, f"SCORE: {self.score}", 10)
            return

        # プレイヤー（三角形）
        pyxel.tri(
            self.player_x, self.player_y - 5,
            self.player_x - 5, self.player_y + 5,
            self.player_x + 5, self.player_y + 5,
            11
        )

        # 弾
        for bullet in self.bullets:
            pyxel.circ(bullet[0], bullet[1], 2, 10)

        # 敵
        for enemy in self.enemies:
            pyxel.rect(enemy[0] - 4, enemy[1] - 4, 8, 8, 8)

        # スコア
        pyxel.text(5, 5, f"SCORE: {self.score}", 7)


App()
