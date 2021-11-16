from typing import Counter
import actions

def Turn_Player(life, inventory, enemy):
    while(True):
        choise = input("Quel action voulez-vous faire :\n1 : Attaque simple\n2 : Utiliser Parchemin\n3 : Utiliser Potion\n4 : Sauvegarder\n5 : Quitter")
        try :
            choise = int(choise)
        except:
            raise TypeError
        if (choise == 1):
            cnt = 1
            for life in enemy :
                print(cnt, "Enemie", cnt,":", life, "pv")
            pass
        elif (choise == 2):
            pass
        elif (choise == 3):
            pass
        elif (choise == 4):
            break
        elif (choise == 5):
            break
        else:
            raise ValueError