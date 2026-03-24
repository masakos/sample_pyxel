import pyxel
import random

# =============================================
# ★★★ 改造ポイント ★★★
# 数字を変えるだけでゲームの動きが変わるよ！
# =============================================
MOVE_SPEED     = 2    # プレイヤーの速さ　　（おすすめ範囲: 1〜5）
JUMP_POWER     = -10   # ジャンプ力　　　　　（おすすめ範囲: -4〜-10）
GRAVITY        = 9.8  # 重力の強さ　　　　　（おすすめ範囲: 0.2〜1.0）
ENEMY_SPEED    = 1    # 敵の移動速さ　　　　（おすすめ範囲: 1〜4）
ENEMY_INTERVAL = 90   # 敵の出やすさ　　　　（小さいほどよく出る、20〜120）

# =============================================
# 画面・キャラのサイズ（ここは変えなくてOK）
# =============================================
WIDTH            = 160  # 画面の横幅（ピクセル）
HEIGHT           = 120  # 画面の縦幅（ピクセル）
GROUND_Y         = 100  # 地面のY座標（プレイヤーが立つ位置）
SCROLL_BORDER    = WIDTH // 2  # プレイヤーの位置がこの境界を超えたら画面スクロール
MAP_TILE_WIDTH   = 20   # タイルマップの横タイル数
MAP_PIXEL_WIDTH  = MAP_TILE_WIDTH * 8  # タイルマップの横幅（ピクセル）
PLAYER_SIZE      = 8    # プレイヤーのサイズ（幅・高さ）
ENEMY_SIZE       = 8    # 敵のサイズ（幅・高さ）

# ゲームの状態
STATE_PLAY     = "play"
STATE_GAMEOVER = "gameover"


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Jump & Dodge!")
        pyxel.load("my_resource.pyxres")
        self.reset()
        pyxel.run(self.update, self.draw)

    # ゲームをリセットする（最初の状態に戻す）
    def reset(self):
        self.player_world_x = 20  # プレイヤーのX座標（世界座標）
        self.player_y       = GROUND_Y
        self.player_vy      = 0     # 縦方向の速度
        self.is_jumping     = False

        self.camera_x = 0    # カメラの位置
        self.enemies  = []   # 敵のリスト
        self.score    = 0    # スコア

        self.state = STATE_PLAY

    # =========================
    # 毎フレーム呼ばれる更新処理
    # =========================
    def update(self):
        if self.state == STATE_PLAY:
            self.update_play()
        elif self.state == STATE_GAMEOVER:
            if pyxel.btnp(pyxel.KEY_R):  # Rキーでリトライ
                self.reset()

    def update_play(self):

        # -------- スコア --------
        # 毎フレーム1点ずつ増える
        self.score += 1

        # -------- プレイヤー移動 --------
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_world_x += MOVE_SPEED
            # 画面の右半分まで来たらカメラをスクロール
            if self.player_world_x - self.camera_x > SCROLL_BORDER:
                self.camera_x += MOVE_SPEED

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_world_x -= MOVE_SPEED
            if self.player_world_x - self.camera_x < SCROLL_BORDER:
                if self.camera_x > 0:
                    self.camera_x -= MOVE_SPEED

        # -------- ジャンプ --------
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.is_jumping:
            self.player_vy  = JUMP_POWER
            self.is_jumping = True

        # 重力で落ちる
        self.player_vy += GRAVITY
        self.player_y  += self.player_vy

        # 地面で止まる
        if self.player_y >= GROUND_Y:
            self.player_y   = GROUND_Y
            self.player_vy  = 0
            self.is_jumping = False

        # -------- 敵の出現 --------
        # ランダムで敵が画面右から出てくる
        # 0〜ENEMY_INTERVALの範囲でランダムな数を生成して、0だったら敵を出す
        if random.randint(0, ENEMY_INTERVAL) == 0:
            spawn_x = self.camera_x + WIDTH + random.randint(0, 40)
            self.enemies.append({"x": spawn_x, "y": GROUND_Y})

        # -------- 敵の移動 --------
        for enemy in self.enemies:
            enemy["x"] -= ENEMY_SPEED

        # 画面の外に出た敵を消す
        self.enemies = [e for e in self.enemies if e["x"] > self.camera_x - 20]

        # -------- 当たり判定 --------
        # プレイヤーと敵の四角が重なったらゲームオーバー
        px = self.player_world_x
        py = self.player_y
        for enemy in self.enemies:
            ex = enemy["x"]
            ey = enemy["y"]
            if (px + PLAYER_SIZE > ex and px < ex + ENEMY_SIZE and
                    py + PLAYER_SIZE > ey and py < ey + ENEMY_SIZE):
                self.state = STATE_GAMEOVER

    # =========================
    # 毎フレーム呼ばれる描画処理
    # =========================
    def draw(self):
        pyxel.cls(0)

        # -------- 背景（タイルマップをループ表示）--------
        map_x = self.camera_x % MAP_PIXEL_WIDTH
        pyxel.bltm(0, 0, 0, map_x, 0, WIDTH, HEIGHT)
        if map_x + WIDTH > MAP_PIXEL_WIDTH:
            pyxel.bltm(MAP_PIXEL_WIDTH - map_x, 0, 0, 0, 0, WIDTH, HEIGHT)

        # -------- プレイヤー描画 --------
        screen_x = self.player_world_x - self.camera_x
        pyxel.blt(screen_x, self.player_y, 0, 8, 0, PLAYER_SIZE, PLAYER_SIZE, 0)

        # -------- 敵描画 --------
        for enemy in self.enemies:
            ex = enemy["x"] - self.camera_x
            pyxel.blt(ex, enemy["y"], 0, 8, 8, ENEMY_SIZE, ENEMY_SIZE, 0)

        # -------- スコア表示 --------
        # ★改造ポイント★スコアを表示する 
        # pyxel.text(5, 5, f"SCORE: {self.score}", 7)

        # -------- ゲームオーバー画面 --------
        if self.state == STATE_GAMEOVER:
            pyxel.rect(35, 42, 90, 38, 1)          # 背景の黒い四角
            pyxel.rectb(35, 42, 90, 38, 7)         # 枠線
            pyxel.text(57, 50, "GAME OVER!", 8)    # 赤い文字
            pyxel.text(50, 62, f"SCORE: {self.score}", 10)
            pyxel.text(46, 72, "R : RETRY", 6)


App()
