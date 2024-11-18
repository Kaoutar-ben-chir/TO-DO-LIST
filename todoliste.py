# Liste pour stocker les tâches
taches = []

# Fonction Ajouter une tâche
def ajouter_tache():
    titre = input("Veuillez saisir la description de la tâche! : ")
    tache = {"Titre": titre, "Terminee": False}
    taches.append(tache)
    print(f"Tâche '{titre}' tâche ajoutée avec succès !")

# Fonction Afficher toutes les tâches
def afficher_taches():
    if not taches:
        print("Aucune tâche n'existe dans la liste.")
    else:
        print(" La liste des tâches :")
        for i, tache in enumerate(taches, start=1):
            etat = "Terminée" if tache["Terminee"] else "En cours"
            print(f"{i}. {tache['Titre']} [{etat}]")

# Fonction Marquer une tâche comme terminée
def terminer_tache():
    afficher_taches()
    index = int(input("Entrez le numéro de la tâche à marquer comme terminée : ")) - 1
    if 0 <= index < len(taches):
        taches[index]["Terminee"] = True
        print(f"Tâche '{taches[index]['Titre']}' marquée comme terminée.")
    else:
        print("Numéro invalide.")

# Fonction Supprimer une tâche
def supprimer_tache():
    afficher_taches()
    index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
    if 0 <= index < len(taches):
        tache = taches.pop(index)
        print(f"Tâche '{tache['Titre']}' supprimée avec succès.")
    else:
        print("Numéro invalide.")

# Programme principal
def main():
    while True:
        print("\nMenu :")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            terminer_tache()
        elif choix == "4":
            supprimer_tache()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
