import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        # pg.display.update()
        tmr += 1
        clock.tick(10)


        png3 = pg.image.load("fig/3.png")
        png3 = pg.transform.flip(png3, True, False)
        png3 = pg.transform.rotozoom(png3, 10, 1.0)
        screen.blit(png3, [300, 200])
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()