from PIL import Image, ImageDraw

class PremierPlan:
    """
    Classe pour dessiner des éléments dans le premier plan de l'image(harbre, soleil, oiseau).

    :param int x: Coordonnée x.
    :param int y: Coordonnée y.
    :param int dim: Dimension de l'objet.

    Exemple:
    ::
    
        img = Image.new("RGB", (1200, 1200), color="DarkTurquoise")
        ctx = ImageDraw.Draw(img)

        c = PremierPlan(0, 0, 50)

        c.soleil(ctx, 50, 50, 50)
        c.dessiner_arbre(ctx)
        c.oiseau(ctx)

        img.save("dessin.png")
    """
    def __init__(self, x, y, dim):
        self.x, self.y = x, y 
        self.dim = dim
    
    def soleil(self, ctx, rayon, decalage_x, decalage_y):
        """
        Dessine un soleil sur l'image.

        :param ctx: Contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw
        :param int rayon: Rayon du soleil.
        :param int decalage_x: Décalage horizontal du bord de l'image(pour éviter que le soleil soit collé au bordure).
        :param int decalage_y: Décalage vertical du bord de l'image(pour éviter que le soleil soit collé au bordure).
        """
        largeur, hauteur = ctx.im.size
        centre_x, centre_y = largeur - rayon - decalage_x, rayon + decalage_y
        x0 = centre_x - rayon
        y0 = centre_y - rayon
        x1 = centre_x + rayon
        y1 = centre_y + rayon
        ctx.pieslice([(x0, y0), (x1, y1)], 0, 360, fill="Yellow")
    
    def dessiner_arbre(self, ctx):
        """
        Dessine un arbre sur l'image.

        :param ctx: contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw
        """
        largeur, hauteur = ctx.im.size
        # Coordonnée du début
        arbre_x = 50  # Décalage X
        arbre_y = hauteur - 200  # Décalage Y

        # Tronc d'arbre
        tronc_x1, tronc_y1 = arbre_x + 60, arbre_y + 120
        tronc_x2, tronc_y2 = tronc_x1 + 40, tronc_y1 + 100
        ctx.rectangle([tronc_x1, tronc_y1, tronc_x2, tronc_y2], fill="brown")

        # Feuille de l'arbre
        couronne_x1, couronne_y1 = arbre_x, arbre_y
        couronne_x2, couronne_y2 = arbre_x + 160, arbre_y + 120
        ctx.rectangle([couronne_x1, couronne_y1, couronne_x2, couronne_y2], fill="green")
        
    def oiseau(self, ctx, color="black"):
        """
        Dessine un oiseau sur l'image.

        :param ctx: Contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw
        :param str color: Couleur de l'oiseau.
        """
        largeur, hauteur = ctx.im.size
        oiseau_x = 100
        oiseau_y = 200
        oiseau_x1 = oiseau_x + 50
        oiseau_y1 = oiseau_y + 50
        ctx.line([(oiseau_x, oiseau_y),
                  (oiseau_x1, oiseau_y1)], fill=color, width=8)
        ctx.line([(oiseau_x1, oiseau_y1),
                  (oiseau_x1 + 50, oiseau_y1 - 50)], fill=color, width=8)

class Background:
    """
    Classe pour dessiner l'arrière-plan de l'image (l'herbe en bas de l'image).

    :param int x: Coordonnée x.
    :param int y: Coordonnée y.
    :param int dim: Dimension de l'objet.

    Exemple:
    ::

        img = Image.new("RGB", (1200, 1200), color="DarkTurquoise")
        ctx = ImageDraw.Draw(img)

        b = Background(0, 0, 50)

        b.herbe(ctx)

        img.save("dessin.png")
    """
    def __init__(self, x, y, dim):
        self.x, self.y = x, y 
        self.dim = dim
        
    def herbe(self, ctx):
        """
        Dessine de l'herbe sur l'image.

        :param ctx: Contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw

        """
        largeur, hauteur = ctx.im.size
        # Coo Début du rectangle
        herbe_x = hauteur // 1200
        herbe_y = largeur // 1.05
            
        # Dessin de l'herbe
        x1, y1 = herbe_x, herbe_y
        x2, y2 = hauteur, largeur
        ctx.rectangle([x1, y1, x2, y2], fill="LightGreen")

# Créez une nouvelle image
img = Image.new("RGB", (1200, 1200), color="DarkTurquoise")
ctx = ImageDraw.Draw(img)

c = PremierPlan(0, 0, 50)
b = Background(0, 0, 50)

# Dessin
b.herbe(ctx)
c.soleil(ctx, 50, 50, 50)
c.dessiner_arbre(ctx)
c.oiseau(ctx)

img.save("dessin.png")

if __name__ == '__main__':
    img.show()