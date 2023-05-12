import pygame
import math



WIDTH = 500
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOR = (5, 5, 5)

maxH = 100

def draw_window(height, h, w):
    WIN.fill((255, 255, 255))

    for i in range(h):
        for a in range(w):
            c = (255/100) * (abs(height[i][a]) * 100 / maxH)
            WIN.set_at((i, a), (c,c,c))

    pygame.display.update()


def main():

    h = HEIGHT
    w = WIDTH

    mass = []
    height = []
    vell = []

    stiff_coeff = 50
    amplitude = 100
    wave_freq = 5
    t = 0.01

    for n in range(h):
        mass.append([])
        height.append([])
        vell.append([])
        for i in range(w):
            mass[n].append(1)
            height[n].append(0)
            vell[n].append(0)

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
                        control = int(w/2)
                        start = not start
                    elif event.key == pygame.K_d:
                        control = w - 1
                        start = not start

        if start:
            height[int(h/2)][control] = s(deg, amplitude)
            deg += wave_freq

        for i in range(h):
            for a in range(w):
                height[i][a] += vell[i][a]

        for a in range(h):
            for i in range(w - 1):
                diff = height[a][i] - height[a][i+1]
                f = diff * stiff_coeff
                vell[a][i] += (-f / mass[a][i]) * t
                vell[a][i+1] += (f / mass[a][i+1]) * t

        for a in range(w):
            for i in range(h - 1):
                diff = height[i][a] - height[i+1][a]
                f = diff * stiff_coeff
                vell[i][a] += (-f / mass[i][a]) * t
                vell[i+1][a] += (f / mass[i+1][a]) * t

        draw_window(height, h, w)

def s(d, h):
    return math.sin(math.radians(d)) * h

if __name__ == "__main__":
    main()