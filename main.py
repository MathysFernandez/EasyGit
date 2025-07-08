import tkinter as tk
from tkinter import ttk # ttk pour des widgets plus modernes (optionnel mais recommandé)
from Files import Saves
from Files import Git
import json
import os
import subprocess

def get_screen_resolution_tkinter():
    """
    Récupère la largeur et la hauteur de l'écran en pixels à l'aide de Tkinter.
    """
    fenetre = tk.Tk()       # Crée une fenêtre principale Tkinter
    fenetre.withdraw()      # La rend invisible (on n'a pas besoin de la voir)

    largeur_ecran = fenetre.winfo_screenwidth() - 1200 # Obtient la largeur de l'écran
    hauteur_ecran = fenetre.winfo_screenheight() - 400 # Obtient la hauteur de l'écran

    fenetre.destroy()       # Détruit la fenêtre temporaire pour libérer les ressources

    return largeur_ecran, hauteur_ecran

def clear_frame():
    """Détruit tous les widgets enfants du cadre principal pour changer de menu."""
    for widget in fenetre.winfo_children():
        widget.destroy()


def recuperer_texte_entree(champ_saisie, numero, event = None):
    # Récupère le widget qui a le focus (est actif) au moment de l'événement.
    chemin_saisi = champ_saisie.get()
    if not chemin_saisi == "":
        print(chemin_saisi)
        print(numero)
        print("tentative sauvegarde")
        Saves.ajouter_sauvegarde(numero, chemin_saisi)
        show_menu1()
    
    
def supprimer(numero):
    Saves.supprimer_sauvegarde(numero)
    show_menu1()
    

def Git_commit(chemin = "", champ_saisie_message_commit =""):
    message = champ_saisie_message_commit.get()
    
    if not chemin == "" and not message == "":
        Git.git_commit(chemin, message)
    
    

# Utilisation :
largeur_ecran, hauteur_ecran = get_screen_resolution_tkinter()


#Toute application Tkinter commence par une fenêtre racine, qui est la fenêtre principale de votre application.
fenetre = tk.Tk()

fenetre.title("EasyGit")
fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}+600+200") #Largeur x Hauteur

fenetre.configure(bg="white")

ttk.Style().theme_use("clam")


style = ttk.Style()
style.theme_use("alt")

style.configure("My.TLabelframe", background="white") # Utilise le code hexadécimal directement


style.configure("TButton", background="#C0C0C0") # Utilise le code hexadécimal directement
style.map("TButton",background=[
        ('active', '#808080'),  
        ('pressed', '#808080')])  


# --- 3. Configure le style "TEntry" ---
style.configure("TEntry",
    fieldbackground="#C0C0C0",  # Couleur de fond du champ de saisie (foncé)
    foreground="black",         # Couleur du texte tapé 
    insertbackground="black",   # Couleur du curseur de saisie 
    font=("Consolas", 12),      # Police et taille du texte
    borderwidth=1,              # Largeur de la bordure
    relief="solid",             # Style de la bordure (peut être "flat", "ridge", "groove", etc.)
    padding=(10,3) 
) 

# Définir l'état de la fenêtre sur 'zoomed' pour la maximiser
# Cela inclut généralement la barre de titre et permet à la barre des tâches de rester visible.
#fenetre.state('zoomed')


def show_menu1(event = None):
    utiliser1, chemin1, nom1 = Saves.charger_sauvegarde(1)
    utiliser1 = int(utiliser1)
    
    utiliser2, chemin2, nom2 = Saves.charger_sauvegarde(2)
    utiliser2 = int(utiliser2)
    
    utiliser3, chemin3, nom3 = Saves.charger_sauvegarde(3)
    utiliser3 = int(utiliser3)
    
    utiliser4, chemin4, nom4 = Saves.charger_sauvegarde(4)
    utiliser4 = int(utiliser4)
    
    
    """Affiche le contenu du Menu 1."""
    clear_frame() # Efface le contenu précédent

    # --- Colonne 1 ---
    frame_col1 = ttk.LabelFrame(fenetre, text="SAUVEGARDE", style="My.TLabelframe")
    frame_col1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configurer les lignes et colonnes du FRAME_COL1 pour qu'elles s'étirent
    # Cela permet aux boutons à l'intérieur de ce cadre de s'étirer
    frame_col1.grid_columnconfigure(0, weight=1) # La seule colonne du cadre prendra tout l'espace
    frame_col1.grid_rowconfigure(0, weight=1) # La première ligne pour bouton1_col1
    frame_col1.grid_rowconfigure(1, weight=1) 
    frame_col1.grid_rowconfigure(2, weight=1) 
    frame_col1.grid_rowconfigure(3, weight=1)
    
    if utiliser1:
        bouton1_col1 = ttk.Button(frame_col1, text = nom1, command=lambda: show_menu2(chemin1))
        bouton1_col1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        #Pour permettre à l'utilisateur de saisir du texte.
        champ_saisie1 = ttk.Entry(frame_col1, width=40) # <-- C'est ici que tu utilises .get()
        champ_saisie1.grid(row=0, column=0, padx=10, pady=10) # Ajouter sticky="nsew"
        # '<Return>' est l'événement qui correspond à la touche Entrée.
        # Lorsque cet événement se produit dans 'entry_champ', la fonction 'recuperer_texte_entree' est appelée.
        champ_saisie1.bind('<Return>', lambda event: recuperer_texte_entree(champ_saisie1,1, event))
    
    
    
    
    if utiliser2:
        bouton2_col1 = ttk.Button(frame_col1, text = nom2, command=lambda: show_menu2(chemin2))
        bouton2_col1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        #Pour permettre à l'utilisateur de saisir du texte.
        champ_saisie2 = ttk.Entry(frame_col1, width=40) # <-- C'est ici que tu utilises .get()
        champ_saisie2.grid(row=1, column=0, padx=10, pady=10) # Ajouter sticky="nsew"
        # '<Return>' est l'événement qui correspond à la touche Entrée.
        # Lorsque cet événement se produit dans 'entry_champ', la fonction 'recuperer_texte_entree' est appelée.
        champ_saisie2.bind('<Return>', lambda event: recuperer_texte_entree(champ_saisie2,2, event))
    
    
    
    
    
    if utiliser3:
        bouton3_col1 = ttk.Button(frame_col1, text = nom3, command=lambda: show_menu2(chemin3))
        bouton3_col1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        #Pour permettre à l'utilisateur de saisir du texte.
        champ_saisie3 = ttk.Entry(frame_col1, width=40) # <-- C'est ici que tu utilises .get()
        champ_saisie3.grid(row=2, column=0, padx=10, pady=10) # Ajouter sticky="nsew"
        # '<Return>' est l'événement qui correspond à la touche Entrée.
        # Lorsque cet événement se produit dans 'entry_champ', la fonction 'recuperer_texte_entree' est appelée.
        champ_saisie3.bind('<Return>', lambda event: recuperer_texte_entree(champ_saisie3,3, event))
    
    
    
    
    if utiliser4:
        bouton4_col1 = ttk.Button(frame_col1, text = nom4, command=lambda: show_menu2(chemin4))
        bouton4_col1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        #Pour permettre à l'utilisateur de saisir du texte.
        champ_saisie4 = ttk.Entry(frame_col1, width=40) # <-- C'est ici que tu utilises .get()
        champ_saisie4.grid(row=3, column=0, padx=10, pady=10) # Ajouter sticky="nsew"
        # '<Return>' est l'événement qui correspond à la touche Entrée.
        # Lorsque cet événement se produit dans 'entry_champ', la fonction 'recuperer_texte_entree' est appelée.
        champ_saisie4.bind('<Return>', lambda event: recuperer_texte_entree(champ_saisie4,4, event))
    






    # --- Colonne 2 ---
    frame_col2 = ttk.LabelFrame(fenetre, text="AJOUT / SUPRESSION", style="My.TLabelframe")
    frame_col2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Configurer les lignes et colonnes du FRAME_COL2 pour qu'elles s'étirent
    frame_col2.grid_columnconfigure(0, weight=1)
    frame_col2.grid_rowconfigure(0, weight=1)
    frame_col2.grid_rowconfigure(1, weight=1)
    frame_col2.grid_rowconfigure(2, weight=1)
    frame_col2.grid_rowconfigure(3, weight=1)
    
    
    
    
    
    if utiliser1:
        bouton1_col2 = ttk.Button(frame_col2, text="Supprimer", command=lambda: supprimer(1))
        bouton1_col2.grid(row=0, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        bouton1_col2 = ttk.Button(frame_col2, text="Ajouter", command = lambda: recuperer_texte_entree(champ_saisie1,1))
        bouton1_col2.grid(row=0, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    
    
    if utiliser2:
        bouton2_col2 = ttk.Button(frame_col2, text="Supprimer", command=lambda: supprimer(2))
        bouton2_col2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        bouton1_col2 = ttk.Button(frame_col2, text="Ajouter", command = lambda: recuperer_texte_entree(champ_saisie2,2))
        bouton1_col2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    
    
    if utiliser3:
        bouton3_col2 = ttk.Button(frame_col2, text="Supprimer", command=lambda: supprimer(3))
        bouton3_col2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        bouton3_col2 = ttk.Button(frame_col2, text="Ajouter", command = lambda: recuperer_texte_entree(champ_saisie3,3))
        bouton3_col2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
        
        
    if utiliser4:
        bouton4_col2 = ttk.Button(frame_col2, text="Supprimer", command=lambda: supprimer(4))
        bouton4_col2.grid(row=3, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    else:
        bouton4_col2 = ttk.Button(frame_col2, text="Ajouter", command = lambda: recuperer_texte_entree(champ_saisie4,4))
        bouton4_col2.grid(row=3, column=0, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    







    # Configurer le redimensionnement des colonnes et des lignes de la FENÊTRE PRINCIPALE
    fenetre.grid_columnconfigure(0, weight=4)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_rowconfigure(0, weight=1)








def show_menu2(chemin = ""):
    print(chemin)
    message = "test menu 2"
    
    
    
    """Affiche le contenu du Menu 2."""
    
    fenetre.bind("<Escape>",show_menu1)
    clear_frame() # Efface le contenu précédent
    
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_rowconfigure(0, weight=1)
    
    
    # --- Colonne 1 ---
    frame = ttk.LabelFrame(fenetre, text="GIT", style="My.TLabelframe")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configurer les lignes et colonnes du FRAME_COL1 pour qu'elles s'étirent
    # Cela permet aux boutons à l'intérieur de ce cadre de s'étirer
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)# La seule colonne du cadre prendra tout l'espace
    frame.grid_rowconfigure(0, weight=1) # La première ligne pour bouton1_col1
    frame.grid_rowconfigure(1, weight=1) 
    frame.grid_rowconfigure(2, weight=1) 
    frame.grid_rowconfigure(3, weight=1)

    # Bouton 1 - Colonne 1
    bouton1_col1 = ttk.Button(frame, text="GIT pull", command = lambda: Git.git_pull(chemin))
    bouton1_col1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"

    # Bouton 2 - Colonne 1
    bouton2_col1 = ttk.Button(frame, text="GIT add all", command = lambda: Git.git_add_all(chemin))
    bouton2_col1.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"
    
    # champ saisi 3 - Colonne 1
    champ_saisie_message_commit = ttk.Entry(frame)
    champ_saisie_message_commit.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    # Bouton 3 - Colonne 2
    bouton3_col2 = ttk.Button(frame, text="GIT commit", command = lambda: Git_commit(chemin, champ_saisie_message_commit))
    bouton3_col2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"

    # Bouton 4 - Colonne 1
    bouton4_col1 = ttk.Button(frame, text="GIT push", command = lambda: Git.git_push(chemin))
    bouton4_col1.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew") # Ajouter sticky="nsew"


    
    # Configurer le redimensionnement des colonnes et des lignes de la FENÊTRE PRINCIPALE
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=0)
    fenetre.grid_rowconfigure(0, weight=1)




# --- Démarrage de l'application ---
# Affiche le premier menu au lancement
show_menu1()

# Lancer la boucle principale de l'application
fenetre.mainloop()