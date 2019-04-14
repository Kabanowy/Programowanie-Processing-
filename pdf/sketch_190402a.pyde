nazwa = "obraz"
ext = ".jpg"
i = loadImage(nazwa+ext)
size (532,712)
print(type(i))
imageMode(CENTER)
image(i, width/2, height/2, width, height)
s = loadShape("okulary.svg")
shape(s, width/5, height/3, 320, 300)
save(nazwa+"edited"+ext)
