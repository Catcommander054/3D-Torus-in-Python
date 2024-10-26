import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def draw_torus(r, R, N, M):
    for i in range(N):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(M + 1):
            for k in [i, i + 1]:
                theta = float(k) * (2.0 * np.pi / N)
                phi = float(j) * (2.0 * np.pi / M)

                x = (R + r * np.cos(phi)) * np.cos(theta)
                y = (R + r * np.cos(phi)) * np.sin(theta)
                z = r * np.sin(phi)

                nx = np.cos(phi) * np.cos(theta)
                ny = np.cos(phi) * np.sin(theta)
                nz = np.sin(phi)
                glNormal3f(nx, ny, nz)

                glVertex3f(x, y, z)
        glEnd()


def main():
    pygame.init()
    display = (1920, 1080) #Разрешение экрана

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | pygame.DOUBLEBUF | HWSURFACE | OPENGLBLIT)

    glClearColor(0.2, 0.2, 0.2, 1.0)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    light_position = [2.0, 2.0, 2.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    ambient_light = [0.2, 0.2, 0.2, 1.0]
    diffuse_light = [1.0, 1.0, 1.0, 1.0]
    specular_light = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)

    material_color = [0.5, 0.25, 1.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_color)

    r = 0.25
    R = 1.0
    N = 30
    M = 15

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1.0, 1.0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_torus(r, R, N, M)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
