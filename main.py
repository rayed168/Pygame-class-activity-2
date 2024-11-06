import pygame as pg
pg.init()
WIDTH=500
HEIGHT=500
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Adding new image")
bg_image=pg.transform.scale(pg.image.load("Background.png").convert(),(WIDTH,HEIGHT))
penguin_image=pg.transform.scale(pg.image.load("download.png").convert_alpha(),(200,200))
penguin_rectangle=penguin_image.get_rect(center=(WIDTH//2,HEIGHT//2-30))
def game_loop():
    clock=pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
        screen.blit(bg_image,(0,0))
        screen.blit(penguin_image,penguin_rectangle)        
        pg.display.flip()
        clock.tick(30)
if __name__=="__main__":
    game_loop()
    