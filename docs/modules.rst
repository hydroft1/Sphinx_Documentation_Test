.. py:module:: Test

.. warning::
   **Assurez-vous d'avoir installer PILLOW.**
   
   ``pip install PILLOW``

Classes
=======

.. py:class:: PremierPlan

    Classe pour dessiner des éléments dans le premier plan de l'image(harbre, soleil, oiseau).

    :param int x: Coordonnée x.
    :param int y: Coordonnée y.
    :param int dim: Dimension de l'objet

    .. py:method:: __init__(self, xy, d)

        Initialise un objet PremierPlan avec des coordonnées (xy) et une dimension (d).

    .. py:method:: soleil(self, ctx, rayon, decalage_x, decalage_y)

        Dessine un soleil sur l'image.

        :param ctx: Contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw
        :param int rayon: Rayon du soleil.
        :param int decalage_x: Décalage horizontal du bord de l'image(pour éviter que le soleil soit collé au bordure).
        :param int decalage_y: Décalage vertical du bord de l'image(pour éviter que le soleil soit collé au bordure).


    .. py:method:: dessiner_arbre(self, ctx)

        Dessine un arbre sur l'image.

        :param ctx: contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw

    .. py:method:: oiseau(self, ctx, color="black")

        Dessine un oiseau sur l'image.

        :param ctx: Contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw
        :param str color: Couleur de l'oiseau.

.. py:class:: Background

    Classe pour dessiner l'arrière-plan de l'image (l'herbe en bas de l'image).

    :param int x: Coordonnée x.
    :param int y: Coordonnée y.
    :param int dim: Dimension de l'objet.

    .. py:method:: __init__(self, xy, d)

        Initialise un objet Background avec des coordonnées (xy) et une dimension (d).

    .. py:method:: herbe(self, ctx)

        Dessine de l'herbe sur l'image.

        :param ctx: Contexte graphique pour l'image.
        :type ctx: PIL.ImageDraw.Draw

Exemple d'utilisation
======================

Exemple d'utilisation :

.. code-block:: python

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
