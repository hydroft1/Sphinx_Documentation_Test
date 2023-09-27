# Projet de Dessin d'Image

Ce projet Python vous permet de créer des images en dessinant divers éléments tels que le soleil, un arbre et un oiseau sur un arrière-plan d'herbe. Il utilise la bibliothèque PIL (Python Imaging Library) pour la manipulation d'images.

## Documentation

si vous souhaitez consulter la documentation de `draw_paysage` : https://hydroft1.github.io/draw_paysage_documentation

## Utilisation

Pour utiliser ce projet, suivez ces étapes :

1. Clonez ce dépôt GitHub sur votre machine locale.
```
git clone https://github.com/hydroft1/projet-de-dessin-image.git
```
2. Assurez-vous d'avoir Python installé sur votre système.

3. Installez la bibliothèque Pillow, qui est une extension de PIL, en utilisant pip.
```
pip install Pillow
```

4. Exécutez le fichier principal pour créer votre propre dessin.
```
python draw_paysage.py
```


L'image résultante sera sauvegardée sous le nom `dessin.png` dans le répertoire du projet.

## Exemples

Voici un exemple de code qui utilise ce projet pour créer une image avec un soleil, un arbre et un oiseau :

```python
import draw_paysage

img = draw_paysage.Image.new("RGB", (1200, 1200), color="DarkTurquoise")
ctx = draw_paysage.ImageDraw.Draw(img)

c = draw_paysage.PremierPlan(50, 50, 50)
b = draw_paysage.Background(ctx, ctx, ctx)

b.herbe(ctx)
c.soleil(ctx, 100, 20, 50)
c.dessiner_arbre(ctx)
c.oiseau(ctx)

img.save("dessin.png")
img.show()
```

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, ouvrez une issue pour discuter de vos idées ou soumettez une demande d'extraction avec vos modifications. Vous pouvez aussi soutenir ce projet avec le sponsor github : https://github.com/sponsors/hydroft1

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](https://github.com/hydroft1/draw_paysage_documentation/blob/master/LICENSE)
 pour plus de détails.
