def attack(damage, life):
    try:
        int(damage)
        int(life)
    except :
        raise TypeError
    return (life - range(2, damage))

def feu(damage, life):
    try:
        int(damage)
        int(life)
    except :
        raise TypeError
    return (life - range(5, damage))

def ice(damage, life):
    try:
        int(damage)
        int(life)
    except :
        raise TypeError
    return (life - range(5, damage))

def thunder(damage, life):
    try:
        int(damage)
        int(life)
    except :
        raise TypeError
    return (life - range(5, damage))

def potion(vie):
    vie += 25
    return vie % 50

