def waterState(f):
    if f <= 32:
        return "solid"
    elif 32 < f < 212:
        return "liquid"
    else:
        return "gas"
print (waterState(32))

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False
print (isDozen(45))

def toGerman(x):
    if x == "yes":
        return "ja"
    else:
        return "nein"
print (toGerman("yes"))

def stopLight(c):
    if c == "green":
        return "go"
    elif c == "yellow":
        return "slow"
    else:
        return "stop"
print (stopLight("red"))