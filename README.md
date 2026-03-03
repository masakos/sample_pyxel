# sample_pyxel

[Pyxel](https://github.com/kitao/pyxel)を使ったミニゲーム集です。
ゲーム開発の基礎（描画・入力・当たり判定・シーン管理など）を学ぶためのサンプルをまとめています。

## run
```python
python -m venv .venv
pip install pyxel 
.venv\Scripts\activate.bat

pip install pyxel
python  pythonファイル名
```

## htmlファイルに変換する
```bash
pyxel package . hanabi.py 
pyxel app2html sample_hanabi.pyxapp
```

