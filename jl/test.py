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