import pyxel

pyxel.init(160, 120, title="Pyxel Drawing")
pyxel.load("my_resource.pyxres")

while True:
    #ゲームの処理
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.play(0, 0)

    #画面の表示
    pyxel.cls(6)
    pyxel.text(61, 60, "HELLO", 5)

    pyxel.flip()
