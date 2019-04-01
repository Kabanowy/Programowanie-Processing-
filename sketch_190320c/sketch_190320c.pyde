def setup ():
    import random
    frameRate(30)
    rectMode(CORNER)
    size(200,200)
    strokeWeight(0)
    stroke(255,255,0)
    global x
    global y
    x = 0
    y = 0 
def draw():
    fill(random(255),random(255),random(255))  #poszedłeś na łatwiznę z kolorami
    background(0)
    global x
    x=x+1  #założenia co do ruchu były nieco inne
    global y
    y=y+1
    rect(x,y,50,50)
    if x > width:
        exit()
    


    



    