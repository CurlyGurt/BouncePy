import pygame 
from pygame.locals import *
import math

class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.prevx = x
        self.prevy = y
        self.mass = mass

class Stick:
    def __init__(self, particleA, particleB, length):
        self.particleA = particleA
        self.particleB = particleB
        self.length = length

def eulerPhysics():

    p1 = Particle()

    force = 10.0
    acceleration = force / p1.mass

    time = 0.0
    deltaTime = 0.0

def borderBounds(particle):
    if particle.x >= WIDTH: particle.x = WIDTH
    if particle.y >= HEIGHT: particle.y = HEIGHT
    if particle.x < 0: particle.x = 0
    if particle.y < 0: particle.y = 0

def findDifference(particleA, particleB):
    return (particleA.x - particleB.x, particleA.y - particleB.y)

def verletUpdate(clock):
    deltaTime = pygame.time.Clock.get_rawtime(clock)
    for i in range(len(particles)):
        force = (0.0, 0.025)
        acceleration = (force[0] / particles[i].mass, force[1] / particles[i].mass)
        prevPosition = (particles[i].x, particles[i].y)

        particles[i].x = 2 * particles[i].x - particles[i].prevx + acceleration[0] * (deltaTime * deltaTime)
        particles[i].y = 2 * particles[i].y - particles[i].prevy + acceleration[1] * (deltaTime * deltaTime)
        
        particles[i].prevx = prevPosition[0]
        particles[i].prevy = prevPosition[1]

        borderBounds(particles[i])

    for i in range(len(sticks)):
        particleDiff = findDifference(sticks[i].particleA, sticks[i].particleB)
        #print("particleDiff = ", particleDiff)
        diffFactor = (sticks[i].length - findLength(particleDiff)) / findLength(particleDiff) * .5
        offset = (particleDiff[0] * diffFactor, particleDiff[1] * diffFactor)

        sticks[i].particleA.x += offset[0]
        sticks[i].particleA.y += offset[1]
        sticks[i].particleB.x -= offset[0]
        sticks[i].particleB.y -= offset[1]



def findLength(particle):
    return math.sqrt((particle[0]*particle[0]) + (particle[1]*particle[1]))

def findDistance(particleA, particleB):
    xDiff = particleA.x - particleB.x
    yDiff = particleA.y - particleB.y
    return math.sqrt((xDiff*xDiff) + (yDiff*yDiff))



    #print("in verlet: particles[i].x = ", particles[i].x, "\tSupposed new number = ", 2 * particles[i].x - particles[i].prevx + acceleration[0] * (deltaTime * deltaTime))


particles = []
particles.append(Particle(10,50,1))     #0          #1------#2  
particles.append(Particle(40,30,1))     #1           |       |
particles.append(Particle(70,30,1))     #2          #0------#3
particles.append(Particle(100,50,1))    #3

sticks = []
sticks.append(Stick(particles[0], particles[1], findDistance(particles[0], particles[1])))
sticks.append(Stick(particles[1], particles[2], findDistance(particles[1], particles[2])))
sticks.append(Stick(particles[2], particles[3], findDistance(particles[2], particles[3])))
sticks.append(Stick(particles[3], particles[0], findDistance(particles[3], particles[0])))
sticks.append(Stick(particles[0], particles[2], findDistance(particles[0], particles[2])))
sticks.append(Stick(particles[1], particles[3], findDistance(particles[1], particles[3])))
#sticks.append(Stick(particles[], particles[], findDistance(particles[], particles[])))
              

WIDTH = 600
HEIGHT = 600

def main():
    #setup
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    #Globals
    RED = (255,0,0)
    RADIUS = 5
  
    run = True

    while run:
        clock.tick(144)

        for i in range(len(particles)):
            pygame.draw.circle(window, RED, (particles[i].x, particles[i].y), RADIUS)

        for i in range(len(sticks)):
            pygame.draw.line(window, RED, (sticks[i].particleA.x, sticks[i].particleA.y), (sticks[i].particleB.x, sticks[i].particleB.y), 2)

        pygame.display.update()

        window.fill((0,0,0))
        verletUpdate(clock)

main()