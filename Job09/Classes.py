class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom du produit : {self.nom}\n"
        infos += f"Prix HT : {self.prixHT} euros\n"
        infos += f"TVA : {self.TVA}%\n"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 15)

# Calcul et affichage des prix TTC des produits
print("Prix TTC du produit 1:", produit1.calculerPrixTTC())
print("Prix TTC du produit 2:", produit2.calculerPrixTTC())

# Modification du nom et du prix des produits
produit1.modifierNom("PC portable")
produit1.modifierPrixHT(900)

produit2.modifierNom("Smartphone")
produit2.modifierPrixHT(600)

# Affichage des nouvelles informations des produits
print("\nNouveau nom du produit 1:", produit1.obtenirNom())
print("Nouveau prix HT du produit 1:", produit1.obtenirPrixHT())
print("Nouveau nom du produit 2:", produit2.obtenirNom())
print("Nouveau prix HT du produit 2:", produit2.obtenirPrixHT())
