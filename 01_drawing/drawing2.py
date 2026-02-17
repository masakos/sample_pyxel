import pyxel

pyxel.init(160, 120, title="Pyxel Drawing")

pyxel.pset(10, 10, 7)  #  点　
pyxel.line(10, 20, 80, 20, 8)  # 線
pyxel.circ(20, 50, 10, 11)  #   塗りすつぶした円　
pyxel.circb(50, 50, 10, 11)  #  円の枠
pyxel.rect(10, 80, 20, 10, 13)  # 塗りつぶした四角形
pyxel.rectb(40, 80, 20, 10, 13)  # 四角形の枠

pyxel.show()





