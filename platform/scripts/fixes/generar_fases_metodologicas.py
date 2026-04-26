from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 500
bg = (245, 246, 248)
arrow = (196, 198, 201)
box = (11, 46, 79)
border = (235, 237, 240)
white = (242, 244, 247)

img = Image.new("RGB", (W, H), bg)
d = ImageDraw.Draw(img)

# Arrow body and head
d.rectangle([20, 120, W - 300, 380], fill=arrow)
d.polygon([(W - 300, 30), (W - 40, H // 2), (W - 300, H - 30)], fill=arrow)

boxes = [
    (80, 155, 520, 345),
    (560, 155, 1000, 345),
    (1040, 155, 1480, 345),
]
for rect in boxes:
    d.rounded_rectangle(rect, radius=42, fill=box, outline=border, width=4)


def pick_font(size: int):
    for name in ("arialbd.ttf", "Arial Bold.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            pass
    return ImageFont.load_default()


f_mid = pick_font(56)
f_small = pick_font(50)


def draw_multiline_centered(text: str, rect, font, spacing: int = 8):
    x1, y1, x2, y2 = rect
    lines = text.split("\n")
    widths = []
    heights = []

    for line in lines:
        bb = d.textbbox((0, 0), line, font=font)
        widths.append(bb[2] - bb[0])
        heights.append(bb[3] - bb[1])

    total_h = sum(heights) + spacing * (len(lines) - 1)
    y = y1 + (y2 - y1 - total_h) // 2

    for line, w, h in zip(lines, widths, heights):
        x = x1 + (x2 - x1 - w) // 2
        d.text((x, y), line, font=font, fill=white)
        y += h + spacing


draw_multiline_centered("Fase de\ndiagnóstico", boxes[0], f_mid, spacing=10)
draw_multiline_centered("Fase de\nimplementación\npiloto", boxes[1], f_small, spacing=8)
draw_multiline_centered("Fase de\nevaluación", boxes[2], f_mid, spacing=10)

out = r"e:\Maestria\Seminario_De_Investigacion\Investigación\media\fases_metodologicas.png"
img.save(out, format="PNG")
print(out)
