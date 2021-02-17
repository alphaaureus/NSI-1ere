from tkinter import *
import random

# Nombre total de tentative
tentative = 10

# On génère un nombre aléatoire compris entre 1 et 99
answer = random.randint(1, 99)

def check_answer():
    global tentative
    global text

    # A chaque mauvaise réponse, on perd une tentative
    tentative -= 1

    # Entrer une valeur
    guess = int(entry_window.get())

    # Les différentes réponses
    if answer == guess:
        text.set("Gagné!!!")
        btn_check.pack_forget()
    # Quand le joueur n'as plus de tentative
    elif tentative == 0:
        text.set("Perdu, tu n'as plus de tentative'")
        btn_check.pack_forget()
    # Quand le joueur donne un nombre plus petit que la réponse
    elif guess < answer:
        text.set("Faux - Il te reste " + str(tentative) + " tentatives restanstes - PLUS GRAND")
        entry_window.delete(0, END)
    # Quand le joueur donne un nombre plus grand que la réponse
    elif guess > answer:
        text.set("Faux - Il te reste " + str(tentative) + " tentatives restantes - PLUS PETIT")
        entry_window.delete(0, END)
    return


root = Tk()
# Titre de la page
root.title("Trouves le bon nombre")

# Taille de la fenêtre
root.geometry("1200x800")

# Règle du jeu
label = Label(root, text="Trouves le bon nombre compris entre 1 et 99.")
label.pack()

# Case pour écrire
entry_window = Entry(root, width=100, borderwidth=8)
entry_window.pack()
# Le bouton pour proposer une réponse
btn_check = Button(root, text="Ok", command=check_answer)
btn_check.pack()
# Le bouton quitter
btn_quit = Button(root, text="Quitter", command=root.destroy)
btn_quit.pack()

# Affichage du début
text = StringVar()
text.set("Tu as 10 tentatives. Bonne chance!!!")
guess_tentative = Label(root, textvariable=text)
guess_tentative.pack()

root.mainloop()
