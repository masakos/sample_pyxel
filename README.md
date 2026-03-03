# sample_pyxel

[Pyxel](https://github.com/kitao/pyxel)を使った
ゲーム開発の基礎（描画・入力・当たり判定・シーン管理など）を学ぶためのサンプルをまとめています。

## 環境準備
```bash
python -m venv .venv
pip install pyxel 
.venv\Scripts\activate.bat
```

## run
```bash
python  pythonファイル名
```

## Pyxel Editorの起動
Pyxel アプリケーションで使用する画像やサウンドを作成する

```bash
pyxel edit my_resource.pyxre(Pyxelリソースファイル)
```

## htmlファイルに変換する
```bash
pyxel package . hanabi.py 
pyxel app2html sample_hanabi.pyxapp
```

