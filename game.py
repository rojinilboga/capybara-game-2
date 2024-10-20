#importing the libraries
import pgzrun
from random import randint

TITLE = "CAPYBARA SHOT GAME!!!"
WIDTH = 600
HEIGHT = 600

#creating the capybara
capybara =Actor("capybara")

msg = ""

def draw():
    screen.clear()
    screen.fill(color =("#D6CA98") )

    capybara.draw()
    screen.draw.text(msg, center=(100,10), fontsize=30)

def place_capy():
   capybara.x=randint(50,550)
   capybara.y=randint(50,550) 

def on_mouse_down(pos):
    global msg
    if capybara.collidepoint(pos):
        msg = 'Good shot'
        place_capy()
    else:
        msg = "You missed:("


place_capy()


  



pgzrun.go()