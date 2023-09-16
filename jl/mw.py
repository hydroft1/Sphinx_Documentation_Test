from PIL import Image, ImageDraw

class Background:
    def __init__(self, xy, d):
        self.x, self.y = xy 
        self.dim = d
        
    def herbe(self, ctx):
        largeur, hauteur = ctx.im.size
        # Coo Début du rectangle
        herbe_x = hauteur // 1200
        herbe_y = largeur // 1.05
            
        # Dessin de l'herbe
        x1, y1 = herbe_x, herbe_y
        x2, y2 = hauteur, largeur
        ctx.rectangle([x1, y1, x2, y2], fill="LightGreen")

