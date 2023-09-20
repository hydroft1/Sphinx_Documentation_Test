<div class="warning">
    <strong>Assurez-vous d'importer les modules nécessaires (PIL) avant d'utiliser ce code.</strong>
    <code>from PIL import Image, ImageDraw</code>
</div>


## Classe `PremierPlan`

Classe pour dessiner des éléments dans le premier plan de l'image (arbre, soleil, oiseau).

### Paramètres
- `x` (int): Coordonnée x.
- `y` (int): Coordonnée y.
- `dim` (int): Dimension de l'objet.

### Exemple

```python
from PIL import Image, ImageDraw

img = Image.new("RGB", (1200, 1200), color="DarkTurquoise")
ctx = ImageDraw.Draw(img)

c = PremierPlan(0, 0, 50)

c.soleil(ctx, 50, 50, 50)
c.dessiner_arbre(ctx)
c.oiseau(ctx)

img.save("dessin.png")
