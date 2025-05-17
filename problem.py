def isLandscape(width, height):
    if width>height:
        return "Landscape"
    else:
        return "Portrait"
    
name = isLandscape(10, 20)
print(name)