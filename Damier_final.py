from tkinter import *
from tkinter import messagebox
from random import *

X = 20      # Taille du canvas en X
Y = 15      # Taille du canvas en Y
e = 20      # Taille d'une arête d'une case
C = 0       # Compteur du nombre de pions A
K = 0       # Compteur du nombre de pions B
ma=[[0 for j in range (Y)] for i in range(X)]  # Initialisation de la matrice
a, b = 0, 0        # Initialisation de a et b, les coordonnées aléatoires qui sélectionneront dans la matrice le placement des pions
nombrePionsB = 1    # Initialisation du nombre de pions B et A à afficher
nombrePionsA = 1
coulA, coulB = 'red', 'green' # Initialisation des variables servant à contenir les noms des couleurs

fen = Tk()      # Création de la fenêtre et des "ascenseurs" qui permettront de changer facilement la valeur du nombre de pions et de la taille du canevas
fen.title('Damier')
Xcanvas = Scale(fen,bg='light grey', activebackground='grey', orient = 'horizontal',length=150 ,label = 'Largeur du damier', from_=1, to=30)
Xcanvas.grid(row=0, column=1)
Ycanvas = Scale(fen,bg='light grey', activebackground='grey', orient = 'vertical',length=70, label = 'Hauteur du damier', from_=1, to=25)
Ycanvas.grid(row=0, column=2)
Nb_pionsA = Scale(fen, bg = 'light grey', activebackground='grey', orient='horizontal', length=110, label='Pions A ('+coulA+')', from_=1, to=20)
Nb_pionsA.grid(row=0, column=3)
Nb_pionsB = Scale(fen, bg = 'light grey', activebackground='grey', orient='horizontal', length=110, label='Pions B ('+coulB+')', from_=1, to=20)
Nb_pionsB.grid(row=0, column=4)



def net():              # Fonction de réinitialisation du canevas et des variables nécéssaires
    global C, K
    X = Xcanvas.get()
    Y = Ycanvas.get()
    C = 0
    K = 0
    can.delete(ALL)

def tracé_lignes():     # Fonction de tracé de la grille où les pions s'afficheront
    net()
    global Y, X, e
    X = Xcanvas.get()
    Y = Ycanvas.get()
    can.configure(height=Y*e,width=X*e)
    can.delete(ALL)
    for i in range(X):
        can.create_line(i*e,0,i*e,Y*e)
    for j in range(Y):
        can.create_line(0,j*e,X*e,j*e)



def pionr():            # Fonction de génération des pions A dans la matrice
    global C, ma, X, Y, a, b, nombrePionsA
    C = 0
    while C < nombrePionsA:
        a, b = randint(0 ,Y-1), randint(0, X-1)
        if ma[a][b] == 0:
            ma[a][b]=1
            C = C + 1

def pionv():            # Fonction de génération des pions B dans la matrice
    global K, ma, X, Y, a, b, nombrePionsB
    K = 0
    while K < nombrePionsB:
        a, b  = randint(0, Y-1), randint(0,X-1)
        if ma[a][b] == 0:
            ma[a][b]=2
            K = K + 1

def affpion():          # Fonction de génération des pions dans le canevas
    global X, Y, ma, e, nombrePionsA, nombrePionsB, coulA, coulB
    ma=[[0 for j in range(X)] for i in range(Y)]
    nombrePionsB = Nb_pionsB.get()
    nombrePionsA = Nb_pionsA.get()
    if (nombrePionsA + nombrePionsB) <= (X*Y):
        Erreur.grid_forget()
        pionv()
        pionr()
        for i in range(Y):
            for j in range(X):
                if ma[i][j]==1:
                    can.create_oval(e*j+3,e*i+3,(e*j)+e-3,(e*i)+e-3,fill=coulA)
                if ma[i][j]==2:
                    can.create_oval(e*j+3,e*i+3,(e*j)+e-3,(e*i)+e-3,fill=coulB)
        ma=[[0 for j in range(X)] for i in range(Y)]
    else :
        Erreur.grid(row=6, column = 1, columnspan=3)


def Choix_couleurs():
    global coulA, coulB
    txtCOLORa.grid(row =0, column =7 , sticky='n')
    txtCOLORb.grid(row=2, column=7, sticky='n')
    COLORa.grid(row=1, column = 7, sticky='n')
    COLORb.grid(row=3, column = 7, sticky='n')
    ValiderCoul.grid(row=4, column =7, sticky='n')

def Verifcouleurs():
    global coulA, coulB
    coulA = COLORa.get()
    coulB = COLORb.get()
    COLORa.grid_forget()
    COLORb.grid_forget()
    COLORa.delete(0,END)
    COLORb.delete(0,END)
    txtCOLORa.grid_forget()
    txtCOLORb.grid_forget()
    ValiderCoul.grid_forget()
    if coulA == 'rouge':
        coulA = 'red'
    elif coulA == 'vert':
        coulA = 'green'
    elif coulA == 'bleu':
        coulA = 'blue'
    elif coulA == 'blanc':
        coulA = 'white'
    elif coulA == 'noir':
        coulA = 'black'
    elif coulA == 'jaune':
        coulA = 'yellow'
    else:
        coulA = 'red'
        messagebox.showerror(" Erreur"," La couleur entrée en A n'est pas répertoriée")

    if coulB == 'rouge':
        coulB = 'red'
    elif coulB == 'vert':
        coulB = 'green'
    elif coulB == 'bleu':
        coulB = 'blue'
    elif coulB == 'blanc':
        coulB = 'white'
    elif coulB == 'noir':
        coulB = 'black'
    elif coulB == 'jaune':
        coulB = 'yellow'
    else:
        coulB='green'
        messagebox.showerror(" Erreur"," La couleur entrée en B n'est pas répertoriée")
    Nb_pionsA.configure(label='Pions A ('+coulA+')')
    Nb_pionsB.configure(label='Pions B ('+coulB+')')

can = Canvas(fen,height=Y*e,width=X*e, bg='white')              # Création du canevas et des widgets nécéssaires à l'utilisation des fonctions
can.grid(row=1, column=1, columnspan = 6, rowspan=4)
bouDamier = Button(fen, text = 'Afficher Damier', command = tracé_lignes)
bouDamier.grid(row=5, column=1)
bouQuitter = Button(fen,text='Quitter', command=fen.destroy)
bouQuitter.grid(row=5, column=6)
afficher_pion = Button(fen,text='afficher pions',command=affpion)
afficher_pion.grid(row=5,column=2)
nettoyer = Button(fen, text='Réinitialisation',command=net)
nettoyer.grid(row=5,column=3)
Couleurs = Button(fen, text='Choix des couleurs', command=Choix_couleurs)
Couleurs.grid(row=5, column=5)
ValiderCoul = Button(fen, text='Valider', command=Verifcouleurs)
Erreur = Label(fen, text=''' Il n'y a pas assez de cases pour le nombre de pions demandé''', fg = 'red')

COLORa = Entry(fen)
COLORb = Entry(fen)
txtCOLORa = Label(fen, text='Couleur des pions A (rouge, vert, jaune, bleu, noir, blanc)')
txtCOLORb = Label(fen, text='Couleur des pions B (rouge, vert, jaune, bleu, noir, blanc)')


fen.mainloop()
