class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial
    
    def depot(self, montant):
        self.solde += montant
    
    def retrait(self, montant):
        if montant > self.solde:
            print("Solde insuffisant.")
        else:
            self.solde -= montant
    
    def afficher_solde(self):
        print("Le solde actuel est de {} Dinar.".format(self.solde))
# Création d'une instance de la classe CompteBancaire avec un solde initial de 100 euros
compte = CompteBancaire(100)

# Affichage du solde actuel
compte.afficher_solde()  # Le solde actuel est de 100 euros.

# Dépôt de 50 euros sur le compte
compte.depot(50)

# Affichage du solde actuel après dépôt
compte.afficher_solde()  # Le solde actuel est de 150 euros.

# Retrait de 80 euros du compte
compte.retrait(80)

# Affichage du solde actuel après retrait
compte.afficher_solde()  # Le solde actuel est de 70 euros.

# Retrait de 100 euros du compte (solde insuffisant)
compte.retrait(100)  # Solde insuffisant.

# Affichage du solde actuel après retrait (qui n'a pas eu lieu)
compte.afficher_solde()  # Le solde actuel est de 70 euros.
