import os
import subprocess


def git_pull(chemin: str) -> bool:
    print("--pull--")
    # Vérifier si le chemin existe et est un répertoire
    if not os.path.isdir(chemin):
        #print(f"Erreur : Le chemin '{chemin}' n'existe pas ou n'est pas un répertoire.")
        return False

    # Vérifier si c'est bien un dépôt Git
    if not os.path.isdir(os.path.join(chemin, ".git")):
        #print(f"Erreur : '{chemin}' ne semble pas être un dépôt Git valide (pas de répertoire .git trouvé).")
        return False
    
    try:
        # Exécuter la commande 'git pull'
        # cwd=chemin : exécute la commande dans le répertoire du dépôt
        # capture_output=True : capture la sortie standard et d'erreur
        # text=True : décode la sortie en texte (str)
        # check=True : lève une CalledProcessError si la commande échoue (code de retour non nul)
        result = subprocess.run(
            ["git", "pull"],
            cwd=chemin,
            capture_output=True,
            text=True,
            check=True
        )

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("(git pull) Erreur standard :\n", result.stderr)
        return True

    except subprocess.CalledProcessError as e:
        print(f"\nErreur : La commande 'git pull' a échoué dans '{chemin}'.")
        print(f"Code de retour : {e.returncode}")
        print(f"Sortie standard :\n{e.stdout}")
        print(f"Erreur standard :\n{e.stderr}")
        return False
    
    except FileNotFoundError:
        print("\nErreur : La commande 'git' n'a pas été trouvée.")
        print("Veuillez vous assurer que Git est installé et accessible dans votre PATH.")
        return False
    
    except Exception as e:
        print(f"\nUne erreur inattendue s'est produite lors du 'git pull' : {e}")
        return False
    
    



def git_add_all(chemin: str) -> bool:
    print("--add all--")
    # Vérifier si le chemin existe et est un répertoire
    if not os.path.isdir(chemin):
        #print(f"Erreur : Le chemin '{chemin}' n'existe pas ou n'est pas un répertoire.")
        return False

    # Vérifier si c'est bien un dépôt Git
    if not os.path.isdir(os.path.join(chemin, ".git")):
        #print(f"Erreur : '{chemin}' ne semble pas être un dépôt Git valide (pas de répertoire .git trouvé).")
        return False

    try:
        # Exécuter la commande 'git add .'
        # cwd=chemin : exécute la commande dans le répertoire du dépôt
        # capture_output=True : capture la sortie standard et d'erreur
        # text=True : décode la sortie en texte (str)
        # check=True : lève une CalledProcessError si la commande échoue (code de retour non nul)
        result = subprocess.run(
            ["git", "add", "."],  # La commande pour 'git add .'
            cwd=chemin,
            capture_output=True,
            text=True,
            check=True
        )

        if result.stderr:
            print("(git add all) Erreur standard :\n", result.stderr)
        if result.stdout: # Normalement, 'git add .' n'a pas beaucoup de sortie standard en cas de succès
            print(result.stdout)
        
        return True

    except subprocess.CalledProcessError as e:
        print(f"\nErreur : La commande 'git add .' a échoué dans '{chemin}'.")
        print(f"Code de retour : {e.returncode}")
        print(f"Sortie standard :\n{e.stdout}")
        print(f"Erreur standard :\n{e.stderr}")
        return False
    except FileNotFoundError:
        print("\nErreur : La commande 'git' n'a pas été trouvée.")
        print("Veuillez vous assurer que Git est installé et accessible dans votre PATH.")
        return False
    except Exception as e:
        print(f"\nUne erreur inattendue s'est produite lors du 'git add .' : {e}")
        return False
    
    





def git_commit(chemin: str, message: str) -> bool:
    print("--commit--")
    # Vérifier si le chemin existe et est un répertoire
    if not os.path.isdir(chemin):
        #print(f"Erreur : Le chemin '{chemin}' n'existe pas ou n'est pas un répertoire.")
        return False

    # Vérifier si c'est bien un dépôt Git
    if not os.path.isdir(os.path.join(chemin, ".git")):
        #print(f"Erreur : '{chemin}' ne semble pas être un dépôt Git valide (pas de répertoire .git trouvé).")
        return False

    # Vérifier si un message de commit est fourni
    if not message.strip():
        #print("Erreur : Le message de commit ne peut pas être vide.")
        return False

    try:
        # Exécuter la commande 'git commit -m "Votre message"'
        # cwd=chemin: exécute la commande dans le répertoire du dépôt
        # capture_output=True: capture la sortie standard et d'erreur
        # text=True: décode la sortie en texte (str)
        # check=True: lève une CalledProcessError si la commande échoue (code de retour non nul)
        result = subprocess.run(
            ["git", "commit", "-m", message],  # La commande pour 'git commit -m'
            cwd=chemin,
            capture_output=True,
            text=True,
            check=True
        )

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("(git commit) Erreur standard :\n", result.stderr)
        return True

    except subprocess.CalledProcessError as e:
        print(f"\nErreur : La commande 'git commit' a échoué dans '{chemin}'.")
        print(f"Code de retour : {e.returncode}")
        print(f"Sortie standard :\n{e.stdout}")
        print(f"Erreur standard :\n{e.stderr}")
        
        # Cas spécifique : rien à commiter
        if "nothing to commit" in e.stderr.lower() or "no changes added to commit" in e.stderr.lower():
            print("Astuce : Il n'y a rien à commiter. Assurez-vous d'avoir ajouté des fichiers avec 'git add .' au préalable.")
        return False
    except FileNotFoundError:
        print("\nErreur : La commande 'git' n'a pas été trouvée.")
        print("Veuillez vous assurer que Git est installé et accessible dans votre PATH.")
        return False
    except Exception as e:
        print(f"\nUne erreur inattendue s'est produite lors du 'git commit' : {e}")
        return False
    












def git_push(chemin: str) -> bool:
    print("--push--")
    # Vérifier si le chemin existe et est un répertoire
    if not os.path.isdir(chemin):
        #print(f"Erreur : Le chemin '{chemin}' n'existe pas ou n'est pas un répertoire.")
        return False

    # Vérifier si c'est bien un dépôt Git
    if not os.path.isdir(os.path.join(chemin, ".git")):
        #print(f"Erreur : '{chemin}' ne semble pas être un dépôt Git valide (pas de répertoire .git trouvé).")
        return False

    try:
        # Exécuter la commande 'git push'
        # cwd=chemin : exécute la commande dans le répertoire du dépôt
        # capture_output=True : capture la sortie standard et d'erreur
        # text=True : décode la sortie en texte (str)
        # check=True : lève une CalledProcessError si la commande échoue (code de retour non nul)
        result = subprocess.run(
            ["git", "push"],
            cwd=chemin,
            capture_output=True,
            text=True,
            check=True
        )
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("(git push) Erreur standard :\n", result.stderr)
        return True

    except subprocess.CalledProcessError as e:
        print(f"\nErreur : La commande 'git push' a échoué dans '{chemin}'.")
        print(f"Code de retour : {e.returncode}")
        print(f"Sortie standard :\n{e.stdout}")
        print(f"Erreur standard :\n{e.stderr}")
        
        # Cas spécifiques pour le push
        if "no upstream branch" in e.stderr.lower():
            print("Astuce : Aucune branche amont n'est configurée. Essayez 'git push --set-upstream origin <nom_de_branche>'.")
        elif "failed to push some refs to" in e.stderr.lower() or "rejected" in e.stderr.lower():
            print("Astuce : Le push a été rejeté. Il se peut que vous ayez besoin de faire un 'git pull' d'abord pour résoudre des conflits ou récupérer des changements distants.")
        elif "authentication failed" in e.stderr.lower() or "could not read username" in e.stderr.lower():
            print("Astuce : Échec d'authentification. Vérifiez vos identifiants ou vos droits d'accès.")
        
        return False
    except FileNotFoundError:
        print("\nErreur : La commande 'git' n'a pas été trouvée.")
        print("Veuillez vous assurer que Git est installé et accessible dans votre PATH.")
        return False
    
    except Exception as e:
        print(f"\nUne erreur inattendue s'est produite lors du 'git push' : {e}")
        return False
    
    
    
    
    
    
    
"""    
if git_pull("C:\\Users\\mathy\\Desktop\\EasyGit\\easygit-ui"):
    print("Opération de pull terminée avec succès pour le dépôt valide.")
else:
    print("Échec de l'opération de pull pour le dépôt valide.")
"""

#git_pull("C:\\Users\\mathy\\Desktop\\EasyGit\\easygit-ui")
#git_add_all("C:\\Users\\mathy\\Desktop\\EasyGit\\easygit-ui")
#git_commit("C:\\Users\\mathy\\Desktop\\EasyGit\\easygit-ui", "rename git")
#git_push("C:\\Users\\mathy\\Desktop\\EasyGit\\easygit-ui")
