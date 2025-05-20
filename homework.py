import pgzrun
from random import randint

WIDTH=500
HEIGHT=500

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = (R,G,B)
GRAVITY=2000.0

class Ball:
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y= initial_y
        self.vx=200
        self.vy=0
        self.radius=40

    
    def drawCircle(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)

ball= Ball(100,100)
ball2=Ball(200,100)


def draw():
    screen.clear()
    screen.fill("black")
    ball.drawCircle()
    ball2.drawCircle()
    


def update(dt):
    uy=ball.vy
    ball.vy = ball.vy + (GRAVITY *dt)

    ball.y += (uy + ball.vy) * 0.5 * dt

    if ball.y >HEIGHT:
        ball.y=HEIGHT-ball.radius
        ball.vy = -ball.vy * 0.9
    ball.x += ball.vx*dt

    if ball.x>WIDTH- ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

    uy=ball2.vy
    ball2.vy = ball2.vy + (GRAVITY *dt)

    ball2.y += (uy + ball2.vy) * 0.5 * dt

    if ball2.y >HEIGHT:
        ball2.y=HEIGHT-ball2.radius
        ball2.vy = -ball2.vy * 0.9
    ball2.x += ball2.vx*dt

    if ball2.x>WIDTH- ball2.radius or ball2.x < ball.radius:
        ball2.vx = -ball2.vx

def  on_key_down(key):
    if key == keys.UP:
        ball.vy = -500

def  on_key_down(key):
    if key == keys.W:
        ball2.vy = -500
        
pgzrun.go()