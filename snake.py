import pygame
pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Snake game')

blue=(0,0,255)
red=(255,0,0)
green = (0,255,0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,blue,[450,350,20,20])
    pygame.display.update()
pygame.quit()
quit()
