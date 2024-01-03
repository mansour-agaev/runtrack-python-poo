class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y


# Instanciation d'un point avec des valeurs initiales
point = Point(3, 5)

# Affichage des coordonnées du point
point.afficherLesPoints()

# Affichage de la coordonnée x et y
point.afficherX()
point.afficherY()

# Changement des valeurs de x et y
point.changerX(7)
point.changerY(10)

# Affichage des nouvelles coordonnées du point
point.afficherLesPoints()
