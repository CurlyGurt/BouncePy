import pygame 
from pygame.locals import *

class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.prevx = x
        self.prevy = y
        self.mass = mass

def eulerPhysics():
    p1 = Particle()

    force = 10.0
    acceleration = force / p1.mass

    time = 0.0
    deltaTime = 0.0

def verletUpdate(clock):
    for i in range(len(particles)):
        deltaTime = pygame.time.Clock.get_rawtime(clock)

        force = (0.0, 0.5)
        acceleration = (force[0] / particles[i].mass, force[1] / particles[i].mass)
        prevPosition = (particles[i].x, particles[i].y)

        particles[i].x = 2 * particles[i].x - particles[i].prevx + acceleration[0] * (deltaTime * deltaTime)
        particles[i].y = 2 * particles[i].y - particles[i].prevy + acceleration[1] * (deltaTime * deltaTime)
        
        particles[i].prevx = prevPosition[0]
        particles[i].prevy = prevPosition[1]

    #print("in verlet: particles[i].x = ", particles[i].x, "\tSupposed new number = ", 2 * particles[i].x - particles[i].prevx + acceleration[0] * (deltaTime * deltaTime))


particles = []
particles.append(Particle(10,10,1))
particles.append(Particle(20,10,1))
particles.append(Particle(30,10,1))
particles.append(Particle(40,10,1))

def main():
    #setup
    pygame.init()
    window = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()

    #Globals
    RED = (255,0,0)
    RADIUS = 10
  
    run = True

    while run:
        clock.tick(60)

        for i in range(len(particles)):
            pygame.draw.circle(window, RED, (particles[i].x, particles[i].y), RADIUS)

        pygame.display.update()

        window.fill((0,0,0))
        verletUpdate(clock)

main()