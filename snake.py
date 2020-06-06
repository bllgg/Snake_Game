import pygame
import time

pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Snake game')

blue=(0,0,255)
red=(255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255, 255, 255)

game_over=False

x1 = 400
y1 = 300

snake_block = 20

x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [400, 300])

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -20
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 20
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -20
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 20
                x1_change = 0

    if x1 >= 800 or x1 <= 0 or y1 >= 600 or y1 <= 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, green, [x1, y1, snake_block, snake_block])
 
    pygame.display.update()
 
    clock.tick(snake_speed)

message("LOST",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
