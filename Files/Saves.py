import json
import os
import sys
import os
import sys
import json

#Merci internet sinon cela n'aurais jamais pu fonctionner avec un executable 

# Cette fonction lit les RESSOURCES INITIES (ce qui est intégré à l'EXE)
def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Mode exécutable PyInstaller: les ressources sont dans _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Mode script Python: les ressources sont par rapport à la racine du projet
        # (easygit-ui/ est le dossier parent de Files/)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(project_root, relative_path)

# Cette fonction gère les chemins pour les SAUVEGARDES PERSISTANTES (lecture/écriture)
def get_save_file_path(numero):
    save_dir = ""
    if getattr(sys, 'frozen', False):
        # Pour l'exécutable: les sauvegardes sont stockées à côté de l'EXE
        save_dir = os.path.join(os.path.dirname(sys.executable), "SAVE")
    else:
        # Pour le script Python: les sauvegardes sont stockées dans le dossier SAVE à la racine du projet
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        save_dir = os.path.join(project_root, "SAVE")
    
    # Assure-toi que le dossier de sauvegarde existe avant d'essayer d'y lire/écrire
    os.makedirs(save_dir, exist_ok=True)
    return os.path.join(save_dir, f"Save{numero}.json")

# --- 2. FONCTIONS DE GESTION DES SAUVEGARDES ---

def charger_sauvegarde(numero = 1):
    data = {}
    # Initialise les valeurs de retour pour qu'elles aient toujours une valeur
    chemin = ""
    utiliser = "0" 
    name = f"Slot {numero} (vide)"

    # --- TENTATIVE 1 : LIRE DEPUIS L'EMPLACEMENT PERSISTANT (le plus important !) ---
    nom_fichier_persistant = get_save_file_path(numero) # <<< Appel de get_save_file_path ici
    try:
        with open(nom_fichier_persistant, "r") as f:
            data = json.load(f)
            # Si la lecture réussit, on met à jour les variables et on retourne immédiatement
            chemin = data.get("chemin_absolu", "")
            utiliser = data.get("utiliser", "0")
            name = data.get("name", f"Slot {numero} (vide)")
            print(f"DEBUG: Sauvegarde '{nom_fichier_persistant}' chargée depuis l'emplacement persistant.")
            return utiliser, chemin, name # <-- CLÉ: Retourne ici si la sauvegarde est trouvée !
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"DEBUG: Impossible de charger '{nom_fichier_persistant}' ({type(e).__name__}). Tente de lire l'original intégré.")

    # --- TENTATIVE 2 : SI LA LECTURE PERSISTANTE ÉCHOUE, LIRE LA VERSION INTÉGRÉE (valeurs par défaut) ---
    nom_fichier_integre = get_resource_path(os.path.join("SAVE", f"Save{numero}.json")) # <<< Appel de get_resource_path ici
    try:
        with open(nom_fichier_integre, "r") as f:
            data = json.load(f)
            # Met à jour les variables avec les valeurs de la version intégrée
            chemin = data.get("chemin_absolu", "")
            utiliser = data.get("utiliser", "0")
            name = data.get("name", f"Slot {numero} (vide)")
            print(f"DEBUG: Sauvegarde '{nom_fichier_integre}' chargée depuis l'exécutable intégré (valeurs par défaut).")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"DEBUG: Impossible de charger '{nom_fichier_integre}' (original intégré). Utilise les valeurs par défaut vides. Erreur: {e}")
        # data reste vide, les valeurs par défaut (définies au début) seront utilisées

    return utiliser, chemin, name # Retourne les valeurs finales (chargées ou par défaut)


def ajouter_sauvegarde(numero = 1, ajouter_chemin =""):
    nom_fichier_complet = get_save_file_path(numero) # <<< Appel de get_save_file_path ici pour l'écriture
    data = {}
    try:
        with open(nom_fichier_complet, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {} # Si non trouvé ou corrompu, on démarre avec un dict vide

    data["utiliser"] = "1"
    data["chemin_absolu"] = ajouter_chemin
    data["name"] = os.path.basename(ajouter_chemin)
    
    try:
        with open(nom_fichier_complet, "w") as f: # Utilisez "w" pour l'écriture
            json.dump(data, f, indent=4)
        print(f"DEBUG: Sauvegarde '{nom_fichier_complet}' écrite avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'écriture de la sauvegarde '{nom_fichier_complet}': {e}")


def supprimer_sauvegarde(numero = 1):
    nom_fichier_complet = get_save_file_path(numero) # <<< Appel de get_save_file_path ici pour l'écriture
    data = {}
    try:
        with open(nom_fichier_complet, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {} # Si non trouvé ou corrompu, on démarre avec un dict vide

    data["utiliser"] = "0"
    data["chemin_absolu"] = ""
    data["name"] = ""
    
    try:
        with open(nom_fichier_complet, "w") as f: # Utilisez "w" pour l'écriture
            json.dump(data, f, indent=4)
        print(f"DEBUG: Sauvegarde '{nom_fichier_complet}' supprimée/réinitialisée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de la sauvegarde '{nom_fichier_complet}': {e}")