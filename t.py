from PIL import Image, ImageDraw, ImageFont

# Paramètres fixés
image_width = 1000
image_height = 450
font_size = 90
text = "CSS"
# Remplacez ceci par le chemin actuel de votre fichier de police
font_path = "Monoton-Regular.ttf"
text_color = (255, 255, 255, 255)  # Blanc en RGBA
bg_color = (66, 71, 84, 255)  # Couleur Hex #424754 en format RGBA

# Créer une nouvelle image avec la couleur d'arrière-plan spécifiée
image = Image.new('RGBA', (image_width, image_height), bg_color)

# Charger la police spécifiée
font = ImageFont.truetype(font_path, font_size)

# Initialiser le contexte de dessin
draw = ImageDraw.Draw(image)

# Calculer la position pour dessiner le texte au centre de l'image
text_width, text_height = draw.textsize(text, font)
x = (image_width - text_width) / 2
y = (image_height - text_height) / 2
# Apply the vertical offset
y -= 12

# Dessiner le texte sur l'image
draw.text((x, y), text, fill=text_color, font=font)

# Enregistrer l'image au format PNG (PNG prend en charge la transparence)
output_path = "images/css.png"
image.save(output_path)
