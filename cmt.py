import re

def lire_fichier(chemin):
    try:
        with open(chemin, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
        return None

def comment_rm(chemin,c):
    regex = r'^#.*$'
    r = lire_fichier(chemin)
    lines=r.split('\n')
    for line in lines:
        if not re.match(regex, line):
            c.write(line +'\n')
            

def main():
    #chemin_fichier = input("Entrez le chemin d'accès au fichier : ")
    chemin_fichier ="C:\\Users\\ULTRA PC\\OneDrive\\Bureau\\testpy\\code.txt"
    c=open('C:\\Users\\ULTRA PC\\OneDrive\\Bureau\\testpy\\Nocommentfich.txt','w')
    comment_rm(chemin_fichier,c)
    c.close()
    t=open(chemin_fichier,'r')
    print(t)
    t.close()

if __name__ == "__main__":
    main()
