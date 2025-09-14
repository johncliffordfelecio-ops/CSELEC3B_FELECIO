from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 800, 800
MEDAL_RADIUS = 300
CENTER = (WIDTH // 2, HEIGHT // 2)
GOLD_COLOR = (255, 215, 0)
ORANGE = (255, 140, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

img = Image.new("RGB", (WIDTH, HEIGHT), color=WHITE)
draw = ImageDraw.Draw(img)

draw.ellipse([
    (CENTER[0] - MEDAL_RADIUS, CENTER[1] - MEDAL_RADIUS),
    (CENTER[0] + MEDAL_RADIUS, CENTER[1] + MEDAL_RADIUS)
], fill=GOLD_COLOR, outline=BLACK, width=5)

basketball_radius = 100
draw.ellipse([
    (CENTER[0] - basketball_radius, CENTER[1] - basketball_radius),
    (CENTER[0] + basketball_radius, CENTER[1] + basketball_radius)
], fill=ORANGE, outline=BLACK, width=4)

x, y = CENTER
r = basketball_radius
draw.line((x, y - r, x, y + r), fill=BLACK, width=3)
draw.line((x - r, y, x + r, y), fill=BLACK, width=3)
draw.arc((x - r, y - r // 2, x + r, y + r // 2), start=0, end=180, fill=BLACK, width=3)
draw.arc((x - r, y - r // 2, x + r, y + r // 2), start=180, end=360, fill=BLACK, width=3)

try:
    title_font = ImageFont.truetype("arialbd.ttf", 40)
    name_font = ImageFont.truetype("arial.ttf", 30)
except Exception as e:
    print("Font loading failed, using default font.", e)
    title_font = ImageFont.load_default()
    name_font = ImageFont.load_default()

title_text = "Basketball Champion"
title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_height = title_bbox[3] - title_bbox[1]
title_pos = (CENTER[0] - title_width // 2, CENTER[1] - MEDAL_RADIUS + 60)
print("Title bbox:", title_bbox)
print("Title position:", title_pos)
draw.text(title_pos, title_text, fill=BLACK, font=title_font)

name = "John Clifford "
name_text = f"Awarded to: {name}"
name_bbox = draw.textbbox((0, 0), name_text, font=name_font)
name_width = name_bbox[2] - name_bbox[0]
name_height = name_bbox[3] - name_bbox[1]
name_y = CENTER[1] + MEDAL_RADIUS - 100 - name_height // 2
name_pos = (CENTER[0] - name_width // 2, name_y)
print("Name bbox:", name_bbox)
print("Name position:", name_pos)
draw.text(name_pos, name_text, fill=BLACK, font=name_font)

img.show()
img.save("basketball_champion_medal.png")
print("Image saved as basketball_champion_medal.png")
