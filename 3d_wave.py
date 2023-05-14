import pygame
import math
import numpy as np


WIDTH = 150
HEIGHT = 150

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOR = (5, 5, 5)

maxH = 10


def main():

    h = HEIGHT
    w = WIDTH

    mass = []
    height = []
    vell = []

    stiff_coeff = 0.5
    amplitude = 250
    wave_freq = 0.5
    t = 0.1

    mass = np.ones((HEIGHT, WIDTH))
    height = np.zeros((HEIGHT, WIDTH))
    vell = np.zeros((HEIGHT, WIDTH))

    run = True
    start = False
    deg = 0
    WIN.fill((0, 0, 0))
    for i in range(h):
        for a in range(w):
            if math.sqrt((int(w/2) - a) ** 2 + (int(h/2) - i) ** 2) < 30:
                mass[i][a] = 3
                WIN.set_at((i, a), (24, 32, 77))

    
    frame = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                else:
                    deg = 0
                    if event.key == pygame.K_a:
                        start = not start

        if start:
            height[int(h/2)][1] = s(deg, amplitude)
            deg += wave_freq
            # print(vell[int(h/2)][1])

        for i in range(1, h - 1):
            for a in range(1, w - 1):
                height[i][a] += vell[i][a]
                c = height[i][a]
                if c > 255:
                    c = 255
                if c < 0:
                    c = 0
                WIN.set_at((a, i), (c,c,c))

        for a in range(1, h-1):
            for i in range(1, w - 1):
                diff = -height[a][i] * 4 + (height[a][i - 1] + height[a][i + 1] + height[a + 1][i] + height[a - 1][i])
                # diff = (height[a][i - 1] + height[a][i + 1] + height[a + 1][i] + height[a - 1][i])/4 - height[a][i]
                # f = diff * stiff_coeff
                vell[a][i] += (diff / mass[a][i]) * t

        pygame.display.update()

        frame+=1

def s(d, h):
    return math.sin(math.radians(d)) * h

if __name__ == "__main__":
    main()