import pyxel
import random

TILE_SIZE = 16
MAZE_W = 15   # 横マス数（奇数にする）
MAZE_H = 15   # 縦マス数（奇数にする）

class App:
    def __init__(self):
        pyxel.init(MAZE_W * TILE_SIZE, MAZE_H * TILE_SIZE, title="Random Maze")
        self.maze = [[1 for _ in range(MAZE_W)] for _ in range(MAZE_H)]
        self.generate_maze()
        self.player_x = 1
        self.player_y = 1
        pyxel.run(self.update, self.draw)

    # --- 迷路生成（穴掘り法） ---
    def generate_maze(self):
        stack = [(1, 1)]
        self.maze[1][1] = 0

        while stack:
            x, y = stack[-1]
            directions = [(2,0), (-2,0), (0,2), (0,-2)]
            random.shuffle(directions)

            carved = False
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 1 <= nx < MAZE_W-1 and 1 <= ny < MAZE_H-1:
                    if self.maze[ny][nx] == 1:
                        self.maze[y + dy//2][x + dx//2] = 0
                        self.maze[ny][nx] = 0
                        stack.append((nx, ny))
                        carved = True
                        break

            if not carved:
                stack.pop()

    # --- 更新処理 ---
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        dx, dy = 0, 0
        if pyxel.btnp(pyxel.KEY_LEFT):
            dx = -1
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            dx = 1
        elif pyxel.btnp(pyxel.KEY_UP):
            dy = -1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            dy = 1

        nx = self.player_x + dx
        ny = self.player_y + dy

        if 0 <= nx < MAZE_W and 0 <= ny < MAZE_H:
            if self.maze[ny][nx] == 0:
                self.player_x = nx
                self.player_y = ny

    # --- 描画処理 ---
    def draw(self):
        pyxel.cls(0)

        for y in range(MAZE_H):
            for x in range(MAZE_W):
                if self.maze[y][x] == 1:
                    pyxel.rect(x*TILE_SIZE, y*TILE_SIZE,
                               TILE_SIZE, TILE_SIZE, 5)

        # プレイヤー（丸）
        pyxel.circ(
            self.player_x*TILE_SIZE + TILE_SIZE//2,
            self.player_y*TILE_SIZE + TILE_SIZE//2,
            TILE_SIZE//2 - 2,
            8
        )

App()
