import re

def lire_fichier(chemin):
    try:
        with open(chemin, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
        return None

def identifier_accepte(identifiant):
    regex = r'^[a-zA-Z]\w*$'
    return re.match(regex, identifiant) is not None

def main():
    #chemin_fichier = input("Entrez le chemin d'accès au fichier : ")
    chemin_fichier ="C:\Data\PythonProjects\P1\code02.txt"
    contenu = lire_fichier(chemin_fichier)

    if contenu:
        identifiants = contenu.split()
        acceptes = []
        non_acceptes = []

        for identifiant in identifiants:
            if identifier_accepte(identifiant):
                acceptes.append(identifiant)
            else:
                non_acceptes.append(identifiant)

        print("Nombre d'identifiants acceptés :", len(acceptes))
        print("Identifiants acceptés :", acceptes)
        print("Nombre d'identifiants non acceptés :", len(non_acceptes))
        print("Identifiants non acceptés :", non_acceptes)

if __name__ == "__main__":
    main()
