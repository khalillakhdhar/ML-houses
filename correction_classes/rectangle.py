class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
    
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
# Création d'une instance de la classe Rectangle avec longueur=4 et largeur=2
rect = Rectangle(4, 2)

# Appel de la méthode aire() pour calculer l'aire du rectangle
aire_rect = rect.aire()
print("L'aire du rectangle est :", aire_rect)

# Appel de la méthode perimetre() pour calculer le périmètre du rectangle
perimetre_rect = rect.perimetre()
print("Le périmètre du rectangle est :", perimetre_rect)
