import pyxel
import random
import math

WIDTH = 160
HEIGHT = 120

PARTICLE_COUNT = 40      # ← ① 粒の数を変えてみよう
SPEED = 2.5              # ← ② 初速度を変えてみよう
GRAVITY = 0.05           # ← ③ 重力を変えてみよう
FADE_SPEED = 2           # ← ④ 消える速さを変えてみよう


class Particle:
    def __init__(self, x, y):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, SPEED)

        self.x = x
        self.y = y
        # 花火が「円状に広がる」ための速度の計算
        # 「角度」と「速さ」から 「x方向の速度」と「y方向の速度」を計算している」
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = 60
        self.color = random.randint(1, 15)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
        self.life -= FADE_SPEED

    def draw(self):
        if self.life > 0:
            pyxel.pset(self.x, self.y, self.color)


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        self.particles = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.explode(pyxel.mouse_x, pyxel.mouse_y)

        for p in self.particles:
            p.update()

        self.particles = [p for p in self.particles if p.life > 0]

    def draw(self):
        pyxel.cls(0)
        for p in self.particles:
            p.draw()

    def explode(self, x, y):
        for _ in range(PARTICLE_COUNT):
            self.particles.append(Particle(x, y))


App()
