
##  クリックすると花火があがる

## 5分説明
update と draw の役割
座標 += 速度
速度 += 重力

## 10分改造
「一番派手にできるか」

## 生徒にいじらせる場所はこの4つだけ：
PARTICLE_COUNT
SPEED
GRAVITY
FADE_SPEED

## 盛り上がる改造例 
① 超大量花火
PARTICLE_COUNT = 200

② 無重力宇宙花火
GRAVITY = 0

③ ゆっくり消える
FADE_SPEED = 0.5

④ 超高速爆発
SPEED = 5
