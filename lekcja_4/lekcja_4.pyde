def setup():
    size(400, 400)
    textSize(50)
    textAlign(CENTER)
def draw():
    text("hehe", width/2, (height/3)*2)
    print(mouseX, mouseY)
    print(hex(get(100, 100)))
    print(CODED)
    if keyPressed:
        fill(105,255,0)
        #miały być dwie strzałki, inicjały i możliwość wyboru liter na klawiaturze + zaznaczenia myszą przez najechanie
        #więc więcej warunków i to zagnieżdżaonych
        if keyCode == 39 and mouseX>=260 and mouseX<=370 and mouseY>=230 and mouseY<=260:
            fill(0)
        text("beka", width/2+120, (height/3)*2)
        fill(255,50,30)
        
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.noStroke()
    s.vertex(120, 300)
    s.vertex(56, 59)
    s.vertex(50, 50)
    s.vertex(50, 0)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    
    
    
