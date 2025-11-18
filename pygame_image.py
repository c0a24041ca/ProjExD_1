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
    tmr = 0
    x = tmr %3200#練習９残像問題

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(bg_img2, [-x+800, 0]) #練習7 こうかとんもう一匹
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