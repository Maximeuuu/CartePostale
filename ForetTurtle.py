"""
Auteur    : Maxime
Nom       : foret.py
Date      : 10 novembre 2020
Version   : 5.5
But       : Dessine une foret de sapin en pleine nuit etoilee.
Fonctions : fenetre(),arreter(),triangle(x,y,c),tronc(x,y,l),sapin(x,y,c),
             foret(nb_sapin),etoile(x,y,t,nb_branches),lune(),etoile_brille(),
             ciel(nb_etoiles),decors()
"""

from turtle import *
from random import randint,randrange
from math import sqrt
from time import sleep

#creation d'une liste contenant les caracteristiques de chaques etoiles
liste_etoileGlobale=[]

#taille de l'ecran
largeurAffichage=1000
hauteurAffichage=500


def fenetre():
    """
    Permet de donner les propriétés générale de la fenêtre et de la tortue.
    """
    setup(largeurAffichage,hauteurAffichage+100)
    title("Foret")
    speed(0)
    delay(0)
    ht()
    colormode(255)


def arreter():
    """
    Permet d'empecher un bug de la fenetre lors de la fermeture.
    """
    exitonclick()
    try:
        exitonclick()
    except Terminator:
        pass


def triangle(x,y,c):
    """
    Dessine un triangle de coordonnees x,y et de cote c correspondant a un etage
     de branche du sapin.
    """
    up()
    goto(x,y)
    down()

    begin_fill()
    for i in range(3):
        forward(c)
        left(120)
    end_fill()


def tronc(x,y,l):
    """
    Dessine un rectangle de coordonnées x,y et de largeur l correspondant au
     tronc du sapin.
    """
    up()
    goto(x,y)
    down()
    fillcolor(86,44,12)
    begin_fill()
    for i in range(2):
        forward(l)
        right(90)
        forward(l*1.5)
        right(90)
    end_fill()


def sapin(x,y,c):
    """
    Dessine un sapin en appelant 3 fois la fonction triangle() et 1 fois tronc().
    """
    tronc(x+0.375*c,y,0.25*c)
    begin_fill()
    teinte_verte=0,160-c,0 #couleur en fonction de la taille
    fillcolor(teinte_verte)

    for i in range(3):
        triangle(x,y,c)
        x=x+0.125*c
        y=y+0.3*c
        c=0.75*c
    end_fill()


def foret(nb_sapin):
    """
    Dessine une foret en utilisant la fonction sapin() le nombre de fois que
     l’utilisateur a choisit (nb_sapin).
    """
    nombreSapin=0
    setheading(0)

    racineCarre=int(sqrt(nb_sapin)) #la racine carre va etre beaucoup utilise
    for y in range(racineCarre):
        for x in range(racineCarre):

            c=randint(40,120)#taille aleatoire

            #calcul permettant de ne pas supperposer les sapins
            cooY=int(-10-y*(hauteurAffichage/2/racineCarre))
            cooX=randint(-largeurAffichage/2,largeurAffichage/2-c)
            cooY=randint(int(cooY-(racineCarre/2)),int(cooY+(racineCarre/2)))

            sapin(cooX,cooY,c)
            nombreSapin+=1 #compteur de sapin

    #ajoute les sapins manquants sur une derniere ligne
    if nombreSapin<nb_sapin:
        sapinsManquants=nb_sapin-nombreSapin
        for x in range(sapinsManquants):

            c=randint(40,120)#taille aleatoire

            #calcul permettant de ne pas supperposer les sapins
            cooY=int(-10-(y+1)*(hauteurAffichage/2/racineCarre))
            cooX=randint(-largeurAffichage/2,largeurAffichage/2-c)
            cooY=randint(int(cooY-(racineCarre/2)),int(cooY+(racineCarre/2)))

            sapin(cooX,cooY,c)


def etoile(x,y,t,nb_branches):
    """
    Dessine les differentes etoiles de coordonees x,y ; de taille t et de
     nombres de branches nb_branches.
    """
    up()
    goto(x,y)
    setheading(0)
    begin_fill()
    down()

    angle=180-180/nb_branches #calcul permettant creer une etoile avec nb_branches
    for _ in range(nb_branches):
        forward(t)
        right(angle-360/nb_branches)
        forward(t)
        left(angle)

    end_fill()


def lune():
    """
    Dessine une lune.
    """
    up()
    goto(largeurAffichage/2-60,hauteurAffichage/2-30)
    down()
    fillcolor(244,244,244)
    begin_fill()
    circle(30,360)
    end_fill()

    up()
    goto(largeurAffichage/2-75,hauteurAffichage/2-30)
    down()
    fillcolor(10,2,40)
    begin_fill()
    circle(30,360)
    end_fill()


def etoile_brille():
    """
    Permet de faire scintiller quelques etoiles à la fin du programme.
    """
    for _ in range(50): #plus ou moins 10 secondes

        #choisit une etoile aleatoire parmi la liste
        etoileA=randrange(0,len(liste_etoileGlobale),4)

        #caracteristiques d'une etoile
        x=liste_etoileGlobale[etoileA]
        y=liste_etoileGlobale[etoileA+1]
        t=liste_etoileGlobale[etoileA+2]
        nb_branches=liste_etoileGlobale[etoileA+3]

        fillcolor(10,2,40)
        etoile(x,y,t,nb_branches) #efface une etoile
        sleep(0.1) #attend 0.1 seconde
        end_fill()
        for _ in range(4*nb_branches+1): #annule l'"effacement"
            undo()


def ciel(nb_etoiles):
    """
    Dessine le ciel, la lune et les étoiles en appelant lune() et etoile() en
     fonction du nombre d'etoiles (nb_etoiles).
    """

    up()
    goto(-(largeurAffichage/2),0)
    down()
    fillcolor(10,2,40)
    begin_fill()
    for _ in range(2):
        forward(largeurAffichage)
        left(90)
        forward(hauteurAffichage/2+100)
        left(90)
    end_fill()

    lune()

    for _ in range(nb_etoiles):
        x=randint(-largeurAffichage/2,largeurAffichage/2-18) #coordonee x aleatoire
        y=randint(30,hauteurAffichage/2) #coordonnee y aleatoire
        t=randint(5,12) #taille aleatoire
        nb_branches=randint(5,10) #type_etoile

        #ajoute les caracteristiques de chaques etoile dans une liste
        liste_etoileGlobale.append(x)
        liste_etoileGlobale.append(y)
        liste_etoileGlobale.append(t)
        liste_etoileGlobale.append(nb_branches)

        fillcolor("yellow")
        etoile(x,y,t,nb_branches)

def neige():
    """
    dessine des flocons de neiges tombant du ciel (ne fontionne pas)
    """
    liste_flocon=[]
    nb_flocon_dessine=0
    nb_flocon=int(largeurAffichage*12/1000) #proportions de flocons
    color("grey")
    fillcolor("grey")
    for etage in range(15):
        for _ in range(1,nb_flocon):
            x=randrange(-largeurAffichage/2,largeurAffichage/2)
            y=hauteurAffichage+etage*-50
            liste_flocon.append(x)
            liste_flocon.append(y)

        print(len(liste_flocon)/2)
        for i in range(int(len(liste_flocon)/2)):
            up()
            goto(liste_flocon[i*2],liste_flocon[i*2+1])
            down()
            begin_fill()
            circle(10,360)
            end_fill()
        for _ in range(nb_flocon):
            undo()
        sleep(2)


def decors():
    """
    Demande à l’utilisateur le nombre de sapin et le nombre d’etoiles qu’il
     souhaite et appelle les fonctions fenetre(), ciel(), foret(),
     etoile_brille() puis arreter().
    """
    nb_sapin=int(input("Combien de sapins ? "))
    nb_etoiles=int(input("Combien d'étoiles ? "))
    fenetre()
    tracer(100,0)
    ciel(nb_etoiles)
    foret(nb_sapin)
    #etoile_brille()

    """
    neige()
    """
    arreter()


#execute le programme
decors()
