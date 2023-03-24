class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def parler(self):
        print("{} {} est en train de parler.".format(self.prenom, self.nom))

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, niveau):
        super().__init__(nom, prenom, age)
        self.niveau = niveau
# Création d'une instance de la classe Personne
personne = Personne("Salim", "Hamdi", 30)

# Appel de la méthode parler()
personne.parler()

# Création d'une instance de la classe Etudiant
etudiant = Etudiant("Sami", "Ben Ahmed", 20, "Licence")

# Appel de la méthode parler() pour l'étudiant
etudiant.parler()

# Accès à l'attribut niveau de l'étudiant
print("{} {} est en {}.".format(etudiant.prenom, etudiant.nom, etudiant.niveau))
