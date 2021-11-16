def prog():
    life = 20
    enemy = list()
    inventory = {"Potion":3, "Fire":0, "Thunder":0, "Ice":0}
    while (True):
        choise = input('1 : Nouvelle partie\n2 : Charger partie\n3 : Afficher score\n4 : Quitter\nChoix = ')
        try :
            choise = int(choise)
        except:
            raise TypeError
        if (choise == 1):
            pass
        elif (choise == 2):
            pass
        elif (choise == 3):
            pass
        elif (choise == 4):
            break
        else:
            raise ValueError

prog()
