import random

def Comp_game(c,d):
    c=random.randint(1,3)
    if c==1:
        c='s'
    elif c==2:
        c='p'
    else :
        c='k'

    if c=="s":
        if d=="p":
            A=False
        else:
            A=True
    elif c=="p":
        if d=="k":
            A=False
        else:
            A=True
    elif c=="k":
        if d=="s":
            A=False
        else:
            A=True
    if A==True:
        print ("Computer won!")
    else:
        print("Player won!")
    return


def game(a,b):
    if a=="s":
        if b=="p":
            A=False
        else:
            A=True
    elif a=="p":
        if b=="k":
            A=False
        else:
            A=True
    elif a=="k":
        if b=="s":
            A=False
        else:
            A=True
    if A==True:
        print ("Player 1 won!")
    else:
        print("Player 2 won!")
    return

choose=input("Do you want to play with a player 'p' or computer 'c'?: ")
if choose=='p':
    a=input("Player 1 turn: Enter Stone(s) Paper(p) or Scissors(k): ")
    b=input("Player 2 turn: Enter Stone(s) Paper(p) or Scissors(k): ")
    game(a,b)
else:
    c=print("Computers' turn: ")
    d=input("Players' turn: Enter Stone(s) Paper(p) or Scissors(k): ")
    Comp_game(c,d)