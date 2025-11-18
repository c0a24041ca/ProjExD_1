import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習8 背景画像左右反転
    kk_img = pg.image.load("fig/3.png") #練習3:こうかとん画像の読み込み
    kk_img = pg.transform.flip(kk_img, True, False) #練習3反転
    kk_rct = kk_img.get_rect() #練習10-1
    kk_rct.center = 300,200 #練習10-2 こうかとんの座標
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() # 練習10-3:キーの押下状態を取得
        move_vector = [-1, 0]
        if key_lst[pg.K_UP]: # 上矢印キー
             move_vector[1] -= 1 # 上に移動
        if key_lst[pg.K_DOWN]: # 下矢印キー
             move_vector[1] += 1 # 下に移動
        if key_lst[pg.K_LEFT]: # 左矢印キー
             move_vector[0] -= 1 # 左に移動
        if key_lst[pg.K_RIGHT]: # 右矢印キー
            move_vector[0] += 2 # 右に移動
        kk_rct.move_ip(move_vector)
        x = tmr %3200#練習９残像問題

        screen.blit(bg_img, [0, 0])
        screen.blit(bg_img2, [-x+1600, 0]) #練習7 こうかとんもう一匹
        screen.blit(bg_img, [-x, 0])#練習5背景移動
        screen.blit(kk_img,(300,200)) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習６


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()