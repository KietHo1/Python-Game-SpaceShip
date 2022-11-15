import pgzrun
import random
from random import randint
WIDTH=800
HEIGHT=600
score=0
game_over=False
#Build menu
print("*******************************************************")
print("*                 Menu game SpaceShip                 *")
print("*-----------------------------------------------------*")
print("* 1. You can choose your Playership, Gem and Meteor   *")
print("* 2. Random Playership, Gem and Meteor                *")
print("*******************************************************")

while True:
    chooseNumber = input("Enter your choose number: ")
    chooseNumber = int (chooseNumber)
    if(chooseNumber > 0 and chooseNumber < 3):
        break
if(chooseNumber == 1):
    #Choose playership in your way
    while True:
        listPlayershipNumber = input("Enter your playership number: ")
        listPlayershipNumber = int (listPlayershipNumber)
        if(listPlayershipNumber > 0 and listPlayershipNumber < 13):
            break
    if(listPlayershipNumber == 1):
        ship=Actor('playership/playership1_blue')
    elif(listPlayershipNumber == 2):
        ship=Actor('playership/playership1_green')
    elif(listPlayershipNumber == 3):
        ship=Actor('playership/playership1_orange')
    elif(listPlayershipNumber == 4):
        ship=Actor('playership/playership1_red')
    elif(listPlayershipNumber == 5):
        ship=Actor('playership/playership2_blue')
    elif(listPlayershipNumber == 6):
        ship=Actor('playership/playership2_green')
    elif(listPlayershipNumber == 7):
        ship=Actor('playership/playership2_orange')
    elif(listPlayershipNumber == 8):
        ship=Actor('playership/playership2_red')
    elif(listPlayershipNumber == 9):
        ship=Actor('playership/playership3_blue')
    elif(listPlayershipNumber == 10):
        ship=Actor('playership/playership3_green')
    elif(listPlayershipNumber == 11):
        ship=Actor('playership/playership3_orange')
    else:
        ship=Actor('playership/playership3_red')
    ship.x=370
    ship.y=550
    #Choose gem in your way
    while True:
        listGemNumber = input("Enter your gem number: ")
        listGemNumber = int (listGemNumber)
        if(listGemNumber > 0 and listGemNumber < 13):
            break
    if(listGemNumber == 1):
        gem=Actor('gem/gemblue')
    elif(listGemNumber == 2):
        gem=Actor('gem/gemgreen')
    elif(listGemNumber == 3):
        gem=Actor('gem/gemred')
    elif(listGemNumber == 4):
        gem=Actor('gem/gemyellow')
    elif(listGemNumber == 5):
        gem=Actor('gem/hud_gem_blue')
    elif(listGemNumber == 6):
        gem=Actor('gem/hud_gem_green')
    elif(listGemNumber == 7):
        gem=Actor('gem/hud_gem_red')
    else:
        gem=Actor('gem/hud_gem_yellow')
    gem.x=200
    gem.y=0
    #Choose meteor in your way
    while True:
        listMeteorNumber = input("Enter your meteor number: ")
        listMeteorNumber = int (listMeteorNumber)
        if(listMeteorNumber > 0 and listMeteorNumber < 13):
            break
    if(listMeteorNumber == 1):
        meto=Actor('./meteor/meteorbrown_big1')
    elif(listMeteorNumber == 2):
        meto=Actor('./meteor/meteorbrown_big2')
    elif(listMeteorNumber == 3):
        meto=Actor('./meteor/meteorbrown_big3')
    elif(listMeteorNumber == 4):
        meto=Actor('./meteor/meteorbrown_big4')
    elif(listMeteorNumber == 5):
        meto=Actor('./meteor/meteorgrey_big1')
    elif(listMeteorNumber == 6):
        meto=Actor('./meteor/meteorgrey_big2')
    elif(listMeteorNumber == 7):
        meto=Actor('./meteor/meteorgrey_big3')
    else:
        meto=Actor('./meteor/meteorgrey_big4')
    meto.x=400
    meto.y=0
else:
    # Random playership
    listPlayershipNumber = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12]
    if(random.choice(listPlayershipNumber) == 1):
        ship=Actor('playership/playership1_blue')
    elif(random.choice(listPlayershipNumber) == 2):
        ship=Actor('playership/playership1_green')
    elif(random.choice(listPlayershipNumber) == 3):
        ship=Actor('playership/playership1_orange')
    elif(random.choice(listPlayershipNumber) == 4):
        ship=Actor('playership/playership1_red')
    elif(random.choice(listPlayershipNumber) == 5):
        ship=Actor('playership/playership2_blue')
    elif(random.choice(listPlayershipNumber) == 6):
        ship=Actor('playership/playership2_green')
    elif(random.choice(listPlayershipNumber) == 7):
        ship=Actor('playership/playership2_orange')
    elif(random.choice(listPlayershipNumber) == 8):
        ship=Actor('playership/playership2_red')
    elif(random.choice(listPlayershipNumber) == 9):
        ship=Actor('playership/playership3_blue')
    elif(random.choice(listPlayershipNumber) == 10):
        ship=Actor('playership/playership3_green')
    elif(random.choice(listPlayershipNumber) == 11):
        ship=Actor('playership/playership3_orange')
    else:
        ship=Actor('playership/playership3_red')
    ship.x=370
    ship.y=550
    # Random playership
    listGemNumber = [1, 2, 3, 4, 5, 6, 7, 8]
    if(random.choice(listGemNumber) == 1):
        gem=Actor('gem/gemblue')
    elif(random.choice(listGemNumber) == 2):
        gem=Actor('gem/gemgreen')
    elif(random.choice(listGemNumber) == 3):
        gem=Actor('gem/gemred')
    elif(random.choice(listGemNumber) == 4):
        gem=Actor('gem/gemyellow')
    elif(random.choice(listGemNumber) == 5):
        gem=Actor('gem/hud_gem_blue')
    elif(random.choice(listGemNumber) == 6):
        gem=Actor('gem/hud_gem_green')
    elif(random.choice(listGemNumber) == 7):
        gem=Actor('gem/hud_gem_red')
    else:
        gem=Actor('gem/hud_gem_yellow')
    gem.x=200
    gem.y=0
    # Random playership
    listMeteorNumber = [1, 2, 3, 4, 5, 6, 7, 8]
    if(random.choice(listMeteorNumber) == 1):
        meto=Actor('./meteor/meteorbrown_big1')
    elif(random.choice(listMeteorNumber) == 2):
        meto=Actor('./meteor/meteorbrown_big2')
    elif(random.choice(listMeteorNumber) == 3):
        meto=Actor('./meteor/meteorbrown_big3')
    elif(random.choice(listMeteorNumber) == 4):
        meto=Actor('./meteor/meteorbrown_big4')
    elif(random.choice(listMeteorNumber) == 5):
        meto=Actor('./meteor/meteorgrey_big1')
    elif(random.choice(listMeteorNumber) == 6):
        meto=Actor('./meteor/meteorgrey_big2')
    elif(random.choice(listMeteorNumber) == 7):
        meto=Actor('./meteor/meteorgrey_big3')
    else:
        meto=Actor('./meteor/meteorgrey_big4')
    meto.x=400
    meto.y=0

def on_mouse_move(pos,rel,buttons):
    ship.x=pos[0]
    ship.y=pos[1]
def update():
    global score ,game_over
    gem.y=gem.y+4+score/4
    meto.y=meto.y+4+score/4
    if gem.y>600:
        gem.y=0
    if meto.y>600:
        meto.y=0
    if gem.colliderect(ship):
        gem.x=random.randint(20,780)
        gem.y=0
        score=score+1
        sounds.epe.play()
    if meto.colliderect(ship):
        game_over=True
        sounds.bumm.play()
        sounds.gameover.play()

def draw():
    screen.fill((0,0,0))
    if game_over:
        screen.draw.text('GAME OVER!',(360,300),color=(255,255,255),fontsize=60)
        screen.draw.text('Final score: '+str(score),(360,350),color=(255,0,255),fontsize=80)
    else:
      screen.draw.text('score: '+str(score),(10,15),color=(255,255,255),fontsize=60)
      ship.draw()
      gem.draw()
      meto.draw()
pgzrun.go()