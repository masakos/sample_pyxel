import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(
            0,  # 画面に描く位置x
            0,  # 画面に描く位置y
            0,  # タイルマップの番号
            0,  # タイルマップ内の開始位置
            0,  # タイルマップ内の開始位置
            160,  # 描く幅と高さ
            120,
        )

App()
