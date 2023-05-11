import pygame
import math

WIN = pygame.display.set_mode((2340, 780))
COLOR = (5, 5, 5)

WIDTH = 2340
HEIGHT = 780

def draw_window(h):
    WIN.fill((255, 255, 255))

    for i in range(len(h)):
        pygame.draw.rect(WIN, (0,0,0), ((i*2) + 150, (HEIGHT/2) - h[i], 2, 2))
    pygame.display.update()


def main():

    body_num = 1000

    mass = []
    height = []
    vell = []

    stiff_coeff = 1
    amplitude = 70
    wave_freq = 2
    t = 0.1
#
    for i in range(body_num):
        mass.append(1)
        height.append(0)
        vell.append(0)

    run = True
    start = False
    deg = 0
    clock = pygame.time.Clock()

    control = 0
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                else:
                    deg = 0
                    if event.key == pygame.K_a:
                        control = 0
                        start = not start
                    elif event.key == pygame.K_s:
                        control = int(body_num/2)
                        start = not start
                    elif event.key == pygame.K_d:
                        control = body_num - 1
                        start = not start

        if start:
            height[control] = s(deg, amplitude)
            deg += wave_freq

        for i in range(body_num):
            height[i] += vell[i]

        for i in range(body_num - 1):
            diff = height[i] - height[i+1]
            f = diff * stiff_coeff
            vell[i] += (-f / mass[i]) * t
            vell[i+1] += (f / mass[i+1]) * t

        draw_window(height)

def s(d, h):
    return math.sin(math.radians(d)) * h

if __name__ == "__main__":
    main()